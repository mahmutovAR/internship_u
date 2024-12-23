#!/bin/bash

echo "Running all tests, failed tests rerun 2 times"
pytest -n 5 --reruns 2 --maxfail=5 --disable-warnings --alluredir=allure-results --clean-alluredir --browser="$1" "$2" --ignore=tests/bdd/

echo "Running failed tests"
pytest --last-failed --disable-warnings --alluredir=allure-results --ignore=tests/bdd/

echo "Creating file with main information about the environment"
python3 create_env_properties_file.py

echo "Generating Allure report"
allure generate allure-report --clean --single-file allure-results
