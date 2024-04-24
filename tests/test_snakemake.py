import pytest
from orcestrator.db.models import SnakemakePipeline
import datetime
from orcestrator.core.snakemake import build_snakemake_command


@pytest.fixture(scope="module")
def snakemake_pipeline():
    today_pipeline: str = (
        f"pipeline_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    return SnakemakePipeline(
        name=today_pipeline,
        git_url="github.com/repo",
        output_files=["results/summary.txt"],
        snakefile_path="./Snakefile",
    )


def test_build_snakemake_command(snakemake_pipeline):
    command: list[str] = build_snakemake_command(
        pipeline=snakemake_pipeline,
        work_dir="./tests/test_snakemake-workflows/simple_Snakefile",
    )

    today_pipeline: str = (
        f"pipeline_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )

    expected_command = [
        "snakemake",
        "--snakefile tests/test_snakemake-workflows/simple_Snakefile/Snakefile",
        "--directory tests/test_snakemake-workflows/simple_Snakefile",
        f"--config pipeline_name={today_pipeline} git_url=github.com/repo",
        "--use-conda",
        "--conda-prefix tests/test_snakemake-workflows/simple_Snakefile/conda",
        "--jobs 1",
        "results/summary.txt",
    ]
    assert command == expected_command
