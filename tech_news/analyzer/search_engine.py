from datetime import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title: str) -> list:
    query = {"title": {"$regex": title, "$options": "i"}}
    list = search_news(query)
    result = [(news["title"], news["url"]) for news in list]
    return result


# Requisito 7
# Requisito 7
def search_by_date(date: str) -> list:
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        query = {"timestamp": date}
        list = search_news(query)
        result = [(news["title"], news["url"]) for news in list]
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    list = search_news(query)
    result = [(news["title"], news["url"]) for news in list]
    return result


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    list = search_news(query)
    result = [(news["title"], news["url"]) for news in list]
    return result