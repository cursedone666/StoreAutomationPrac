from selenium.webdriver.common.by import By


class ContactUs:

    def __init__(self, driver):
        self.driver = driver

        self.subj_heading_list = "//select[@id='id_contact']"

        self.email_address_fld = "//input[@id='email']"

        self.order_reference_fld = "//input[@id='id_order']"

        self.attach_file_btn = "//input[@id='fileUpload']"

        self.message_field = "//textarea[@id='message']"

        self.send_btn = "//button[@id='submitMessage']/span"

    def enter_email(self, email):
        e_field = self.driver.find_element(By.XPATH, self.email_address_fld)
        e_field.click()
        e_field.send_keys(email)

    def enter_order_reference(self, order_ref):
        order = self.driver.find_element(By.XPATH, self.order_reference_fld)
        order.click()
        order.send_keys(order_ref)

    def enter_message(self, message):
        msg = self.driver.find_element(By.XPATH, self.message_field)
        msg.click()
        msg.send_keys(message)

    # test file
    def attach_file(self, file_path):
        send_file = self.driver.find_element(By.XPATH, self.attach_file_btn)
        send_file.send_keys(file_path)

