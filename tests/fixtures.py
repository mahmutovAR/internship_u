import pytest

from data.data_generators import RegistrationDataGenerator, AlertsDataGenerator
from helpers import cookie_helper


@pytest.fixture
def registration_form_data(request):
    fields = request.param
    yield next(RegistrationDataGenerator().generate_registration_data(**fields))


@pytest.fixture
def alerts_form_data():
    yield next(AlertsDataGenerator().generate_alert_data())


@pytest.fixture
def delete_cookies_file():
    yield
    if cookie_helper.file_exists():
        cookie_helper.remove_cookies_file()


@pytest.fixture
def data_storage():
    return {}
