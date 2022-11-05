import os
from selenium import webdriver


class StartBrowser:

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path=r"C:\SeleniumDrivers\chromedriver.exe")
        os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver.exe"
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
