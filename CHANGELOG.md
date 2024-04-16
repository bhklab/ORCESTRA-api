# CHANGELOG



## v0.4.0-rc.1 (2024-04-16)

### Documentation

* docs: create MultiAssayExperiment-Annotations.md ([`1338540`](https://github.com/bhklab/ORCESTRA-api/commit/13385405ab59d0855a8982f53a01383fbbd0aaeb))

### Feature

* feat: Add new files for ORCESTRA API

This commit includes the addition of several new files for the ORCESTRA API. These files include a new Python script for handling the Snakemake pipeline, documentation on molecular profile annotations, a design documentation file, and a project configuration file. The new Python script includes functions for creating a new Snakemake pipeline and retrieving all pipeline names. The documentation provides information on how to add metadata to a Summarized Experiment. The design documentation file outlines the structure of the project&#39;s documentation. The project configuration file includes the project&#39;s name, version, dependencies, tasks, and semantic release configuration. ([`8b620b0`](https://github.com/bhklab/ORCESTRA-api/commit/8b620b06da0dbdaae5631ab49c26751bc4c198d9))

* feat: restructure documentation files under pipeline directory ([`11e5cff`](https://github.com/bhklab/ORCESTRA-api/commit/11e5cffaf41ba0bd91a2e021209df44d8c0d1d61))

### Unknown

* Merge pull request #23 from bhklab/main

sync w main ([`20f3695`](https://github.com/bhklab/ORCESTRA-api/commit/20f36950afbffce6b2e1a21af7e7fd0c99e86a1e))

* Merge pull request #22 from bhklab/16-define-dnl-schema

16 define dnl schema ([`d480bcf`](https://github.com/bhklab/ORCESTRA-api/commit/d480bcf79ff9a50d2b4da778aa846ebb90632cb3))

* Merge branch &#39;main&#39; into 16-define-dnl-schema ([`6b26baa`](https://github.com/bhklab/ORCESTRA-api/commit/6b26baa5706a1f9dd7bb23c08ae3badcb20b409b))


## v0.2.0 (2024-04-10)

### Build

* build: add pydantic, setup db models ([`07c8093`](https://github.com/bhklab/ORCESTRA-api/commit/07c8093387f20235ef8d55762f66c5a931bc61e6))

### Chore

* chore: update .gitignore Update .gitignore to ignore macOS specific files ([`7590ed5`](https://github.com/bhklab/ORCESTRA-api/commit/7590ed5dc8a50c32a6ad184371fa1c06a37fee8b))

### Ci

* ci: update main.yaml Update Semantic-Release workflow in main.yaml ([`b9d17dd`](https://github.com/bhklab/ORCESTRA-api/commit/b9d17dd333c3953ce2d105d3374b8b797406383f))

* ci: update main.yaml Update Pixi version to v0.19.0 in main.yaml ([`55084a3`](https://github.com/bhklab/ORCESTRA-api/commit/55084a3b07cb6dacee4aa34bdb9a6e58b92f2112))

### Documentation

* docs: Add Pharmacoset-Specific documentation and update DataNutritionLabel model ([`310aa1c`](https://github.com/bhklab/ORCESTRA-api/commit/310aa1cfd0c41d368aeac46a4499e711b7e1070b))

* docs: add data nutrition label diagram to documentation ([`6c53955`](https://github.com/bhklab/ORCESTRA-api/commit/6c539559940765b2712ae993e5d16a4aecde3086))

* docs: Update documentation structure and content

This commit includes several changes to the documentation:
- Updated the table of contents structure in dd.tree
- Added new files for Pipeline-Outputs.md and Data-Nutrition-Label.md
- Modified content in Pipeline-Storage.md and index.md
- Updated the GitHub workflow for building pages
These changes provide more detailed information about pipeline outputs and data nutrition labels, and improve the overall structure and readability of the documentation. ([`99b4c55`](https://github.com/bhklab/ORCESTRA-api/commit/99b4c55a002d44cca23063a51ef191cb444c6507))

* docs: move old docs ([`3e22cfb`](https://github.com/bhklab/ORCESTRA-api/commit/3e22cfb6373d1ff11f5828ce8d7bb0d3487fa9ca))

* docs: add background ([`9a961b7`](https://github.com/bhklab/ORCESTRA-api/commit/9a961b7e503ee4e186ee31774d59bf920caca5b0))

* docs: update background ([`001b719`](https://github.com/bhklab/ORCESTRA-api/commit/001b719effc66a3f333e29c0d4758b57252de4c4))

* docs: Add requirements diagrams and reference images ([`93b2362`](https://github.com/bhklab/ORCESTRA-api/commit/93b2362df7ae2ba1d7d612cabf75098f07f4fbe5))

* docs: add requirements and some reference images ([`13e83ed`](https://github.com/bhklab/ORCESTRA-api/commit/13e83ed777109d1e5b8b7efe25f005c34cd04801))

### Feature

* feat: comment out Semantic-Release workflow in main.yaml ([`f0ba8a7`](https://github.com/bhklab/ORCESTRA-api/commit/f0ba8a7a08193bd33fd026583af7919579a30f8a))

* feat: Add GitHub action for building and deploying documentation ([`e7dafca`](https://github.com/bhklab/ORCESTRA-api/commit/e7dafca4706cce458cbd9b598f5eefeaec974ea1))

* feat: add design documentation

This commit adds design documentation for the ORCESTRA API, including topics on pipeline storage, pipeline standards, Git Flow release cycle, and contributing guidelines. The documentation is organized using JetBrains Writerside software. ([`ee583b4`](https://github.com/bhklab/ORCESTRA-api/commit/ee583b4c536daf9fd453c0e241084311daf97c82))

* feat: add common and pipeline models for MongoDB

This commit introduces two new models for MongoDB: common and pipeline. The common model includes a new type called PyObjectId, which is a string that is validated and converted to a string before storing it as the id field. The pipeline model includes a basic pipeline model and a Snakemake pipeline model that inherits from the basic pipeline model. The Snakemake pipeline model includes additional fields for snakefile_path, config_file_path, and conda_env_file_path. This commit also includes methods to create a student and a Snakemake pipeline in the database. ([`f38c9bb`](https://github.com/bhklab/ORCESTRA-api/commit/f38c9bb1f61720e7a3c1b667206cc31a4ae470d7))

### Merge

* merge: Merge remote-tracking branch &#39;origin&#39; into development ([`2a28a22`](https://github.com/bhklab/ORCESTRA-api/commit/2a28a227c96e079bac63274242ab621ed27441e1))

### Unknown

* Merge pull request #20 from bhklab/16-define-dnl-schema

16 define dnl schema ([`297287f`](https://github.com/bhklab/ORCESTRA-api/commit/297287f28f95e882cadb68caf884a3c5373f6c66))

* Merge remote-tracking branch &#39;origin&#39; into 16-define-dnl-schema ([`90b2e92`](https://github.com/bhklab/ORCESTRA-api/commit/90b2e9218637840c2635005d58ef6ff84658864c))

* update dd.tree, Data-Nutrition-Label.md, Pharmacoset-Specific.md and DataNutritionLabel.py Update DataNutritionLabel model and add Pharmacoset-Specific documentation ([`cb668db`](https://github.com/bhklab/ORCESTRA-api/commit/cb668db3bb7079ee766d495442cef557e198529b))

* Merge pull request #19 from bhklab/staging

Staging ([`147910c`](https://github.com/bhklab/ORCESTRA-api/commit/147910c0ef37a69093ffdbf6ded6af1a2ee6677d))

* Merge pull request #14 from bhklab/development

Development ([`fedb93b`](https://github.com/bhklab/ORCESTRA-api/commit/fedb93b1f2a43627275bfda756128b8326bddea9))

* Merge pull request #17 from bhklab/16-define-dnl-schema

16 define dnl schema ([`1f2242a`](https://github.com/bhklab/ORCESTRA-api/commit/1f2242a460de2b7baa6cfa8174dbd33df544f735))

* first dnl draft ([`fad585a`](https://github.com/bhklab/ORCESTRA-api/commit/fad585a3099d5e7bb2473fcdd6ac3c017bb0a353))

* Update .gitignore and pixi.lock ([`c87ee54`](https://github.com/bhklab/ORCESTRA-api/commit/c87ee5405abf92906ad9285182171973ea1bd536))


## v0.1.5 (2024-04-08)

### Unknown

* Merge pull request #6 from bhklab/staging

Staging ([`23418a6`](https://github.com/bhklab/ORCESTRA-api/commit/23418a6bd9a41bb077c4f3f53d0625380e796fac))

* Merge branch &#39;main&#39; into staging ([`331efb7`](https://github.com/bhklab/ORCESTRA-api/commit/331efb7cd79badc47869290517f888723ba6cf0d))


## v0.1.5-rc.3 (2024-04-08)

### Documentation

* docs: update CHANGELOG.md Merge branch &#39;main&#39; into staging ([`f206256`](https://github.com/bhklab/ORCESTRA-api/commit/f2062562b49356db06934678348a9984d1bd401f))


## v0.1.5-rc.2 (2024-04-08)

### Build

* build(deps): update README.md and pyproject.toml Add Pipeline Specification documentation ([`3d9f8a0`](https://github.com/bhklab/ORCESTRA-api/commit/3d9f8a005dc38ebf62ff378ec224cafb1de27880))


## v0.1.5-rc.1 (2024-04-08)

### Build

* build(deps): update pyproject.toml Update hello command in pyproject.toml ([`3f252cd`](https://github.com/bhklab/ORCESTRA-api/commit/3f252cdf2615b99687a8c7e18a12406c814081dd))

### Chore

* chore: update .gitignore ([`a5fa71d`](https://github.com/bhklab/ORCESTRA-api/commit/a5fa71d730966ce2edb98b9cc122aee15581deb5))

### Documentation

* docs: update README. Add Pipeline-standards documentation ([`a84fb74`](https://github.com/bhklab/ORCESTRA-api/commit/a84fb741002c14b61f0d2449f01d7501085b35dc))

### Unknown

* tests: add test directories with simple snakefiles ([`03552b2`](https://github.com/bhklab/ORCESTRA-api/commit/03552b219b5a7381c1f2c6315a45c8dbb8a0919d))


## v0.1.4 (2024-04-05)

### Unknown

* Merge pull request #4 from bhklab/staging

Staging ([`f6a8f39`](https://github.com/bhklab/ORCESTRA-api/commit/f6a8f39712c0480b9bbc0105ce74c481739913f3))

* Merge branch &#39;main&#39; into staging ([`b0e0c95`](https://github.com/bhklab/ORCESTRA-api/commit/b0e0c956ac94f2032cf29bf6dbecfdcbbfbbd187))


## v0.1.3-rc.4 (2024-04-05)

### Build

* build(deps): update .gitignore and pyproject.toml Update .gitignore and pyproject.toml ([`9cb36dc`](https://github.com/bhklab/ORCESTRA-api/commit/9cb36dc838c0bdb80bf550b0b359479efc0a1cb6))

### Documentation

* docs: update README.md Update badges in README.md ([`2c0b6c1`](https://github.com/bhklab/ORCESTRA-api/commit/2c0b6c1a850575eaedf897c8df33c7b12160ce2b))


## v0.1.3-rc.3 (2024-04-05)

### Ci

* ci: update main.yaml Fix GitHub app token configuration in main.yaml ([`b110a0e`](https://github.com/bhklab/ORCESTRA-api/commit/b110a0e9d44d19ea5a7b83a0ecb2bc935856ca37))


## v0.1.3 (2024-04-05)

### Unknown

* Merge pull request #3 from bhklab/staging

Staging ([`3fa75fb`](https://github.com/bhklab/ORCESTRA-api/commit/3fa75fbd53e2b5af89f296fda508c5a1e69805b8))


## v0.1.3-rc.2 (2024-04-05)

### Ci

* ci: update main.yaml Fix GitHub app token configuration in main.yaml ([`0de2f74`](https://github.com/bhklab/ORCESTRA-api/commit/0de2f7403d933e5e98b06241fd8de53be89b2fe3))

### Unknown

* Merge pull request #2 from bhklab/main

Merge pull request #1 from bhklab/staging ([`4ada7a1`](https://github.com/bhklab/ORCESTRA-api/commit/4ada7a12c9227a0bade3ddb35b12cc6b0e7cdefe))

* Merge pull request #1 from bhklab/staging

ci: add merge as semver tag ([`0dbba42`](https://github.com/bhklab/ORCESTRA-api/commit/0dbba42ce992270d9a170ebb6885c8d8b9dcdc42))


## v0.1.3-rc.1 (2024-04-05)

### Ci

* ci: add merge as semver tag ([`f0b60f5`](https://github.com/bhklab/ORCESTRA-api/commit/f0b60f56335aae40826ae9e347143d79b6b40721))

### Unknown

* remove unused semver ([`a52c959`](https://github.com/bhklab/ORCESTRA-api/commit/a52c9592931dc451b4e3346631d3f6884d378aab))


## v0.1.2 (2024-04-05)

### Documentation

* docs: update 1 file and create 1 file Add semantic versioning and Python Semantic Release configuration ([`703d601`](https://github.com/bhklab/ORCESTRA-api/commit/703d601b7829443ac710c100d2f012c558e8a139))


## v0.1.1 (2024-04-05)

### Ci

* ci: add semver ([`47d19ed`](https://github.com/bhklab/ORCESTRA-api/commit/47d19edfe176877aa60c649889bb2bd44e48715c))


## v0.1.0 (2024-04-05)

### Feature

* feat: add gha ([`66c3925`](https://github.com/bhklab/ORCESTRA-api/commit/66c39253a0b7b320a8c2a5ae96b24011406ab740))


## v0.0.0 (2024-04-05)

### Unknown

* first commit ([`76e7ae7`](https://github.com/bhklab/ORCESTRA-api/commit/76e7ae7c1398ce33ecc51ee2198c48ade87442ad))
