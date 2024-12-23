# UI autotests
***


## Requirements
* [Python](https://www.python.org/downloads/) (3.12)  
* [Allure](https://allurereport.org/docs/install/) (2.30.0)  
* [Selenium Server](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.27.0) (4.27.0)

Browsers and WebDrivers:
* [Chrome](https://www.google.com/intl/en_us/chrome/) / [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable)
* [Firefox](https://www.mozilla.org/en-US/firefox/new/) / [GeckoDriver](https://geckodriver.com/download/)
* [Edge]() / [MSEdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/)

The Python packages can be installed by running  
```commandline
python3 -m pip install -r requirements.txt
```
***


## Running tests
To run autotests in a specified browser and with or without Selenium Grid,  
run the `run_ui_testing.sh` script with the appropriate `{browser name}` and `grid` (if it should be used) arguments

For example, to run tests in `Firefox` without Selenium Grid, run:
```
./run_ui_testing.sh firefox
```
And to run tests in `Edge` with Selenium Grid, run:
```
./run_ui_testing.sh edge grid
```
By default, `./run_ui_testing.sh` command runs tests in `Chrome` without Selenium Grid

**Note:** UI testing script reruns twice failed tests and generates an `Allure` report

## To run BDD tests
1. Uninstall `allure-pytest==2.13.5`
2. Install `allure-pytest-bdd==2.13.5` and `pytest-bdd==8.1.0`
3. Edit `run_pytest_with_rerun_and_allure.sh` script, remove `--ignore=tests/bdd/` from `pytest` commands  
Example of the script:
```
#!/bin/bash

echo "Running all tests, failed tests rerun 2 times"
pytest -n 5 --reruns 2 --maxfail=5 --disable-warnings --alluredir=allure-results --clean-alluredir --browser="$1" "$2"

echo "Running failed tests"
pytest --last-failed --disable-warnings --alluredir=allure-results

echo "Creating file with main information about the environment"
python3 create_env_properties_file.py

echo "Generating Allure report"
allure generate allure-report --clean --single-file allure-results
```
4. Run tests by using `run_ui_testing.sh` script
***


### Files and directories:
- `allure-report/index.html` allure report
- `allure-results/` test results directory  
**Note:** These directories will be created after running tests script

* `data/` module with data (links, contact data, urls, browser driver paths)
* `helpers/` helpers modules (cookie helper, driver factory)
* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `create_env_properties_file.py` info file generating script
* `requirements.txt` required packages
* `run_pytest_with_grid_chrome.sh` testing script
* `run_pytest_with_grid_edge.sh` testing script
* `run_pytest_with_grid_firefox.sh` testing script
* `run_pytest_with_rerun_and_allure.sh` testing script
* `run_ui_testing.sh` testing script
***
