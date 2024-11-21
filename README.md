# UI autotests

Application for testing the **[www.way2automation.com](https://www.way2automation.com/)**  

### Tests
* Homepage
* Header contains contact information
* Drop down menu lists
* "Best Selenium Certification Course Online" block
* "Most Popular Software Testing Courses" block
* Footer contains company information and contacts

- Drop down menu lists when scrolling the page

* Redirection from drop down menu by link

- Login page
- Log in with valid data
- Log in with invalid data
- Log out
***


## Requirements
* [Python](https://www.python.org/downloads/) (3.12)  
* [Allure](https://allurereport.org/docs/install/) (2.30.0)  
 
The Python packages can be installed by running  
```commandline
python3 -m pip install -r requirements.txt
```
***


## Run `run_ui_testing.py` to test the [Registration Form](https://www.way2automation.com/way2auto_jquery/registration.php#load_box)

### First Environment Variables `REG_FORM_USERNAME` and `REG_FORM_PASSWORD` are set

### Then `pytest` runs `test_registration_form.py` with allure files generating
```commandline
pytest tests/test_registration_form.py --alluredir=allure-results --clean-alluredir
```

### Next, a file is created with information about the environment, for example:
```
os_platform = Linux
os_release = 6.8.0-40-generic
python_version = Python 3.10.15
```

### Finally, `allure` converts the test results into an HTML report
```commandline
allure generate allure-report --clean --single-file allure-results
```

### and opens it in default browser
```python
import webbrowser
webbrowser.open('index.html')
```
***


### Files and directories:
- `allure-report/index.html` allure report
- `allure-results/` test results directory  
**Note:** These directories will be created after running `run_ui_testing.py`

* `data/` module with page data (links, phone numbers, etc.)
* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `requirements.txt` required packages
* `run_task_ui.py` UI testing script
***
