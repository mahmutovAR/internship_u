from os import getenv

from dotenv import load_dotenv


load_dotenv()


class HeaderData:
    phone_1 = getenv('HEADER_PHONE_1')
    phone_2 = getenv('HEADER_PHONE_2')
    phone_3 = getenv('HEADER_PHONE_3')
    skype = getenv('HEADER_SKYPE')
    email = getenv('HEADER_EMAIL')
    all_items = [phone_1, phone_2, phone_3, skype, email]


class LoginData:
    username = getenv('LOGIN_USERNAME')
    password = getenv('LOGIN_PASSWORD')


class AltAuthCookiesData:
    username = getenv('ALT_AUTH_COOKIES_USERNAME')
    password = getenv('ALT_AUTH_COOKIES_PASSWORD')


class BasicAuthData:
    username = getenv('BASIC_AUTH_USERNAME')
    password = getenv('BASIC_AUTH_PASSWORD')
