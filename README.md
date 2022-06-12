# Flask REST API Template

Template to create a REST API with tests, linting, dockerfile and modular achitecture based on Flask.

Inspired by: https://github.com/Sean-Bradley/Seans-Python3-Flask-Rest-Boilerplate

and https://gist.github.com/arundhaj/5f4c0f8c9a8efba9f92f81adea9fd4d7

## Run
```
pipenv install --dev
pipenv shell --anyway
FLASK_APP=app python -m flask run
```

### Run Tests
```
python -m pytest
```

### Linting
```
python -m pylint .
```