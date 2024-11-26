import platform
from dotenv import load_dotenv

from os import system as os_system
from os.path import join as os_path_join
from webbrowser import open as open_report


def main():
    load_dotenv()

    os_system('pytest tests/ -n 4 --alluredir=allure-results --clean-alluredir')

    env_data = [f'os_platform = {platform.system()}\n',
                f'os_release = {platform.release()}\n',
                f'python_version = {platform.python_version()}']

    with open(os_path_join('allure-results', 'environment.properties'), 'w') as env_file:
        for line in env_data:
            env_file.write(line)

    os_system('allure generate allure-report --clean --single-file allure-results')

    open_report(os_path_join('allure-report', 'index.html'))


if __name__ == '__main__':
    main()
