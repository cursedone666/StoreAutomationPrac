from selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):

        self.driver = driver
        # by id
        self.search_field = "search_query_top"
        # by XPATH
        self.search_button = "//button[@name='submit_search']"
        # by XPATH
        self.sign_in_button = "//header[@id='header']/div[2]/div/div/nav/div/a"
        # by XPATH
        self.contact_us_button = "//div[2]/a"

        self.women_button = "//a[contains(text(),'Women')]"

        self.dresses_button = "(//a[contains(text(),'Dresses')])[5]"

        self.t_shirts_button = "(//a[contains(text(),'T-shirts')])[2]"

        self.best_sellers_button = "//a[contains(text(),'Best Sellers')]"

        self.popular_button = "//a[contains(text(),'Popular')]"

        self.counter_element = "Contact us"

    def click_on_search_field(self):
        self.driver.find_element(By.ID, self.search_field).click()

    def type_text(self, text):
        self.driver.find_element(By.ID, self.search_field).send_keys(text)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH, self.search_button).click()

    def find_summer_dress(self):
        test = self.driver.find_element(By.LINK_TEXT, self.counter_element)
        return test.text