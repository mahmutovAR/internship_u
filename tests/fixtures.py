from random import choice, randrange, sample

import pytest
from faker import Faker


@pytest.fixture
def form_data():
    class FakeData:
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        marital_status = choice(['single', 'married', 'divorced'])
        hobby = sample(['dance', 'reading', 'cricket'], k=randrange(0, 3))
        phone = fake.basic_phone_number()
        email = fake.email()
        about = fake.text()
    return FakeData()
