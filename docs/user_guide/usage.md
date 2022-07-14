# Usage

Using a local copy of the [PyTemplates/fastapi](https://github.com/PyTemplate/fastapi) repository:

```bash
make start
```

Building and running a local docker image:

```bash
make build
make run
```

Pulling and running a public docker image:

```bash
docker pull pytemplates/fastapi:latest
docker run --rm -p 8001:80 pytemplates/fastapi
```
