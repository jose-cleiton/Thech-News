from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


# 0
def get_get_tech_news():
    data = int(input("Digite o número de notícias a serem buscadas: "))
    return get_tech_news(data)


# 1
def get_search_by_title():
    data = input("Digite o título: ")
    return search_by_title(data)


# 2
def get_search_by_date():
    data = input("Digite a data no formato aaaa-mm-dd: ")
    return search_by_date(data)


# 3
def get_search_by_tag():
    data = input("Digite a tag: ")
    return search_by_tag(data)


# 4
def get_search_by_category():
    data = input("Digite a categoria: ")
    return search_by_category(data)


# 5
def top_news():
    return top_5_news()


# 6
def top_categories():
    return top_5_categories()


def exit_script():
    print("Encerrando script")


METHODS = [
    get_get_tech_news,
    get_search_by_title,
    get_get_tech_news,
    get_search_by_tag,
    get_search_by_date,
    top_news,
    top_categories,
]

menu = (
    "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
    ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
    " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
    "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
)


menu_options = {
    "0": get_get_tech_news,
    "1": get_search_by_title,
    "2": get_search_by_date,
    "3": get_search_by_tag,
    "4": get_search_by_category,
    "5": top_news,
    "6": top_categories,
    "7": exit_script,
}