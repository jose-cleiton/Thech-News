import unittest
from tech_news.functions import (
    get_tech_news,
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
    top_5_news,
    top_5_categories,
)

class TestFunctions(unittest.TestCase):
  def test_get_tech_news(self):
    result = get_tech_news(5)
    self.assertEqual(len(result), 5)
  
  def test_search_by_title(self):
    result = search_by_title('Novo iPhone')
    self.assertTrue(all(item['title'] == 'Novo iPhone' for item in result))
  
  def test_search_by_date(self):
    result = search_by_date('2022-01-01')
    self.assertTrue(all(item['date'] == '2022-01-01' for item in result))
  
  def test_search_by_tag(self):
    result = search_by_tag('Apple')
    self.assertTrue(all('Apple' in item['tags'] for item in result))
  
  def test_search_by_category(self):
    result = search_by_category('Tecnologia')
    self.assertTrue(all(item['category'] == 'Tecnologia' for item in result))
  
  def test_top_5_news(self):
    result = top_5_news()
    self.assertEqual(len(result), 5)
  
  def test_top_5_categories(self):
    result = top_5_c
    
   def test_top_5_categories(self):
    result = top_5_categories()
    self.assertEqual(len(result), 5)

if __name__ == '__main__':
  unittest.main()
   
