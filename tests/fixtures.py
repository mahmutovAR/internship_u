import pytest

from data.data_generators import RegistrationDataGenerator
from helpers import cookie_helper


@pytest.fixture
def registration_form_data(request):
    fields = request.param
    yield next(RegistrationDataGenerator().generate_registration_data(**fields))


@pytest.fixture
def delete_cookies_file():
    yield
    if cookie_helper.file_exists():
        cookie_helper.remove_cookies_file()
