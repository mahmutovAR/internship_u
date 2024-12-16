Feature: Tabs testing

    Scenario: Tabs page opening
        Given Tabs page
        When Click link
        Then New tab opened
        When Click second link
        Then Three tabs are opened