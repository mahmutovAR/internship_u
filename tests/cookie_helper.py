import json
from os import getcwd, remove
from os.path import isfile
from os.path import join as os_path_join


class CookieHelper:
    def __init__(self):
        self.file_path = os_path_join(getcwd(), 'tests', 'cookies.json')

    def save_cookies_to_file(self, cookies: list) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(cookies, file)

    def load_cookies_from_file(self) -> list:
        with open(self.file_path, 'r') as file:
            cookies = json.load(file)
        return cookies

    def delete_cookies_file(self) -> None:
        remove(self.file_path)

    def file_exists(self) -> bool:
        return isfile(self.file_path)
