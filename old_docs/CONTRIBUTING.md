# Contributing

## Getting Started

This project uses a number of tools and technologies. Here's a brief overview:

- **Python**: The main language used in this project. If you're not familiar with it, you can learn more about it [here](https://www.python.org/about/gettingstarted/).
- **Pixi**: A tool used for managing Python environments and dependencies. You can learn more about it [here](https://pixi.sh).
- **Semantic Versioning**: A versioning scheme for software that aims to convey meaning about the underlying changes with each release. You can learn more about it [here](https://semver.org/).
- **Pre-commit**: A framework for managing and maintaining multi-language pre-commit hooks. You can learn more about it [here](https://pre-commit.com/).

## Semantic Versioning

This project uses [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) for automatic versioning and changelog generation. It is implemented via GitHub Actions and the configuration can be found in `.github/workflows/main.yml`.

For a detailed explanation of the release process, please refer to the [GitFlow Process and Release Cycle](GitFlow-Process_ReleaseCycle.md).


## Understanding the Project Structure

The project is structured as follows:

- `src/`: This is where the main source code of the project resides.
- `tests/`: This directory contains all the test files.
- `.github/workflows/`: This directory contains GitHub Actions workflows for continuous integration and deployment.
- `docs/`: This directory contains the project documentation.

## How to Contribute

1. **Fork the repository**: Start by forking the repository to your own GitHub account.

2. **Clone the repository**: Next, clone the repository to your local machine so you can start making changes.

3. **Create a new branch**: Always create a new branch for your changes. This keeps the project history clean and easy to navigate.

4. **Make your changes**: Make the changes you want to contribute. Be sure to follow the coding style and conventions used throughout the project.

5. **Test your changes**: Before submitting your changes, make sure all tests pass.

6. **Submit a pull request**: Finally, submit a pull request to the `development` branch with your changes. Be sure to provide a clear and detailed description of your changes.


## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality and consistency. Before you can commit your changes, the pre-commit hooks will run checks on your code. If any of these checks fail, you will need to fix the issues before you can commit your changes.

## Questions

If you have any questions or run into any issues, please open an issue on the GitHub repository.
