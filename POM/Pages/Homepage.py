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

        self.promotion_banner = "//img[contains(@src,'http://automationpractice.com/modules/blockbanner" \
                                "/img/sale70.png')]"

        self.cart_btn = "//a[@href='http://automationpractice.com/index.php?controller=order']"

        self.three_days_sale_banner = "//div[@id='htmlcontent_top']/ul/li/a/img"

        self.summer_collection_banner = "//div[@id='htmlcontent_top']/ul/li[2]/a/img"

        self.top_trends_banner = "//div[@id='htmlcontent_home']/ul/li/a/img"

        self.mens_coats_banner = "//div[@id='htmlcontent_home']/ul/li[2]/a/img"

        self.women_coats_banner = "//div[@id='htmlcontent_home']/ul/li[3]/a/img"

        self.sunglasses_banner = "//div[@id='htmlcontent_home']/ul/li[4]/a/img"

        self.handbags_banner = "//div[@id='htmlcontent_home']/ul/li[5]/a/img"



    def click_on_search_field(self):
        self.driver.find_element(By.ID, self.search_field).click()

    def type_text(self, text):
        self.driver.find_element(By.ID, self.search_field).send_keys(text)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH, self.search_button).click()

    def click_contact_us_btn(self):
        self.driver.find_element(By.XPATH, self.contact_us_button).click()

    def find_summer_dress(self):
        test = self.driver.find_element(By.LINK_TEXT, self.contact_us_button)
        return test.text