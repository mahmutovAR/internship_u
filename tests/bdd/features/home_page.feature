Feature: Homepage testing

    Scenario: Home page
        Given Homepage
        Then Title is "Get Online Selenium Certification Course | Way2Automation"
        And the main page elements are active

    Scenario: Header
        Given Homepage
        Then Header link are clickable
        And data is correct

    Scenario: Certification Block
        Given Homepage
        Then Certification Block link are clickable,
        And data is correct

    Scenario: Courses Block
        Given Homepage
        When Scroll to Courses Block
        Then Courses Block navigation buttons are active