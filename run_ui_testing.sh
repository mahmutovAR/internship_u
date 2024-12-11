#!/bin/bash

browser=$1

case "$browser" in
    firefox)
        if [ "$2" == "grid" ]; then
            ./run_pytest_with_grid_firefox.sh
        else
            ./run_pytest_with_rerun_and_allure.sh firefox
        fi
        ;;
    edge)
        if [ "$2" == "grid" ]; then
            ./run_pytest_with_grid_edge.sh
        else
            ./run_pytest_with_rerun_and_allure.sh edge
        fi
        ;;
    *)
        if [ "$2" == "grid" ]; then
            ./run_pytest_with_grid_chrome.sh
        else
            ./run_pytest_with_rerun_and_allure.sh
        fi
        ;;
esac