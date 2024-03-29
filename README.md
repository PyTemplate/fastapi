<p align="center">
  <a href="https://user-images.githubusercontent.com/20674972/178172752-abd4497d-6a0e-416b-9eef-1b1c0dca8477.png">
    <img src="https://user-images.githubusercontent.com/20674972/178172752-abd4497d-6a0e-416b-9eef-1b1c0dca8477.png" alt="Pytemplates Banner" style="width:100%;">
  </a>
</p>

<p align="center">
  <a href="https://github.com/PyTemplate/fastapi/actions/workflows/test.yaml">
    <img src="https://github.com/PyTemplate/fastapi/actions/workflows/test.yaml/badge.svg" alt="Test status">
  </a>

  <a href="https://github.com/PyTemplate/fastapi/actions/workflows/lint.yaml">
    <img src="https://github.com/PyTemplate/fastapi/actions/workflows/lint.yaml/badge.svg" alt="Linting status">
  </a>

  <!-- <a href="https://github.com/PyTemplate/fastapi/actions/workflows/release.yaml">
    <img src="https://github.com/PyTemplate/fastapi/actions/workflows/release.yaml/badge.svg" alt="Release status">
  </a> -->

  <a href="https://results.pre-commit.ci/latest/github/PyTemplate/fastapi/main">
    <img src="https://results.pre-commit.ci/badge/github/PyTemplate/fastapi/main.svg" alt="pre-commit.ci status">
  </a>

  <a href="https://codecov.io/gh/PyTemplate/fastapi">
    <img src="https://codecov.io/gh/PyTemplate/fastapi/branch/main/graph/badge.svg?token=HG1NQ8HRA4" alt="Code coverage status">
  </a>
</p>

## Description

### A production ready FastAPI template

