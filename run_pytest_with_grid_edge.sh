#!/bin/bash

source .env

java -jar $SELENIUM_JAR_PATH hub &
HUB_PID=$!

sleep 2

java -Dwebdriver.edge.driver=$MSEDGE_DRIVER_PATH -jar $SELENIUM_JAR_PATH node --hub http://localhost:4444 &
NODE_PID=$!

sleep 2

./run_pytest_with_rerun_and_allure.sh edge --grid

kill $HUB_PID
kill $NODE_PID