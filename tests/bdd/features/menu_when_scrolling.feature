Feature: Menu when scrolling testing

    Scenario: Home page
        Given Homepage
        When Scroll to Footer
        Then All Menu items are present and clickable
