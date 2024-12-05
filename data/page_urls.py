from os import getenv

from dotenv import load_dotenv


load_dotenv()


class PageUrls:
    homepage = getenv('HOME_PAGE')
    login_page = getenv('LOGIN_PAGE')
    registration_page = getenv('REGISTRATION_PAGE')

    auth_cookies_page = getenv('AUTH_COOKIES_PAGE')
    alt_auth_cookies_page = getenv('ALT_AUTH_COOKIES_PAGE')
    alt_auth_cookies_logged_page = getenv('ALT_AUTH_COOKIES_LOGGED_PAGE')

    drag_and_drop_page = getenv('DRAG_AND_DROP_PAGE')
    tabs_page = getenv('TABS_PAGE')
    alerts_page = getenv('ALERTS_PAGE')
    basic_auth_page = getenv('BASIC_AUTH_PAGE')
    # homepage = "https://www.way2automation.com/"
    # login_page = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"
    # registration_page = "https://www.way2automation.com/way2auto_jquery/registration.php#load_box"
    # auth_cookies_page = "https://www.sql-ex.ru/"
    # drag_and_drop_page = "https://way2automation.com/way2auto_jquery/droppable.php#load_box"
    # tabs_page = "https://way2automation.com/way2auto_jquery/frames-and-windows.php#load_box"
    # alerts_page = "http://way2automation.com/way2auto_jquery/alert.php"
    # basic_auth_page = "https://www.httpwatch.com/httpgallery/authentication/#showExample10"
    # alt_auth_cookies_page = "https://the-internet.herokuapp.com/login"
    # alt_auth_cookies_logged_page = "https://the-internet.herokuapp.com/secure"


class MenuUrls:
    all_urls = [getenv('HOME_PAGE'), getenv('MENU_ALL_COURSES'), getenv('MENU_VIDEO_TUTORIAL'),
                getenv('MENU_RESOURCES'), getenv('MENU_CAREERS'), getenv('MENU_LIFETIME_MEMBERSHIP'),
                getenv('MENU_BLOG'), getenv('MENU_FORUM'), getenv('MENU_MEMBER_LOGIN')]
    appium_python = getenv('MENU_ALL_COURSES_APPIUM_PYTHON')
    spring_boot = getenv('MENU_VIDEO_TUTORIAL_SPRING')
    lifetime_membership = getenv('MENU_LIFETIME_MEMBERSHIP')
    online_training = getenv('MENU_ONLINE_TRAINING')
    video_tutorials = getenv('MENU_VIDEO_TUTORIAL')
    corporate_training = getenv('MENU_CORPORATE_TRAINING')
