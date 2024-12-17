Feature: Menu redirection testing

    Scenario: Menu redirection to "Appium with Python"
        Given Homepage
        When Click on menu item "Appium"
        And Click on menu item "Appium with Python"
        Then Redirection to the "Appium with Python" page successful

    Scenario: Menu redirection to "Spring Boot"
        Given Homepage
        When Click on menu item "Spring Boot"
        Then Redirection to the "Spring Boot" page successful