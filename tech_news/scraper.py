from requests import HTTPError, ReadTimeout, get
import time
# from parsel import Selector
# from tech_news.database import create_news
# Requisito 1
URL_BASE = "https://blog.betrybe.com"
HEADRS = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(ur: str, timeout: int = 3) -> str | None:
    try:
        time.sleep(1)
        response = get(ur, headers=HEADRS, timeout=timeout)
        response.raise_for_status()
    except (HTTPError, ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito    5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
