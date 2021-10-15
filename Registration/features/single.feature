Feature: As a candidate for Etherscan Tester
  I want to test
  the registration form
  using cucumber and python


Background:
  Given I am on registration page


# This test case cannot be implemented due to captcha
#  Scenario: Register with Valid credentials
#    Given I am on registration page
#     When I input valid credentials
#      And I click on Create Account button
#     Then I should see email verification message

  Scenario: Register with shorter userName than require
     When I input username with length less than 5 alphanumeric characters
     Then I should see userName error message


  Scenario: Register with longer userName than required
     When I input username with length more than 30 alphanumeric characters
     Then I should see userName error message

  Scenario: Register with special characters in userName
     When I input username of valid length and containing special characters
     Then I should see userName error message

# This test cannot be automated due to captcha

#  Scenario: Register with already signed email
#     When I input email address already registered  to the portal
#      And I enter valid inputs to other fields
#      And I click on Create Account button
#     Then I should see error message


  Scenario: Register with inavlid email
     When I input invalid email
     Then I should see email error message

  Scenario: Register with shorter password than required
     When I input password shorter than 5 characters
     Then I should see password error message

  Scenario: Register with different Passwords in "Password" and "Confirm Password" Field
     When I input valid password in "Password" field
      And I input different valid password in "Confirm Password" field
     Then I should see different password error message

  Scenario: Register without accepting terms and conditions
    Given Terms and conditions is unchecked
     When I click on "Create Account" button without accepting terms and conditions
     Then I should terms and conditions see error message







