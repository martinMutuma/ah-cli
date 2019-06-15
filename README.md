## AH Cli [![Coverage Status](https://coveralls.io/repos/github/martinMutuma/ah-cli/badge.svg)](https://coveralls.io/github/martinMutuma/ah-cli) [![Build Status](https://travis-ci.com/martinMutuma/ah-cli.svg?branch=develop)](https://travis-ci.com/martinMutuma/ah-cli)

 CLI imprementation of [Authors Haven](http://ah-premier-staging.herokuapp.com/api/) API Client

 

# Description

This a python based Cli application

## Documentation

Commands 

1. View single article and export to csv and or json

    ``` ah view <article-slug> --export --json --csv```
2. List articles 

      ``` ah list  --export --json --csv```


### Dependencies
1. python 3.3.7
2. click 7.0
3. pytest

Dev
1. Flake8
2. Autopep8

### Getting Started


1. Git clone the repo 
2. Install and activate virtual environment 
   
    `virtualenv venv`

    `source venv/bin/activate`
3. Install the application 

    `pip install .`

4. Run command

    `ah --help`


## Testing

`pytest`


