from typing import (
    List,
    Optional,
)
from datetime import datetime, timezone

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
)
from orcestrator.models.common import PyObjectId


class SnakemakePipeline(BaseModel):
    git_url: str
    output_files: List[str]
    snakefile_path: str = Field(
        default="Snakefile",
    )
    config_file_path: str = Field(
        default="config/config.yaml",
    )
    conda_env_file_path: str = Field(
        default="pipeline_env.yaml",
    )


class CreatePipeline(SnakemakePipeline):
    pipeline_name: str
    created_at: Optional[str] = datetime.now(timezone.utc).isoformat()
    last_updated_at: Optional[str] = datetime.now(timezone.utc).isoformat()

    model_config: ConfigDict = {
        "json_schema_extra": {
            "example": {
                "pipeline_name": "GDSC",
                "git_url": "https://github.com/BHKLAB-DataProcessing/GDSC-Pharmacoset_Snakemake",
                "output_files": ["results/GDSC.RDS"],
                "snakefile_path": "Snakefile",
                "config_file_path": "config/config.yaml",
                "conda_env_file_path": "pipeline_env.yaml",
            },
        }
    }


class UpdatePipeline(SnakemakePipeline):
    # remove the pipeline_name from the update
    pass

class PipelineOut(SnakemakePipeline):
    pipeline_name: str
    id: PyObjectId = Field(alias="_id", default=None)

    # If needed, add extra fields that should be included in the response
    created_at: Optional[str] = None
    last_updated_at: Optional[str] = None
