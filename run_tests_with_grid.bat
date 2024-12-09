@echo off
setlocal

set SCRIPT_DIR=%~dp0
set ALLURE_RESULTS_DIR=%~dp0\allure-results

for /f "tokens=1,2 delims==" %%k in (.env) do set %%k=%%~v

echo Starting Selenium Hub
start java -jar %SELENIUM_JAR_PATH% -role hub -port 4444

timeout /t 2

echo Starting Selenium Node
start java -Dwebdriver.chrome.driver=$CHROME_DRIVER_PATH% -jar %SELENIUM_JAR_PATH% -role node -hub http://localhost:4444

timeout /t 2

echo Running pytest tests
pytest -n 4 --alluredir=%ALLURE_RESULTS_DIR% --clean-alluredir

echo Creating file with main information about the environment
python3 "%SCRIPT_DIR%create_env_properties_file.py"

echo Generating Allure report
allure generate allure-report --clean --single-file %ALLURE_RESULTS_DIR%

echo Stopping Selenium Grid
taskkill /f /im java.exe

pause
endlocal