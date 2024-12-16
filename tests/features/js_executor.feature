Feature: Java Script testing

    Scenario: Remove focus from input field
        Given Form page
        And click "First Name" field
        When Remove focus from input field by using JavaScriptExecutor
        Then Focus removed from input field

    Scenario: Check if page has scroll
        Given Form page
        Then Use JavaScriptExecutor to assert page scroll