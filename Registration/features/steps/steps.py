import behave
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def before_scenario(context):
 context.browser.get("https://etherscan.io/register")

@Given("I am on registration page")
def before_scenario(context):
 context.browser.get("https://etherscan.io/register")


@given('Terms and conditions is unchecked')
def step(context):
 terms_conditions = context.browser.find_element_by_id('ContentPlaceHolder1_MyCheckBox')
 checked = terms_conditions.is_selected()
 assert  checked == False


#cannot be automated due to captcha
# @when('I input valid credentials')
# def step(context):
#  userName = context.browser.find_element_by_id('ContentPlaceHolder1_txtUserName')
#  userName.send_keys("DummyUser999")
#  email_input = context.browser.find_element_by_id('ContentPlaceHolder1_txtEmail')
#  email_input.send_keys('dummy.user999@gmail.com')
#  password = context.browser.find_element_by_id('ContentPlaceHolder1_txtPassword')
#  password.send_keys("Abc123!")
#  confirm_password = context.browser.find_element_by_id('ContentPlaceHolder1_txtPassword2')
#  confirm_password.send_keys("Abc123!")
#  terms_conditions = context.browser.find_element_by_id('ContentPlaceHolder1_MyCheckBox')
#  checked = terms_conditions.get_attribute('checked')
#  if checked != True:
#   terms_conditions.click()
#  # re captcha automation not possible
#  btn_create = context.browser.find_element_by_id('ContentPlaceHolder1_btnRegister')
#  btn_create.click()


@When('I input username with length less than 5 alphanumeric characters')
def step(context):
 userName = context.browser.find_element_by_id('ContentPlaceHolder1_txtUserName')
 userName.send_keys("abcd")


@When('I input username with length more than 30 alphanumeric characters')
def step(context):
 userName = context.browser.find_element_by_id('ContentPlaceHolder1_txtUserName')
 userName.send_keys('abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde')


@When('I input username of valid length and containing special characters')
def step(context):
 userName = context.browser.find_element_by_id('ContentPlaceHolder1_txtUserName')
 userName.send_keys('Iqra_Jilani')


@When('I input invalid email')
def step(context):
 email_input = context.browser.find_element_by_id('ContentPlaceHolder1_txtEmail')
 email_input.send_keys('abcd.com')


# Cannot be automated due to captcha
# @when('I input email address already registered  to the portal')
# def step(context):
#  userName = context.browser.find_element_by_id('ContentPlaceHolder1_txtUserName')
#  userName.send_keys("DummyUser999")
#  email_input = context.browser.find_element_by_id('ContentPlaceHolder1_txtEmail')
#  email_input.send_keys('dummy.user999@gmail.com')
#  password = context.browser.find_element_by_id('ContentPlaceHolder1_txtPassword')
#  password.send_keys("Abc123!")
#  confirm_password = context.browser.find_element_by_id('ContentPlaceHolder1_txtPassword2')
#  confirm_password.send_keys("Abc123!")
#  terms_conditions = context.browser.find_element_by_id('ContentPlaceHolder1_MyCheckBox')
#  checked = terms_conditions.get_attribute('checked')
#  if checked != True:
#   terms_conditions.click()
#   # re captcha automation not possible
#  btn_create = context.browser.find_element_by_id('ContentPlaceHolder1_btnRegister')
#  btn_create.click()


@When('I input password shorter than 5 characters')
def step(context):
 password = context.browser.find_element_by_id('ContentPlaceHolder1_txtPassword')
 password.send_keys('Abcd')


@When('I input valid password in "Password" field')
def step(context):
 password = context.browser.find_element_by_id('ContentPlaceHolder1_txtPassword')
 password.send_keys("Abc123!")

@When('I input different valid password in "Confirm Password" field')
def step(context):
 confirm_password = context.browser.find_element_by_id('ContentPlaceHolder1_txtPassword2')
 confirm_password.send_keys("Abc1234!")



@When('I click on "Create Account" button without accepting terms and conditions')
def step(context):
 btn_create = context.browser.find_element_by_id('ContentPlaceHolder1_btnRegister')
 btn_create.submit()



@Then("I should see userName error message")
def step(context):
 error_message = "Username is invalid."
 WebDriverWait(context.browser, 10).until(
  EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "'+error_message+'")]'))
 )


@Then("I should see email error message")
def step(context):
 error_message = "Please enter a valid email address."
 WebDriverWait(context.browser, 10).until(
  EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "' + error_message + '")]'))
 )


@Then("I should see password error message")
def step(context):
 error_message = "Your password must be at least 5 characters long."
 WebDriverWait(context.browser, 10).until(
  EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "' + error_message + '")]'))
 )


@Then("I should see different password error message")
def step(context):
 error_message = "Password does not match, please check again."
 WebDriverWait(context.browser, 10).until(
  EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "' + error_message + '")]'))
 )


@Then("I should terms and conditions see error message")
def step(context):
 error_message = "Please accept our Terms and Conditions."
 WebDriverWait(context.browser, 10).until(
  EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "' + error_message + '")]'))
 )