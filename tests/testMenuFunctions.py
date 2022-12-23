import unittest
from tech_news.menu import (
    get_get_tech_news,
    get_search_by_title,
    get_search_by_date,
    get_search_by_tag,
    get_search_by_category,
    top_news,
    top_categories,
    exit_script,
    METHODS,
    menu,
    menu_options,
)

class TestMenuFunctions(unittest.TestCase):
  def test_get_get_tech_news(self):
    result = get_get_tech_news()
    self.assertIsNotNone(result)

  def test_get_search_by_title(self):
    result = get_search_by_title()
    self.assertIsNotNone(result)

  def test_get_search_by_date(self):
    result = get_search_by_date()
    self.assertIsNotNone(result)

  def test_get_search_by_tag(self):
    result = get_search_by_tag()
    self.assertIsNotNone(result)

  def test_get_search_by_category(self):
    result = get_search_by_category()
    self.assertIsNotNone(result)

  def test_top_news

  def test_top_news(self):
    result = top_news()
    self.assertIsNotNone(result)

  def test_top_categories(self):
    result = top_categories()
    self.assertIsNotNone(result)

  def test_exit_script(self):
    result = exit_script()
    self.assertIsNone(result)

  def test_METHODS(self):
    self.assertEqual(len(METHODS), 7)

  def test_menu(self):
    self.assertIsNotNone(menu)

  def test_menu_options(self):
    self.assertEqual(len(menu_options), 7)

if __name__ == '__main__':
  unittest.main()
