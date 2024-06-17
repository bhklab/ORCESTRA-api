from pathlib import Path

from orcestrator.db.models import SnakemakePipeline

def build_snakemake_command(
    pipeline: SnakemakePipeline,
    work_dir: str,
    dryrun: bool = False,
) -> list[str]:

    WORKDIR = Path(work_dir)
    if not WORKDIR.exists():
        raise FileNotFoundError(f"Working directory not found at {WORKDIR}")

    SNAKEFILE_PATH: Path = WORKDIR / Path(pipeline.snakefile_path)
    if not SNAKEFILE_PATH.exists():
        raise FileNotFoundError(f"Snakefile not found at {SNAKEFILE_PATH}")

    METADATA: dict[str, str] = {
        "pipeline_name": pipeline.pipeline_name,
        "git_url": pipeline.git_url,
    }

    cmd: list[str] = [
        "snakemake",
        f"--snakefile {SNAKEFILE_PATH}",
        f"--directory {WORKDIR}",
        f"--config {' '.join([f'{k}={v}' for k, v in METADATA.items()])}",
        "--use-conda",
        f"--conda-prefix {WORKDIR}/conda",
        f"--jobs {pipeline.jobs}",
        f"{' '.join(pipeline.output_files)}",
    ]

    if dryrun:
        cmd.append("--dryrun")

    return cmd
