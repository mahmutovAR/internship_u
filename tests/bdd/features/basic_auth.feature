Feature: Basic Auth testing

    Scenario: Basic Auth
        Given Basic Auth page
        When Click "Display Image"
        And Log in with valid username "httpwatch" and password "httpwatch"
        Then Authentication is successful