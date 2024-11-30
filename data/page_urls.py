from os import getenv


class PageUrls:
    homepage = getenv('HOME_PAGE')
    login_page = getenv('LOGIN_PAGE')
    registration_page = getenv('REGISTRATION_PAGE')
    auth_cookies_page = getenv('AUTH_COOKIES_PAGE')


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
