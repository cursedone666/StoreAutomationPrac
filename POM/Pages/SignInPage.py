from selenium import webdriver
from selenium.webdriver.common.by import By

class SignInPage():

    def __init__(self, driver):
        self.driver = driver
        # by ID
        self.email_filed_reg = "email_create"

        self.email_address_enter_field = "email"

        self.password_field = "passwd"
        # Link_Text
        self.forgot_password_btn = "Forgot your password?"
        # Xpath
        self.sign_in_btn = "//button[@id='SubmitLogin']/span"

        self.create_account_btn = "//button[@id='SubmitCreate']/span"

        self.sign_in_button = "//header[@id='header']/div[2]/div/div/nav/div/a"

    def create_acc(self, email):
        signInBtn = self.driver.find_element(By.XPATH, self.sign_in_button)
        signInBtn.click()
