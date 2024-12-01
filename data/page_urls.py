from os import getenv


class PageUrls:
    # homepage = getenv('HOME_PAGE')
    # login_page = getenv('LOGIN_PAGE')
    # registration_page = getenv('REGISTRATION_PAGE')
    # auth_cookies_page = getenv('AUTH_COOKIES_PAGE')
    # drag_and_drop_page = getenv('DRAG_AND_DROP_PAGE')
    homepage = "https://www.way2automation.com/"
    login_page = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"
    registration_page = "https://www.way2automation.com/way2auto_jquery/registration.php#load_box"
    auth_cookies_page = "https://www.sql-ex.ru/"
    drag_and_drop_page = "https://way2automation.com/way2auto_jquery/droppable.php#load_box"


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
