import pytest

from data.data_generators import RegistrationDataGenerator


@pytest.fixture
def registration_form_data(request):
    fields = request.param
    yield next(RegistrationDataGenerator().generate_registration_data(**fields))
