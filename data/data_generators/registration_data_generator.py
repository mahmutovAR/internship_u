from data.data_classes import RegistrationData
from . import BaseGenerator


class RegistrationDataGenerator(BaseGenerator):
    def generate_registration_data(self, first_name: str = None, last_name: str = None,
                                   marital_status: str = None, hobby: list = None, country: str = None,
                                   date_of_birth_month: str = None, date_of_birth_day: str = None,
                                   date_of_birth_year: str = None, phone: str = None,
                                   username: str = None, email: str = None, picture_path: str = None,
                                   about: str = None, password: str = None, confirm_password: str = None):

        yield RegistrationData(first_name=self.generate_first_name(first_name),
                               last_name=self.generate_last_name(last_name),
                               marital_status=marital_status,
                               hobby=hobby,
                               country=self.generate_country(country),
                               date_of_birth_month=self.generate_date_of_birth_month(date_of_birth_month),
                               date_of_birth_day=self.generate_date_of_birth_day(date_of_birth_day),
                               date_of_birth_year=self.generate_date_of_birth_year(date_of_birth_year),
                               phone=self.generate_phone(phone),
                               username=self.generate_username(username),
                               email=self.generate_email(email),
                               picture_path=picture_path,
                               about=self.generate_about(about),
                               password=self.generate_password(password),
                               confirm_password=self.generate_password(confirm_password))
