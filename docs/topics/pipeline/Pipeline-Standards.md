# Pipeline Standards

A set of standards that ORCESTRA will assume are followed in all future pipelines


This document outlines a set of standards that all pipelines should follow.

- These standards are designed to ensure that pipelines are easy to use, reproducible, and well-documented.
- They are also designed to make it easier for multiple users to collaborate on a pipeline, and to make it easier for users to reproduce the results of a pipeline.

Fundamentally, any user should be able to:

1) Clone the repository from Github
2) Run the pipeline using the exact command provided in the `README.md`
3) Obtain the same results as the original pipeline run by the curator without the pipeline failing.

It is highly recommended to try these steps out from a fresh environment to ensure that the pipeline is reproducible.

> [!WARNING]
> Failure to adhere to these standards may result in the pipeline being rejected from the project.

## Definitions

- **Pipeline/Workflow**: A set of rules that are run in a specific order to produce a set of output files.
- **Rule/Step**: A set of commands/scripts that are run to produce a set of output files from a set of input files.
- **ORCESTRA**: The project that these standards are being developed for. This projects will be used to store and run pipelines on the cloud.
- **Curator** (of a pipeline): The person responsible for maintaining a pipeline and ensuring that it is up-to-date and working correctly.
- **User**: The person running the pipeline. This could be the same person as the curator, or it could be someone else trying to reproduce the results of the pipeline.
- **Environment**: The set of software and dependencies that are required to run a pipeline or rule.
- **Local environment**: The environment on the user's computer. This includes the operating system, software, and dependencies that are installed on the user's computer.
- **Cluster**: A set of computers that are connected together and used to run jobs in parallel.
- **Container**: Think of a container as a digital box that holds everything needed to run a program or application. It includes all the necessary files, settings, and tools so that the program can work properly. Containers are isolated from the rest of the system, so they won't interfere with other programs or applications. Learn more at [Docker](https://www.docker.com/resources/what-container).
- **Repository**: A place where code and other files are stored. This could be a git repository on Github, Gitlab, or Bitbucket, or it could be a folder on a shared drive or cloud storage.
- **README**: A file that contains information about the repository. This could include instructions on how to run the pipeline, information about the data used in the pipeline, or any other information that is relevant to the pipeline.
- **Snakefile**: A file that contains the rules of the pipeline. This file is used by Snakemake to run the pipeline. See the [Snakemake documentation](https://snakemake.readthedocs.io/en/stable/) for more information.

## 1. Version Control Your Pipeline

All pipelines should be version controlled using git. This allows for easy tracking of changes to the pipeline, as well as easy collaboration between multiple users.

- The pipeline must be stored in a git repository, with a `README.md` file that explains how to run the pipeline.
- The repository must **not** contain any large data files. These should be stored in a separate location, such as a shared drive, cloud storage, or ignored using `.gitignore`.
- The repository must contain a `environment.yaml` file that lists the specific version of `snakemake` and any other dependencies required to run the pipeline. See the [Isolated Environments](#2-isolated-environments) section for more information.
- The repository must contain a `Snakefile` in the root directory that defines the rules of the pipeline.
- If the pipeline needs to be updated or modified in any way, the curator should create a **`new branch`** in the repository (i.e `development`), make the changes, and then create a pull request to merge the changes into the **`main`** branch *when they are certain that the pipeline is working as expected*.
    - This ensures that the `main` branch always contains a working version of the pipeline that can be run by users.
    - For more information on git-flow and branching strategies, see the [Atlassian Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

## 2. Isolated Environments

Snakemake allows for each pipeline to define both the environment the `snakemake` call is run in, as well as the environment that each rule is run in.

- This is a powerful feature that allows for the pipeline to be run in a consistent environment, regardless of the user's local environment.
- This is particularly important when running on a cluster, where the environment may be different than the user's local environment.
- This is also important for reproducibility, as the pipeline will always be run in the same environment, regardless of the user's local environment.
- See the [Snakemake documentation on using conda environments](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#integrated-package-management) for more information.
    - Note: Though snakemake allows [using already existing conda environments](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#using-already-existing-named-conda-environments), it is **required** that `.yaml` files are used to define environments.
- If containers are defined for the pipeline specifically (i.e not using an existing container made by someone else), the `Dockerfile` or `Singularity` file should be included in the repository, along with instructions on how to build the container.

## 3. Documentation

All pipelines should be well-documented, both in the code and in the repository.

- The `README.md` file should contain detailed instructions on how to run the pipeline, including any required input files, parameters, and output files.

### 3.1 Pipeline Instructions

At minimum, the `README.md` file should contain the exact command to run the pipeline, including any required parameters. This should be very clear to users and should not require them to read through the entire `Snakefile` to figure out how to run the pipeline.

- i.e "To run the pipeline, use the following command: `snakemake --use-conda --cores <num_cores>`"

If any additional steps are required, you must let the user know in the README. This could include:

- Setting up additional directories
    - i.e "before running the pipeline you will need to create a `references` directory and download
      the data files from `<URL>` into this directory as `annotations.gtf`" using the following command:
      `mkdir references && wget <URL> -O references/annotations.gtf`

### 3.2 Directory Structure

The directory structure of the pipeline should follow:

``` bash
├── .gitignore
├── README.md
├── environment.yaml
├── workflow/
│   ├── rules/
|   │   ├── module1.smk
|   │   └── module2.smk
│   ├── envs/
|   │   ├── tool1.yaml
|   │   └── tool2.yaml
│   ├── scripts/
|   │   ├── script1.py
|   │   └── script2.R
│   ├── notebooks/
|   │   ├── notebook1.py.ipynb
|   │   └── notebook2.r.ipynb
│   └── report/
|       ├── plot1.rst
|       └── plot2.rst
├── config/
│   ├── config.yaml
│   └── some-sheet.tsv
├── rawdata/
├── procdata/
├── references/
├── logs/
├── metadata/
├── results/
├── resources/
└── Snakefile
```

> [!NOTE] if you do not require a specific directory (i.e `metadata` or `workflow/notebooks`), you can remove it from the directory structure.

### 3.3 Data

All sources of data **must** be well described, either in the `README.md` or in the `config.yaml` file. This includes:

The source of the data (e.g. a URL, a database, etc.)

- If the data is publically available, a link to the data **must** be provided. You cannot assume that any user will be able to find the data on their own.
- If the data is not publically available, the curator should provide instructions on how to obtain the data. This could include contacting the curator directly, using a specific tool to download the data, or the point of contact to who can provide the data (i.e a lab or a database).
- As much metadata as possible about the data (e.g. the format of the data, the size of the data, etc.)
- Any processing that has been done to the data (e.g. normalization, filtering, etc.) BEFORE you obtained the data.

Since the pipeline needs to run on ORCESTRA, any data that is not publically available must be shared with the ORCESTRA team. This could include:

- Providing the data to the ORCESTRA team directly
- Providing a link to the data that the ORCESTRA team can access
- Providing instructions on how to obtain the data from a specific location
    - i.e if the RNASEQ data is on a HPC cluster, the ORCESTRA team should be provided with:
        - The location of the data (path to the data on the cluster `i.e /cluster/projects/lab/rawdata/<your-data>`)
        - The path to the data in the pipeline (i.e "The data is used in `rule build_RNASEQ_SE` as an input `rawdata/rnaseq/xyz.fastq`)
        - This will allow for the team to organize the data in a private cloud datastorage so it can be accessed by the ORCESTRA platform (will not be shared with anyone else).

Data from results of the pipeline should also be well described, including:

- The format of the output files (e.g. RDS, CSV, etc.)
- What the file contains (e.g. a table of gene expression values, a plot of the data, a list of `SummarizedExperiments` objects, a `PharmacoSet` object, etc.)

Relative paths **MUST** be used everywhere in the pipeline.

- You *cannot* assume that the pipeline will be run from a specific directory or that everyone has the same directory structure on their computer.
    - i.e `input: "procdata/drugdata.RDS"` over `input: "/home/user/project/procdata/drugdata.RDS"`
    - i.e `input: "references/genes.gtf"` over `input: "/cluster/projects/bhklab/references/genes.gtf"`
- If you need to use shared data (i.e data that is not stored in your directory), you should create [symbolic links](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/) to the data in your directory
    - i.e `ln -s /cluster/projects/bhklab/references/genes.gtf references/genes.gtf` and use `input: "references/genes.gtf"` in the pipeline.
    - In your README, you should let the user know that they need to set up a directory for `references` with the appropriate data files

### 3.4 Snakefile & Rules

The `Snakefile` and pipeline rules/steps should be self-documenting or well-commented.

- This includes named rules, input/output files, and any parameters that are used in the rules.
    - note: using [directories as outputs](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#resources) is *highly discouraged* unless no other option is available as this can lead to issues with the pipeline in the cloud or on a cluster.
    - If using a tabulated input file, such as a `samples.tsv`, relative paths should be used over absolute paths.
- If using a `script` directive, the name of the script should be the same as the name of the rule
    - i.e `rule build_PharmacoSet` and `script: "scripts/build_PharmacoSet.R"` or a similar naming.
- If using a `conda` directive, the name of the environment file should be the same as the name of the rule, unless a specific environment is required for multiple rules.
    - i.e `rule build_PharmacoSet` and `conda: "envs/build_PharmacoSet.yaml"`
    - i.e `rule build_RNASEQ_SE` and `rule build_CNV_SE` can use the same environment file `conda: "envs/build_SE.yaml"`
- If a rule requires specific resources, this should be implemented in the rule itself and not in the `snakemake` call. See the [Snakemake Resource Documentation](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#resources) for more information.
    - i.e `threads: 4` or `threads: 8`
    - i.e `resources: mem_mb=8000` or `resources: mem_mb=16000`
- `log` files should be generated for each rule, and the log file should be named the same as the rule, with a `.log` extension.
    - i.e `rule build_PharmacoSet` should generate a log file named `build_PharmacoSet.log`

<table>
<tr>
<th>Bad Rule</th>
<th>Good Rule</th>
</tr>
<tr>
<td>

``` python
rule pset:
    input:
        # absolute paths, poor file naming
        "/home/user/mydata/data/drugdata.RDS",
        "/home/user/mydata/data/assay.RDS",
        "/home/user/mydata/data/cellline.RDS",
        "/home/user/mydata/data/drugsdata.RDS",
    output:
        "/home/user/mydata/data/output.RDS",
    log:
        "logs/log.log"
    conda:
        # using a user env instead of a yaml file
        "pharmacogx"
    script:
        # poor naming convention
        "scripts/combine.R"
```

</td>
<td>

``` python
rule build_PharmacoSet:
    input:
        tre = "procdata/treatmentResponseExperiment.RDS",
        mae = "procdata/MultiAssayExperiment.RDS",
        sampleMetadata = "procdata/sampleMetadata.RDS",
        treatmentMetadata = "procdata/treatmentMetadata.RDS",
    output:
        pset = "results/PharmacoSet.RDS",
    log:
        "logs/build_PharmacoSet.log"
    conda:
        "envs/build_PharmacoSet.yaml"
    script:
        "scripts/build_PharmacoSet.R"
```

</td>
</tr>
</table>
