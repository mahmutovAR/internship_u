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
pytest -n 4

echo "Stopping Selenium Grid"
kill $HUB_PID
kill $NODE_PID
