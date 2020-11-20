from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

from helpers.helper import to_jobs_page, find_and_apply


if __name__ == "__main__":
    driver = Chrome()
    wait = WebDriverWait(driver, 10)
    to_jobs_page(driver, wait)
    find_and_apply(driver, wait, "Estagiário", "Campinas")
