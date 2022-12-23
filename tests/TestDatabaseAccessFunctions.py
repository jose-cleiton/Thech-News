import unittest
from tech_news.database import (
    create_news,
    insert_or_update,
    find_news,
    search_news,
    get_collection,
)

class TestDatabaseFunctions(unittest.TestCase):
  def setUp(self):
    self.data = [
      {
        'title': 'Notícia 1',
        'url': 'http://teste.com/noticia1',
        'date': '2022-01-01',
        'tags': ['teste', 'banco de dados'],
        'category': 'Tecnologia',
        'content': 'Conteúdo da notícia 1',
      },
      {
        'title': 'Notícia 2',
        'url': 'http://teste.com/noticia2',
        'date': '2022-01-02',
        'tags': ['teste', 'banco de dados'],
        'category': 'Tecnologia',
        'content': 'Conteúdo da notícia 2',
      },
    ]

  def test_create_news(self):
    create_news(self.data)
    result = find_news()
    self.assertEqual(len(result), 2)

  def test_insert_or_update(self):
    insert_or_update(self.data[0])
    result = search_news({'url': 'http://teste.com/noticia1'})
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0]['title'], '



  def test_insert_or_update(self):
    insert_or_update(self.data[0])
    result = search_news({'url': 'http://teste.com/noticia1'})
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0]['title'], 'Notícia 1')
    self.assertTrue(insert_or_update(self.data[0]))
    result = search_news({'url': 'http://teste.com/noticia1'})
    self.assertEqual(len(result), 1)

  def test_find_news(self):
    result = find_news()
    self.assertEqual(len(result), 2)

  def test_search_news(self):
    result = search_news({'tags': 'teste'})
    self.assertEqual(len(result), 2)

  def test_get_collection(self):
    result = get_collection()
    self.assertEqual(result.count(), 2)

if __name__ == '__main__':
  unittest.main()
