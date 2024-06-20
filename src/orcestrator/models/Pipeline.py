from datetime import datetime, timezone
from pathlib import Path
from shutil import rmtree
from typing import (
    List,
    Optional,
)

from git import Repo
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from orcestrator.core import (
    clone_github_repo,
    pull_latest_pipeline,
    validate_github_repo,
)
from orcestrator.models.common import PyObjectId

class SnakemakePipeline(BaseModel):
    git_url: str
    output_files: List[str]
    snakefile_path: str = Field(
        default='Snakefile',
    )
    config_file_path: str = Field(
        default='config/config.yaml',
    )
    conda_env_file_path: str = Field(
        default='pipeline_env.yaml',
    )


class CreatePipeline(SnakemakePipeline):
    pipeline_name: str
    created_at: Optional[str] = datetime.now(timezone.utc).isoformat()
    last_updated_at: Optional[str] = datetime.now(timezone.utc).isoformat()

    model_config: ConfigDict = {
        'json_schema_extra': {
            'example': {
                'pipeline_name': 'GDSC',
                'git_url': 'https://github.com/BHKLAB-DataProcessing/GDSC-Pharmacoset_Snakemake',
                'output_files': ['results/GDSC.RDS'],
                'snakefile_path': 'Snakefile',
                'config_file_path': 'config/config.yaml',
                'conda_env_file_path': 'pipeline_env.yaml',
            },
        }
    }


class UpdatePipeline(SnakemakePipeline):
    # remove the pipeline_name from the update
    pass


class PipelineOut(SnakemakePipeline):
    pipeline_name: str
    id: PyObjectId = Field(alias='_id', default=None)

    # If needed, add extra fields that should be included in the response
    created_at: Optional[str] = None
    last_updated_at: Optional[str] = None

    @property
    def fs_path(self) -> Path:
        return Path.home() / 'pipelines' / self.pipeline_name

    async def validate_url(self) -> bool:
        return await validate_github_repo(self.git_url)

    async def clone(self) -> Repo:
        return await clone_github_repo(self.git_url, self.fs_path)

    async def validate_local_file_paths(self) -> bool:
        """After cloning, need to validate that the paths provided exist.

        when creating, we ask for snakefile, config and conda env file paths

        Returns:
            bool: True if all paths exist

        Raises:
            AssertionError: If any of the paths do not exist.
        """

        assert self.fs_path.exists(), f'Path: {self.fs_path} does not exist.'

        assert (
            self.fs_path / self.snakefile_path
        ), f'Snakefile: {self.snakefile_path} does not exist.'
        assert (
            self.fs_path / self.config_file_path
        ), f'Config file: {self.config_file_path} does not exist.'
        assert (
            self.fs_path / self.conda_env_file_path
        ), f'Conda env file: {self.conda_env_file_path} does not exist.'
        return True

    async def pull(self) -> None:
        repo = await pull_latest_pipeline(self.fs_path)
        _commit_history = repo.iter_commits()  # unused for now

        try:
            await self.validate_local_file_paths()
        except AssertionError as ae:
            raise Exception(f'Error validating local paths: {ae}')

    async def delete_local(self) -> None:
        rmtree(self.fs_path)
