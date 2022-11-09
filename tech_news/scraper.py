import time

from requests import HTTPError, ReadTimeout, get

# Requisito 1
URL_BASE = "https://blog.betrybe.com"


def fetch(ur, timeout: int = 3):
    try:
        time.sleep(1)
        response = get(ur, headers={"User-Agent": "Chrome"}, timeout=timeout)
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
