from orcestrator.db.models import SnakemakePipeline


def get_snakemake_cmd(
    pipeline: SnakemakePipeline,
    work_dir: str,
) -> str:

    cmd = [
        "snakemake",
        f"--snakefile {work_dir}/{pipeline.snakefile_path}",
        f"--directory {work_dir}",
        f"--use-conda",
        f"--conda-prefix {work_dir}/conda",
        f"--jobs {pipeline.jobs}",
        f"{' '.join(pipeline.output_files)}",
    ]

    return " ".join(cmd)


if __name__ == "__main__":
    import datetime

    today_pipeline: str = (
        f"pipeline_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    snakemake_pipeline = SnakemakePipeline(
        name=today_pipeline,
        git_url="github.com/repo",
        output_files=["results/summary.txt"],
        snakefile_path="./Snakefile",
    )

    print(
        get_snakemake_cmd(
            snakemake_pipeline, "./tests/test_snakemake-workflows/simple_Snakefile"
        )
    )
