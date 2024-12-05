# UI autotests
***


## Requirements
* [Python](https://www.python.org/downloads/) (3.12)  
* [Allure](https://allurereport.org/docs/install/) (2.30.0)  
 
The Python packages can be installed by running  
```commandline
python3 -m pip install -r requirements.txt
```
***


## To run `pytest`, rerun failed tests, and generate an `Allure` report
```commandline
./run_pytest_with_rerun_and_allure.sh
```
***


### Files and directories:
- `allure-report/index.html` allure report
- `allure-results/` test results directory  
**Note:** These directories will be created after running testing script

* `data/` module with data (links, contact data, urls)
* `helpers/` helpers modules
* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `create_env_properties_file.py` info file generating script 
* `requirements.txt` required packages
* `run_pytest_with_rerun_and_allure.sh` testing script
***
