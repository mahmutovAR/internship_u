import pickle
from os import getcwd, remove
from os.path import isfile
from os.path import join as os_path_join


class CookieHelper:
    def __init__(self):
        self.file_path = os_path_join(getcwd(), 'cookies.pkl')

    def save_cookies_to_file(self, cookies: list) -> None:
        """Saves cookies to file."""
        with open(self.file_path, "wb") as file:
            pickle.dump(cookies, file)

    def load_cookies_from_file(self) -> list:
        """Loads cookies from file."""
        with open(self.file_path, "rb") as file:
            cookies = pickle.load(file)
        return cookies

    def remove_cookies_file(self) -> None:
        """Deletes cookies file."""
        remove(self.file_path)

    def file_exists(self) -> bool:
        """Checks if cookies file exists."""
        return isfile(self.file_path)


cookie_helper = CookieHelper()
