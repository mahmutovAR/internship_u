# UI autotests

Application for testing the **[www.way2automation.com](https://www.way2automation.com/)**  

### Testcases
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
 
The Python packages can be installed by running  
```commandline
python3 -m pip install -r requirements.txt
```
***


## Run `pytest` to test the UI
***


### Files and directories:
* `data/` module with page data (links, phone numbers, etc.)
* `locators/` locators modules
* `pages/` web pages modules
* `tests/` test modules
* `requirements.txt` required packages
* `run_task_ui.py` UI testing script
***
***

## Issues
1. Pop-up ad can be closed by using `Explicit waits`, but it is not stable
```python
WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located(ads_close))
browser.find_element(*ads_close).click()
```
it is more efficient to use the following code
```python
time.sleep(6)
body.send_keys(Keys.ESCAPE)
```

2. Running `pytest` fails few tests (pop-up ad not closed or page not loaded),  
but if run the tests one by one, they all pass
```commandline
pytest tests/test_home_page.py
```
```commandline
pytest tests/test_menu_when_scrolling.py
```
```commandline
pytest tests/test_menu_redirect.py
```
```commandline
pytest tests/test_login_page.py
```
