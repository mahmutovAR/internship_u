Feature: Alerts text testing

    Scenario: Alerts
        Given Alerts page
        When Click "Input Alert"
        And click button to activate "Input box"
        And enter text "Alex John Smith"
        Then Entered text is displayed