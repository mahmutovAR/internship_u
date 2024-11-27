from os import getenv


class HeaderData:
    phone_1 = getenv('HEADER_PHONE_NUMBER_1')
    phone_2 = getenv('HEADER_PHONE_NUMBER_2')
    phone_3 = getenv('HEADER_PHONE_NUMBER_3')
    skype = getenv('HEADER_SKYPE')
    email = getenv('HEADER_EMAIL')
    all_items = [phone_1, phone_2, phone_3, skype, email]


class LoginData:
    username = getenv('LOGIN_USERNAME')
    password = getenv('LOGIN_PASSWORD')
