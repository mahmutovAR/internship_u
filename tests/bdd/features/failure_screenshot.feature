Feature: Failure screenshot testing

    Scenario: Failed auth for Registration Page Form
        Given Registration Page Form
        When Click "SUBMIT"
        Then No error messages

    Scenario: Failed auth for Login Page Form
        Given Login Page Form
        When Log in with invalid username "user_A" password "passs" and username * "user_AB"
        Then Authentication is successful

    Scenario: Failed redirection
        Given Homepage
        When Hover over menu
        Then Successful redirection