import time

from requests import HTTPError, ReadTimeout, get

# from parsel import Selector
# from tech_news.database import create_news
# Requisito 1
URL_BASE = "https://blog.betrybe.com"
HEADRS = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url: str, timeout: int = 3) -> str | None:
    try:
        time.sleep(1)
        response = get(url, headers=HEADRS, timeout=timeout)
        response.raise_for_status()
    except (HTTPError, ReadTimeout):
        return None
    else:
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
