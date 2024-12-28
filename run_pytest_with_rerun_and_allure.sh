#!/bin/bash

pytest -n 5 --reruns 2 --maxfail=5 --disable-warnings --alluredir=allure-results --clean-alluredir --browser="$1" "$2" --ignore=tests/bdd/

pytest --last-failed --disable-warnings --alluredir=allure-results --ignore=tests/bdd/

python3 create_env_properties_file.py

allure generate allure-report --clean --single-file allure-results
