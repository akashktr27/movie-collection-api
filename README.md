# Movie Collection API

## Overview
This project pull movies from third party API with basic authentication, and can create collection based on the movies
produced.

## documentation
- Refer docs/index.html file using any browser for endpoint usage.

## Prerequisites
- `Python` >= 3.9.2
- `make`
- `pipenv`

## Makefile Commands for local setup
Need .env file which should contain url, username and password of the movie API.
`url=url`
`username=username`
`password=password`


### `make commands to install using Pipfile`
- make env => Creates an virtual environment
- make install => install the necessary dependencies using Pipfile
- make run => run the server
- make test => run all the unit tests to avoid ruining existing feature

### `make commands to install using requirements.txt`
- make renv => Creates an virtual environment
- make rinstall => install the necessary dependencies using Pipfile
- activate the environment using "source venv/bin/activate"
- make run => run the server
- make test => run all the unit tests to avoid ruining existing feature