- Metadata and dependency information is stored in the pyproject.toml for compatibility with both [pip](https://pip.pypa.io/en/stable/) and [poetry](https://python-poetry.org/docs/).
- [Flake8](https://flake8.pycqa.org/en/latest/), [pylint](https://pylint.pycqa.org/en/latest/index.html), and [isort](https://pycqa.github.io/isort/) configurations are defined to be compatible with the [black](https://black.readthedocs.io/en/stable/) autoformatter.
- Pylint settings are based on the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) and adapted for black compatibility.
- Linting tools run automatically before each commit using [pre-commit](https://pre-commit.com/), black, and isort.
- Test coverage reports are generated during every commit and pull request using [coverage](https://coverage.readthedocs.io/en/6.4.1/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/). All reports are automatically uploaded and archived on [codecov.io](https://about.codecov.io/).
- Unit tests are written using [pytest](https://docs.pytest.org/en/latest/) and static type checking is provided by [mypy](http://mypy-lang.org/index.html).
- Docker images are automatically published to [Docker Hub](https://hub.docker.com/) during every release. Images are tagged with a semantic version number with dynamic versioning provided by [bump2version](https://github.com/c4urself/bump2version).
- Release notes are automatically generated during every release using [github actions](https://docs.github.com/en/actions).

## Installation

Clone a copy of the [Pytemplates/fastapi](https://github.com/PyTemplate/fastapi) repository:

```bash
git clone https://github.com/PyTemplate/fastapi
```

Or download the latest image using `docker`:

```bash
docker pull pytemplates/fastapi:latest
```

## Usage

Run a local uvicorn server:

```bash
make start
```

Build and run a local docker image:

```bash
make build
make run
```

Download and run the public docker image:

```bash
docker pull pytemplates/fastapi:latest
docker run --rm -p 8001:80 pytemplates/fastapi
```

## Developer Setup

To begin local development, clone the [PyTemplates/fastapi](https://github.com/PyTemplate/fastapi) repository and use one of the following methods to build it. Commands should be executed from inside of the project home folder.

### Using poetry

```bash
poetry install
```

Install optional dependencies using the `--extras` flag:

```bash
poetry install --extras=environment
```

### Using pip

```bash
pip install .
```

Install optional dependencies using square brackets:

```bash
pip install .[environment]
```

### Environments

```python
test = [
    "pytest",
    "pytest-cov",
]

lint = [
    "black",
    "isort",
    "flake8",
    "pylint",
    "mypy",
    "pre-commit",
]

docs = [
    "mkdocs",
    "mkdocstrings",
    "mkdocstrings-python",
    "mkdocs-material",
]

# Includes all optional dependencies
dev = [
    "pytest",
    "pytest-cov",
    "black",
    "isort",
    "flake8",
    "pylint",
    "mypy",
    "pre-commit",
    "mkdocs",
    "mkdocstrings",
    "mkdocstrings-python",
    "mkdocs-material",
    "bump2version",
]
```

### Using a local docker build

To build an image locally from the Dockerfile:

```bash
make build
```

To run the image:

```bash
make run
```

## Commands

- `make start` - Launch the API from a local uvicorn server.

- `make build` - Build a docker image locally using the Dockerfile. The image will be named *pytemplates_fastapi*.

- `make run` - Launch the API from a local docker container using the *pytemplates_fastapi* image.

- `make test` - Run the tests using pytest.

- `make lint` - Run the linting tools. Includes pre-commit hooks, black, isort, flake8, pylint, and mypy.

- `make check` - Run the test and lint commands.

- `make clean` - Remove all build, testing, and static documentation files.

- `make gen-docs` - Generate HTML documentation.

- `make docs` - Generate HTML documentation and serve it to the browser.

- `make pre-release increment={major/minor/patch}` - Bump the version and create a release tag. Should only be run from the *main* branch. Passes the increment value to bump2version to create a new version number dynamically. The new version number will be added to *\__version__.py* and *pyproject.toml* and a new commit will be logged. The release tag will be created from the new commit.

## Workflows

- `test` - Run the tests on every push/pull_request to the *main* branch. Writes a coverage report using pytest-cov and uploads it to codecov.io. Tests run against python versions 3.8 and 3.9. Optional manual trigger in the github actions tab.

- `lint` - Run the linting tools on every push/pull_request to the *main* branch. Includes pre-commit hooks, black, isort, flake8, pylint, and mypy. Optional manual trigger in the github actions tab.

- `docs` - Build the documentation, publish to the *docs* branch, and release to github pages. Runs on a manual trigger in the github actions tab.

- `docker` - Build the docker image, tag it with the branch name, and publish it to dockerhub. Runs on a manual trigger in the github actions tab.

- `release` - Build a docker image, create a github release, and publish to Docker Hub whenever a new tag is created. Linting and testing steps must pass before the release steps can begin. All github release tags and docker image tags are in agreement with one another and follow semantic versioning standards.

## Releases

A release should consist of the following two steps from a tested, linted, and up to date copy of the *main* branch:

1. `make pre-release increment={major/minor/patch}` - Commit the version bump and create a new tag locally. The version number follows semantic versioning standards (major.minor.patch) and the tag is the version number prepended with a 'v'.

2. `git push --follow-tags` - Update the *main* branch with only the changes from the version bump. Publish the new tag and kick off the release workflow.

## File Tree

```bash
.
├── Dockerfile
├── docs
│   ├── developer_guide
│   │   ├── commands.md
│   │   ├── developer_setup.md
│   │   ├── releases.md
│   │   └── workflows.md
│   ├── extras
│   │   ├── credits.md
│   │   └── file_tree.md
│   ├── index.md
│   └── user_guide
│       ├── installation.md
│       └── usage.md
├── LICENSE
├── Makefile
├── mkdocs.yml
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   └── pytemplates_fastapi
│       ├── app
│       │   ├── main.py
│       │   └── router.py
│       ├── controllers
│       │   ├── __init__.py
│       │   └── message.py
│       ├── db
│       │   ├── connections.py
│       │   ├── __init__.py
│       │   ├── mock_database.json
│       │   └── session.py
│       ├── __init__.py
│       ├── models
│       │   ├── host_info.py
│       │   ├── http.py
│       │   ├── __init__.py
│       │   └── message.py
│       ├── routes
│       │   ├── home.py
│       │   ├── __init__.py
│       │   └── messages.py
│       └── __version__.py
└── tests
    ├── conftest.py
    ├── __init__.py
    ├── test_database.json
    ├── test_home.py
    ├── test_messages.py
    └── test_performance.py
```

## Credits

### Other python package templates

- [https://github.com/waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage)
- [https://github.com/AllenCellModeling/cookiecutter-pypackage](https://github.com/AllenCellModeling/cookiecutter-pypackage)

### Actions

- [https://github.com/JamesIves/github-pages-deploy-action](https://github.com/JamesIves/github-pages-deploy-action)
- [https://github.com/softprops/action-gh-release](https://github.com/softprops/action-gh-release)
