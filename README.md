# Snakemake Orchestrator API w/ Kubernetes

[![CI-CD](https://github.com/bhklab/ORCESTRA-api/actions/workflows/main.yaml/badge.svg)](https://github.com/bhklab/ORCESTRA-api/actions/workflows/main.yaml)
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhklab%2FORCESTRA-api%2Fmain%2Fpyproject.toml%3Ftoken%3DGHSAT0AAAAAACJ7UIIIFXW3TQEPGTWC7W5WZQUACSA&query=project.version&label=release&color=red)
](https://github.com/bhklab/ORCESTRA-api/tree/main)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhklab%2FORCESTRA-api%2Fstaging%2Fpyproject.toml%3Ftoken%3DGHSAT0AAAAAACJ7UIIJLPEYVLIHZVHXLEUOZQUADVQ&query=project.version&label=staging&color=orange)
](https://github.com/bhklab/ORCESTRA-api/tree/staging)

## Miro board of design:

https://miro.com/app/board/uXjVKLKSUGQ=/


## Setup

This project uses [Pixi](https://pixi.sh/dev/) to manage packages and the environment.

```bash
# linux / mac os
curl -fsSL https://pixi.sh/install.sh | bash
```

To install the dependencies, run the following command:

```bash
pixi install
```

What this does is create a virtual environment and install the dependencies listed in the [pyproject.toml](pyproject.toml) file.
By starting command line commands with `pixi run`, you can run the commands in the specific environment.

```bash
pixi run python -m orcestrator.core.main
# > Hello World!
```

This ensures that any other packages or dependencies can be synchronized across different environments, systems, and developers.

A feature of pixi is that it can be used to run common tasks.
For example, the above command has been implemented as a pixi task in the [pyproject.toml](pyproject.toml) file.

To run the task, use the following command:

```bash
pixi run hello
# > ✨ Pixi task (default): python -m src.core.main
# > Hello, World!
```

TODO:: as development progresses, remove the hello_world function and add a more meaningful function to show the functionality of the project and PIXI in general.

### Pre-commit

This project has pre-commit hooks enabled to ensure that the code is formatted correctly and that the tests pass before committing.
To install the pre-commit hooks, run the following command:

```bash
pixi run pre-commit install
```

Then run:

```bash
pixi run pre-commit run --all-files
```

This will run the pre-commit hooks on all files in the repository.
If there are any issues, they will be displayed in the terminal, and most often, the file will be automatically formatted.

From now on, anytime you commit, the pre-commit hooks will run automatically. If there are any issues, the commit will be rejected until the issues are resolved. Most often, you can just run `git commit` again and the issues will be fixed.

## Pipeline Specification

This project is aims to orchestrate the deployment and execution of Snakemake workflows on Kubernetes clusters.
As such, it makes some assumptions about the structure of the workflow and the environment in which it is executed.

All pipelines must follow the [Pipeline Standards](old_docs/Pipeline-standards.md) (WORK IN PROGRESS)

## Semantic Versioning

For a detailed explanation of the release process, please refer to the [GitFlow Process and Release Cycle](https://bhklab.github.io/ORCESTRA-api/git-flow-release-cycle.html).

This project uses [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) for
automatic versioning and changelog generation.

It is implemented via [GitHub Actions](.github/workflows/main.yml) and the configuration can be found in the [pyproject.toml](pyproject.toml) file.
