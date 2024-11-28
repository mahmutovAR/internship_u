from faker import Faker


class BaseGenerator:
    def __init__(self):
        self.fake = Faker()
        self.birthday = self.fake.date_of_birth(minimum_age=18, maximum_age=65)

    def generate_first_name(self, first_name: str) -> str:
        if first_name is None:
            return self.fake.first_name()
        return first_name

    def generate_last_name(self, last_name: str) -> str:
        if last_name is None:
            return self.fake.last_name()
        return last_name

    def generate_country(self, country: str) -> str:
        if country is None:
            return self.fake.country()
        return country

    def generate_date_of_birth_month(self, date_of_birth_month: str | int) -> str:
        if date_of_birth_month is None:
            return str(self.birthday.month)
        return str(date_of_birth_month)

    def generate_date_of_birth_day(self, date_of_birth_day: str | int) -> str:
        if date_of_birth_day is None:
            return str(self.birthday.day)
        return str(date_of_birth_day)

    def generate_date_of_birth_year(self, date_of_birth_year: str | int) -> str:
        if date_of_birth_year is None:
            return str(self.birthday.year)
        return str(date_of_birth_year)

    def generate_phone(self, phone: str) -> str:
        if phone is None:
            return self.fake.basic_phone_number()
        return phone

    def generate_username(self, username: str) -> str:
        if username is None:
            return self.fake.user_name()
        return username

    def generate_email(self, email: str) -> str:
        if email is None:
            return self.fake.email()
        return email

    def generate_about(self, about: str) -> str:
        if about is None:
            return self.fake.text()
        return about

    def generate_password(self, password: str) -> str:
        if password is None:
            return self.fake.password()
        return password
