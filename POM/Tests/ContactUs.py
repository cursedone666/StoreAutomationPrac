import time
import unittest
from selenium import webdriver
from StoreAutomationPrac.POM.Pages.SignInPage import SignInPage
from StoreAutomationPrac.POM.Pages.Homepage import Homepage
from StoreAutomationPrac.POM.Pages.ContactUsPage import ContactUs
import os


class ContactUsCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.environ['PATH'] += r"StoreAutomationPrac/drivers"
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_send_form_valid(self):
        driver = self.driver
        driver.implicitly_wait(1000)
        homepage = Homepage(driver)
        contact_us = ContactUs(driver)
        homepage.click_contact_us_btn()
        contact_us.enter_email("test@email.com")
        contact_us.enter_order_reference("WHAAAT")
        contact_us.enter_message("just some text to test the field")
        contact_us.attach_file("C:/Users/Ilya/Desktop/Labs/Lab1.docx")
        time.sleep(20)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



