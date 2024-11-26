from os import getenv


class URL:
    homepage = 'https://www.way2automation.com/'
    login_page = 'https://www.way2automation.com/angularjs-protractor/registeration/#/login'
    registration_page = 'https://www.way2automation.com/way2auto_jquery/registration.php#load_box'


class MenuUrls:
    all_urls = [getenv('MENU_HOME'), getenv('MENU_ALL_COURSES'), getenv('MENU_VIDEO_TUTORIAL'),
                getenv('MENU_RESOURCES'), getenv('MENU_CAREERS'), getenv('MENU_LIFETIME_MEMBERSHIP'),
                getenv('MENU_BLOG'), getenv('MENU_FORUM'), getenv('MENU_MEMBER_LOGIN')]
    appium_python = getenv('MENU_ALL_COURSES_APPIUM_PYTHON')
    spring_boot = getenv('MENU_VIDEO_TUTORIAL_SPRING')
