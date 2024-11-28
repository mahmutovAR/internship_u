from selenium.webdriver.common.by import By


class UniqueElementsLocators:
    link_about_us = (By.XPATH, '//a[@href="https://www.way2automation.com/about-us/"]')
    link_view_all_images = (By.XPATH, '//a[@href="https://www.way2automation.com/about-us/#gallery"]')


class HeaderLocators:
    phone_1 = (By.XPATH, '//a[@href="https://wa.me/+919711111558"]')
    phone_2 = (By.XPATH, '//a[@href="https://wa.me/+919711191558"]')
    phone_3 = (By.XPATH, '//a[@href="tel:+16464800603"]')
    skype = (By.XPATH, '//a[@href="skype:seleniumcoaching?chat"]')
    email = (By.XPATH, '//a[@href="mailto:trainer@way2automation.com"]')
    facebook = (By.XPATH, '//a[@href="https://www.facebook.com/way2automation"]')
    linkedin = (By.XPATH, '//a[@href="https://in.linkedin.com/in/rahul-arora-0490b751"]')
    plus_google = (By.XPATH, '//a[@href="https://plus.google.com/u/0/+RamanAhujatheseleniumguru"]')
    youtube = (By.XPATH, '//a[@href="https://www.youtube.com/c/seleniumappiumtutorialtraining"]')
    all_items = [phone_1, phone_2, phone_3, skype, email,
                 facebook, linkedin, plus_google, youtube]
    contacts = [phone_1, phone_2, phone_3, skype, email]


class MenuLocators:
    footer = (By.XPATH, '//div[@data-elementor-type="footer"]')
    main = (By.XPATH, '//div[@class="main-navigation ast-inline-flex"]')
    home = (By.XPATH, '//a[@href="https://www.way2automation.com/"]')
    all_courses = (By.ID, "menu-item-27580")
    video_tutorial = (By.ID, "menu-item-27597")
    resources = (By.ID, "menu-item-27617")
    careers = (By.ID, "menu-item-27621")
    lifetime_membership = (By.ID, "menu-item-27622")
    blog = (By.ID, "menu-item-27623")
    forum = (By.ID, "menu-item-27624")
    member_login = (By.ID, "menu-item-27625")
    all_items = [home, all_courses, video_tutorial, resources, careers, lifetime_membership, blog, forum, member_login]


class MenuRedirectLocators:
    all_courses_appium = (By.ID, "menu-item-27585")
    all_courses_appium_python = (By.ID, 'menu-item-27587')
    appium_python_link_1 = (By.XPATH, '//a[@href="https://www.way2automation.com/buynow-lifetime/"]')
    appium_python_link_2 = (By.XPATH, '//a[@href="https://www.selenium-tutorial.com/p/selenium-webdriver-with-python-and-robot-framework"]')
    video_tutorial_spring = (By.ID, 'menu-item-27615')
    spring_boot_link = (By.ID, "enroll-button-top")
    spring_boot_text_1 = (By.XPATH, '//div[@class="faq-question"]')
    spring_boot_text_2 = (By.XPATH, '//div[@class="checkout-cta"]')


class CertificationLocators:
    lifetime_membership = (By.XPATH, '//div[@data-id="94bce2e"]')
    lifetime_membership_button = (By.XPATH, '//div[@data-id="72a13c4"]')

    online_training = (By.XPATH, '//div[@data-id="442c7c2"]')
    online_training_button = (By.XPATH, '//div[@data-id="513609a"]')

    video_tutorials = (By.XPATH, '//div[@data-id="a4dfd3d"]')
    video_tutorials_button = (By.XPATH, '//div[@data-id="05f99df"]')

    corporate_training = (By.XPATH, '//div[@data-id="ee9b1e1"]')
    corporate_training_button = (By.XPATH, '//div[@data-id="03c01c9"]')


class PopularCoursesLocators:
    main = (By.XPATH, '//div[@data-id="c50f9f0"]')
    slide = (By.XPATH, '//div[contains(h4, "Selenium Web Driver with Java (Basics + Advance + Architect)")]')
    prev_slide = (By.XPATH, '//div[@class="pp-slider-arrow swiper-button-prev swiper-button-prev-c50f9f0"]')
    next_slide = (By.XPATH, '//div[@class="pp-slider-arrow swiper-button-next swiper-button-next-c50f9f0"]')
