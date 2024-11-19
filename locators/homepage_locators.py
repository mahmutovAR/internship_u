from selenium.webdriver.common.by import By


class MainElementsLocators:
    header = (By.ID, 'masthead')
    block_1 = (By.XPATH, '//div[contains(@class, "ast-primary-header-bar ast-primary-header main-header-bar site-header-focus-item")]')
    block_2 = (By.XPATH, '//div[contains(@class, "elementor-widget-wrap elementor-element-populated")]')
    block_3 = (By.XPATH, '//div[contains(@class, "elementor-container elementor-column-gap-default")]')
    live_trainings = (By.XPATH, '//div[h3="Manual and automation live trainings"]')
    footer = (By.XPATH, '//div[@data-elementor-type="footer"]')


class HeaderLocators:
    phone_number_1 = (By.XPATH, '//a[@href="https://wa.me/+919711111558"]')
    phone_number_2 = (By.XPATH, '//a[@href="https://wa.me/+919711191558"]')
    phone_number_3 = (By.XPATH, '//a[@href="tel:+16464800603"]')
    skype = (By.XPATH, '//a[@href="skype:seleniumcoaching?chat"]')
    email = (By.XPATH, '//a[@href="mailto:trainer@way2automation.com"]')
    facebook = (By.XPATH, '//a[@href="https://www.facebook.com/way2automation"]')
    linkedin = (By.XPATH, '//a[@href="https://in.linkedin.com/in/rahul-arora-0490b751"]')
    plus_google = (By.XPATH, '//a[@href="https://plus.google.com/u/0/+RamanAhujatheseleniumguru"]')
    youtube = (By.XPATH, '//a[@href="https://www.youtube.com/c/seleniumappiumtutorialtraining"]')


class MenuLocators:
    home = (By.XPATH, '//a[@href="https://www.way2automation.com/"]')
    all_courses = (By.ID, "menu-item-27580")
    video_tutorial = (By.ID, "menu-item-27597")
    resources = (By.ID, "menu-item-27617")
    careers = (By.ID, "menu-item-27621")
    lifetime_membership = (By.ID, "menu-item-27622")
    blog = (By.ID, "menu-item-27623")
    forum = (By.ID, "menu-item-27624")
    member_login = (By.ID, "menu-item-27625")


class MenuRedirectLocators:
    all_courses_appium = (By.ID, "menu-item-27585")
    all_courses_appium_python = (By.XPATH, '//a[@href="https://www.way2automation.com/python/training/appium-python-training/"]')
    video_tutorial_spring = (By.XPATH, '//a[@href="https://www.selenium-tutorial.com/p/spring-boot-with-complete-bootcamp"]')
    resources_site_1 = (By.XPATH, '//a[@href="https://www.way2automation.com/way2auto_jquery/index.php"]')
    resources_blog = (By.XPATH, '//a[@href="https://www.selenium-tutorial.com/blog/"]')


class CertificationLocators:
    lifetime_membership = (By.XPATH, '//h3[span=" Lifetime Membership "]')
    online_training = (By.XPATH, '//h3[span=" Online Training "]')
    video_tutorials = (By.XPATH, '//div[contains(h3, "Video Tutorials")]')
    corporate_training = (By.XPATH, '//h3[span=" Corporate Training "]')


class PopularCoursesLocators:
    main = (By.XPATH, '//div[@data-id="c50f9f0"]')
    slide = (By.XPATH, '//div[contains(h4, "Selenium Web Driver with Java (Basics + Advance + Architect)")]')
    prev_slide = (By.XPATH, '//div[contains(@class, "pp-slider-arrow") and contains(@aria-label, "Previous slide")]')
    next_slide = (By.XPATH, '//div[contains(@class, "pp-slider-arrow") and contains(@aria-label, "Next slide")]')


class FooterLocators:
    main = (By.XPATH, '//div[@data-elementor-type="footer"]')
    about_us = (By.XPATH, '//div[h4="ABOUT US "]')
    address = (By.XPATH, '//li[contains(string(), "CDR Complex, 3rd Floor, Naya Bans Market")]')
    phone_1 = (By.XPATH, '//a[@href="tel:9711111558"]')
    phone_2 = (By.XPATH, '//a[@href="tel:9711191558"]')
    email_1 = (By.XPATH, '//a[@href="mailto:trainer@way2automation.com"]')
    email_2 = (By.XPATH, '//a[@href="mailto:seleniumcoaching@gmail.com"]')
    info = (By.XPATH, '//div[contains(string(), "Worked with various CMM level orgranizations")]')
