from os import getenv

from dotenv import load_dotenv


load_dotenv()


class DriverPath:
    chrome = getenv('CHROME_DRIVER_PATH')
    firefox = getenv('GECKO_DRIVER_PATH')
    edge = getenv('MSEDGE_DRIVER_PATH')
