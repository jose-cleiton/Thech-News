import time

# selenium 4
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.expected_conditions import (
#     visibility_of,
#     visibility_of_element_located,
# )
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# from requests import HTTPError, ReadTimeout


# from tech_news.database import create_news

URL_BASE = "https://blog.betrybe.com"
HEADRS = {"user-agent": "Fake user-agent"}


class Fetch:
    def __init__(self) -> None:
        URL_BASE = "https://blog.betrybe.com"

        self.locator = (By.XPATH, "/html/body")
        self._SITE_LINK = URL_BASE

        self.drive = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.drive.maximize_window()

    def open_page(self, url):
        time.sleep(1)
        self.drive.get(url)
        html_content = self.drive
        return html_content

    def close_page(self):
        self.drive.close()

    def get_title(self):
        return self.drive.title

    def fetch(self, url, wait: int = 3):
        try:
            self.open_page(url).implicitly_wait(wait)
            return self.open_page(url)
        except (NoSuchElementException, TimeoutException):
            print("Erro no fetch")
            None

    def scrape_novidades(self, html_content) -> list:
        entry_preview = html_content.find_elements(By.TAG_NAME, "article")
        link = []
        for i in entry_preview:
            link.append(i.find_element(By.TAG_NAME, "a").get_attribute("href"))

        if link:
            return link
        return []

    def scrape_next_page_link(self, html_content):

        next_page = html_content.find_element(
            By.CLASS_NAME, "next.page-numbers"
        )
        if next_page:
            return next_page.get_attribute("href")
        return None


if __name__ == "__main__":
    html = Fetch()
    html_content = html.open_page(URL_BASE)
    link_next_page = html.scrape_next_page_link(html_content)
    print(link_next_page)
    html.close_page()