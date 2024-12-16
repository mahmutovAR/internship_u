Feature: Login Page testing

    Scenario: Login page
        Given Login page
        Then "Username" "Password" "Username *" fields are present, labels are correct

    Scenario: Empty Form submitting
        Given Login page
        When Click all fields without entering data
        Then Error messages are displayed and "Login" button is not clickable

    Scenario: Log in with valid data
        Given Login page
        When Log in with valid data: "angular" "password" "user_AB"
        Then Authentication is successful

    Scenario Outline: Log in with invalid data
        Given Login page
        When Log in with invalid data: <username> <password> <username_desc>
        Then Error message is displayed
        Examples:
            | username | password | username_desc |
            | user_A   | psswwrd  | username-C    |
            | angular  | psswwrd  | username_ABC  |
            | user_A   | password | user_AB       |

    Scenario Outline: Log in with invalid data with error message checking
        Given Login page
        When Log in with incorrect data: <username> <password> <username_desc>
        Then Corresponding error message is displayed: <username_error> <password_error> <username_desc_error>
        Examples:
            | username | password | username_desc | username_error | password_error | username_desc_error |
            | ab       | abcdefg  | abcdefg       | True           | False          | False               |
            | abcdefg  | ab       | abcdefg       | False          | True           | False               |
            | abcdefg  | abcdefg  | ab            | False          | False          | True                |
            | abcdefg  | ab       | ab            | False          | True           | True                |
            | ab       | abcdefg  | ab            | True           | False          | True                |
            | ab       | ab       | abcdefg       | True           | True           | False               |
            | ab       | ab       | ab            | True           | True           | True                |

    Scenario: Log in with valid data and log out
        Given Login page
        When Log in with valid data: "angular" "password" "user_AB"
        And log out
        Then Login page is displayed