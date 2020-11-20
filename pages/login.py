class Login:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.email_field = self.driver.find_element_by_id("session_key")
        self.passwd = self.driver.find_element_by_id("session_password")
        self.sign_in = self.driver.find_element_by_class_name(
            "sign-in-form__submit-button"
        )

    def login(self, email: str, passwd: str):
        self.email_field.clear()
        self.email_field.send_keys(email)
        self.passwd.clear()
        self.passwd.send_keys(passwd)
        self.sign_in.click()
