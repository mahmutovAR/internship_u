#!/bin/bash

source .env

echo "Starting Selenium Hub"
java -jar $SELENIUM_JAR_PATH hub &
HUB_PID=$!

sleep 2

echo "Starting Selenium Node"
java -Dwebdriver.chrome.driver=$CHROME_DRIVER_PATH -jar $SELENIUM_JAR_PATH node --hub http://localhost:4444 &
NODE_PID=$!

sleep 2

echo "Running pytest tests"
pytest -n 4 --alluredir=allure-results --clean-alluredir

echo "Creating file with main information about the environment"
python3 create_env_properties_file.py

echo "Generating Allure report"
allure generate allure-report --clean --single-file allure-results

echo "Stopping Selenium Grid"
kill $HUB_PID
kill $NODE_PID
