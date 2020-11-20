from selenium.common.exceptions import TimeoutException


from time import sleep


class LinkedinJobs:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.boxes = self.wait.until(
            lambda driver: self.driver.find_elements_by_class_name(
                "jobs-search-box__text-input"
            )
        )
        self.message_toggle = driver.find_element_by_class_name(
            "msg-overlay-bubble-header__button.truncate.ml2"
        )
        self.search_field = self.boxes[0]
        self.location = self.boxes[-2]
        self.search_button = self.driver.find_element_by_class_name(
            "jobs-search-box__submit-button"
        )

        self.jobs = self.driver.find_elements_by_class_name(
            "job-card-container__metadata-wrapper"
        )

    def search(self, search_text: str, location=None):
        self.message_toggle.click()
        icons = self.driver.find_elements_by_class_name("jobs-search-box__input-icon")
        icons[0].click()
        self.search_field.clear()
        self.search_field.send_keys(search_text)
        icons[-1].click()
        self.location.clear()
        self.location.send_keys(location)
        self.search_button.click()

        self.jobs = self.wait.until(
            lambda driver: self.driver.find_element_by_class_name(
                "jobs-search-results__list.list-style-none"
            )
        )

        self.jobs = self.jobs.find_elements_by_tag_name('li')

    def apply(self):
        sleep(2)
        self.__init__(self.driver, self.wait)
        for job in self.jobs:
            # TODO: Resolver problema do click em vagas
            import ipdb;ipdb.sset_trace()
            job.click()
            try:
                apply_button = self.wait.until(
                    lambda driver: driver.find_element_by_class_name(
                        "jobs-apply-button"
                    )
                )
            except TimeoutException as e:
                continue
            
            if apply_button.text == "Easy Apply":
                apply_button.click()

                submit_application = self.wait.until(
                    lambda driver: self.driver.find_elements_by_class_name(
                        "artdeco-button"
                    )[3]
                )

                submit_application.click()

                close_button = self.driver.find_element_by_class_name(
                    "artdeco-button"
                 )

                close_button.click()
