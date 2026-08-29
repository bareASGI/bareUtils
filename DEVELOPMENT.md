# Development

The project uses standard tooling with Python >= 3.12.

To develop, create a virtual environment and install the project.

```bash
$ python -m venv .venv
$ . .venv/bin/activate
(.venv) $ pip install -e '.[dev,dcos]'
```

To build install the standard build and run it.

```bash
(.venv) $ pip install build
(.venv) $ python -m build
```

To upload use twine.

```bash
(.venv) $ pip install twine
(.venv) $ twine upload dist/*
```

## Testing

The project uses pytest.

```bash
(.venv) $ pytest
```

You can also check the coverage.

```bash
(.venv) $ coverage run -m pytest
(.venv) $ coverage report -m
(.venv) $ coverage html
```

## Creating the documentation

Build and deploy to gh-pages

```bash
mike deploy --push --update-aliases 5.0 latest
```

Set the default version.

```bash
mike set-default --push latest
```
