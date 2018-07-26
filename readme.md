DerbyPy Project Extras Demo
###########################

[![CircleCI](https://circleci.com/gh/DerbyPy/project-extras.svg?style=svg)](https://circleci.com/gh/DerbyPy/project-extras)
[![codecov](https://codecov.io/gh/DerbyPy/project-extras/branch/master/graph/badge.svg)](https://codecov.io/gh/DerbyPy/project-extras)

Demo Steps
==========

1) build app
2) install packages along the way
3) build tests
4) show code coverage
5) create .env file
6) create pipenv scripts section
7) setup tox
8) add circleci config
9) test with circleci CLI command
10) check coverage
11) close gap in coverage
12) add badges

Bonus: explain how Python dependencies work

Improvements
============

* use circleci Python containers
* use circleci to cache dependencies per their example:

```yaml

# Download and cache dependencies
- restore_cache:
    keys:
    - v1-dependencies-{{ checksum "requirements.txt" }}
    # fallback to using the latest cache if no exact match is found
    - v1-dependencies-

- run:
    name: install dependencies
    command: |
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

- save_cache:
    paths:
    - ./venv
    key: v1-dependencies-{{ checksum "requirements.txt" }}

```
