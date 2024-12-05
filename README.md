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


## Run `./run_testing.sh` in the root directory to run tests and generate Allure report
***


### Files and directories:
- `allure-report/index.html` allure report
- `allure-results/` test results directory  
**Note:** These directories will be created after running `run_ui_testing.py`

* `data/` module with data (links, contact data, urls)
* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `requirements.txt` required packages
* `run_task_ui.py` UI testing script
***
