from dataclasses import dataclass


@dataclass
class RegistrationData:
    first_name: str = None
    last_name: str = None
    marital_status: str = None
    hobby: list = None
    country: str = None
    date_of_birth_month: str = None
    date_of_birth_day: str = None
    date_of_birth_year: str = None
    phone: str = None
    username: str = None
    email: str = None
    picture_path: str = None
    about: str = None
    password: str = None
    confirm_password: str = password
