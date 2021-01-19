from decouple import config

from pages import LinkedinJobs, Login

credentials = {
    "username": config("username"),
    "password": config("password"),
}


def to_jobs_page(driver, wait):
    """walks from linkedin initial page to jobs page """
    driver.get("https://www.linkedin.com/")
    Login(driver, wait).login(credentials["username"], credentials["password"])
    options = wait.until(
        lambda driver: driver.find_elements_by_class_name("global-nav__primary-item")
    )

    for option in options:
        if option.text == "Jobs":
            option.click()
            break


def find_and_apply(driver, wait, title, location):
    jobs = LinkedinJobs(driver, wait)
    jobs.search(title, location)
    jobs.apply()
