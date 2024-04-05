# GitFlow Process and Release Cycle

## GitFlow Process

1. **Development**: All development work happens in the `development` branch. This is where new features, bug fixes, and improvements are added.

2. **Staging**: Once the features are tested and ready, they are merged into the `staging` branch. This branch is used for final testing before the changes are moved to the `main` branch.

3. **Main**: The `main` branch is where the stable version of the code resides. Changes from the `staging` branch are merged into `main` when they are ready for release.

## Release Cycle

The release cycle is managed using Semantic Release, which automates the versioning and changelog generation process. Here's how it works:

1. **Commit Messages**: Each commit message should follow the Conventional Commits specification. This allows Semantic Release to automatically determine the type of version bump (major, minor, or patch) that should be made.

2. **CI/CD Pipeline**: When changes are pushed to the `main` or `staging` branch, the CI/CD pipeline is triggered. This pipeline runs tests, builds the project, and prepares it for release.

3. **Semantic Release**: Semantic Release analyzes the commit messages since the last release, determines the next version number, generates the changelog, and creates a new release.

4. **Changelog**: The changelog is automatically updated with each release, providing a detailed list of the changes made. The changelog can be found in the `CHANGELOG.md` file.

5. **Versioning**: The versioning follows the Semantic Versioning specification. Each release is tagged with the version number in the format `vX.Y.Z`.

Please refer to the [CHANGELOG.md](CHANGELOG.md) and the CI/CD pipeline configuration in [.github/workflows/main.yaml](.github/workflows/main.yaml) for more details.

Tags on the staging branch are used to mark release candidates (RC) and are in the format `vX.Y.Z-rc.N`. Once the RC is tested and ready for release, it is merged into the main branch and tagged with the final version number in the format `vX.Y.Z`.

``` mermaid
%%{init: { 'logLevel': 'debug', 'theme': 'base' } }%%
gitGraph TB:
    checkout main
    commit id: "feat: initial commit"
    branch staging
    branch development
    branch feat1
    commit id: "feat: add feature1"
    branch feat2
    commit id: "feat: add feature2"
    checkout development
    merge feat1 id: "merge: feature1"
    merge feat2 id: "merge: feature2"
    checkout staging
    merge development id: "merge: feature1, feature2" tag: "v1.0.0-rc.1"
    checkout development
    merge staging id: "merge: v1.0.0-rc.1"
    commit id: "fix: fix bug1"
    checkout staging
    merge development id: "merge: fix bug1" tag: "v1.0.0-rc.2"
    checkout main
    merge staging id: "merge: v1.0.0-rc.2" tag: "v1.0.0"
```