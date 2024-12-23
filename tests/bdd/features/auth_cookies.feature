Feature: Auth cookies testing

    Scenario: Auth "Form 1", save cookies
        Given "Form 1" page
        When Log in "Form 1" with valid data: user dstu
        Then Auth "Form 1" is successful, save cookies into file

    Scenario: Auth "Form 1" with cookies
        Given "Form 1" page
        When Load cookies  "Form 1" from file
        Then Auth "Form 1" is successful

    Scenario: Auth "Form 2", save cookies
        Given "Form 2" page
        When Log in "Form 2" with valid data: tomsmith SuperSecretPassword!
        Then Auth "Form 2" is successful, save cookies into file

    Scenario: Auth "Form 2" with cookies
        Given "Form 2" page
        When Load cookies "Form 2" from file
        Then Auth "Form 2" is successful