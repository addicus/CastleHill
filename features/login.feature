Feature: User authentication


Scenario: User authenticates
      Given User is on login screen
      When user enters correct credentials
      Then user should be authenticated

Scenario: User submits blank authentication form
      Given User is on login screen
      When user enters blank credentials
      Then user should not be authenticated

Scenario: User fails authentication
      Given User is on login screen
      When user enters incorrect credentials
      Then user should not be authenticated


Scenario: 1 Successful Login
      Given I am on the Sauce Demo Login Page
      When I fill the account information for account StandardUser into the Username field and the Password field
      And I click the Login Button
      Then I am redirected to the Sauce Demo Main Page
      And I verify the App Logo exists

Scenario: 2 Failed Login
      Given I am on the Sauce Demo Login Page
      When I fill the account information for account LockedOutUser into the Username field and the Password field
      And I click the Login Button
      Then I verify the Error Message contains the text "Epic sadface: Sorry, this user has been locked out."
