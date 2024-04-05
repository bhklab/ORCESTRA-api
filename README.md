# Snakemake Orchestrator API w/ Kubernetes

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

What this does is create a virtual environment and install the dependencies listed in the `pyproject.toml` file. 
By starting command line commands with `pixi run`, you can run the commands in the specific environment.

```bash
pixi run python -m src.core.snakemake.main
# > Hello World!
```

This ensures that any other packages or dependencies can be synchronized across different environments, systems, and developers.

A feature of pixi is that it can be used to run common tasks.
For example, the above command has been implemented as a pixi task in the `pyproject.toml` file.

To run the task, use the following command:

```bash
pixi run hello
```

TODO:: as development progresses, remove the hello_world function and add a more meaningful function to show the functionality of the project and PIXI in general.


