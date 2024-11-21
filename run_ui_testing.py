import platform
from os import environ
from os import system as os_system
from os.path import join as os_path_join
from webbrowser import open as open_report

from faker import Faker


def set_env_var():
    """Sets Environment Variables."""
    # check if EnvVar are set:
    fake = Faker()
    try:
        environ['REG_FORM_USERNAME']
    except KeyError:
        environ['REG_FORM_USERNAME'] = fake.user_name()

    try:
        environ['REG_FORM_PASSWORD']
    except KeyError:
        environ['REG_FORM_PASSWORD'] = fake.password()


    # set EnvVar only for test run:
    # fake = Faker()
    # environ['REG_FORM_USERNAME'] = fake.user_name()
    # environ['REG_FORM_PASSWORD'] = fake.password()


def main():
    set_env_var()

    os_system('pytest tests/test_registration_form.py --alluredir=allure-results --clean-alluredir')

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
