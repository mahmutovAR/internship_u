Feature: Registration Form testing

    Scenario: Registration Form log in
        Given Registration Form page
        When Fill first name: Richard
        And Fill last name: Williams
        And Select marital status: single
        And Select hobby: dance,cricket
        And Select country: India
        And Select birth month: 1
        And Select birth day: 1
        And Select birth year: 2014
        And Fill phone: 99658743545
        And Fill username: rdwill
        And Fill email: rv-will@example.com
        And Choose picture: ebersteiger.jpg
        And Fill about: Sint velit eveniet. Rerum atque repellat voluptatem quia rerum.Numquam excepturi.
        And Fill password: sgy67-FVC2q3
        And Confirm password: sgy67-FVC2q3
        And Submit data
        Then No error found