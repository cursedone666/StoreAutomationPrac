import unittest
from selenium import webdriver
from POM.Pages.SignInPage import SignInPage1
from POM.Pages.Homepage import Homepage
import os


class SignInValidTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path=r"C:\SeleniumDrivers\chromedriver.exe")
        os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver.exe"
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_get_dresses(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_search_field()
        homepage.type_text("dress")
        homepage.click_search_btn()
        driver.implicitly_wait(1000)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



