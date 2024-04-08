# Snakemake Orchestrator API w/ Kubernetes
[![CI-CD](https://github.com/bhklab/ORCESTRA-api/actions/workflows/main.yaml/badge.svg)](https://github.com/bhklab/ORCESTRA-api/actions/workflows/main.yaml)
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)


[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhklab%2FORCESTRA-api%2Fmain%2Fpyproject.toml%3Ftoken%3DGHSAT0AAAAAACJ7UIIIFXW3TQEPGTWC7W5WZQUACSA&query=project.version&label=release&color=red)
](https://github.com/bhklab/ORCESTRA-api/tree/main)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fbhklab%2FORCESTRA-api%2Fstaging%2Fpyproject.toml%3Ftoken%3DGHSAT0AAAAAACJ7UIIJLPEYVLIHZVHXLEUOZQUADVQ&query=project.version&label=staging&color=orange)
](https://github.com/bhklab/ORCESTRA-api/tree/staging)

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
pixi run python -m src.core.snakemake.main
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


## Semantic Versioning

For a detailed explanation of the release process, please refer to the [GitFlow Process and Release Cycle](docs/GitFlow-Process_ReleaseCycle.md).

This project uses [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) for
automatic versioning and changelog generation.

It is implemented via [GitHub Actions](.github/workflows/main.yml) and the configuration can be found in the [pyproject.toml](pyproject.toml) file.
