from collections import Counter

from tech_news.database import search_news


# Requisito 10
def top_5_news():
    query = {"$query": {}, "$orderby": {"comments_count": -1, "title": 1}}
    most_popular_news = search_news(query)
    response = [
        (most_news["title"], most_news["url"])
        for most_news in most_popular_news[:5]
    ]
    return response


# Requisito 11
def top_5_categories():
    query = {"$query": {}, "$orderby": {"category": 1}}
    news = search_news(query)
    categories = [news["category"] for news in news]
    top_5 = Counter(categories).most_common(5)
    response = [category for category, _ in top_5]
    return response