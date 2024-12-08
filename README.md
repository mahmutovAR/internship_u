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


## To run `pytest` tests using Selenium Grid
```commandline
./run_tests_with_grid.sh
```
***


### Files and directories:
* `data/` module with data (links, contact data, urls)
* `helpers/` helpers modules
* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `create_env_properties_file.py` info file generating script 
* `requirements.txt` required packages
* `run_tests_with_grid.sh` testing script
***
