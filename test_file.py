import unittest
import os
from main import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Создает временную библиотеку для тестирования."""
        self.library = Library('test_library.json')
        # Удаляем файл, если он существует
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')

    def test_add_book(self):
        """Тестирование добавления книги."""
        self.library.add_book("1984", "George Orwell", 1949)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")

    def test_remove_book(self):
        """Тестирование удаления книги."""
        self.library.add_book("1984", "George Orwell", 1949)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_search_book_by_title(self):
        """Тестирование поиска книги по заголовку."""
        self.library.add_book("1984", "George Orwell", 1949)
        results = self.library.search_books("1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

    def test_search_book_by_author(self):
        """Тестирование поиска книги по автору."""
        self.library.add_book("1984", "George Orwell", 1949)
        results = self.library.search_books("George Orwell")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "George Orwell")

    def test_change_status(self):
        """Тестирование изменения статуса книги."""
        self.library.add_book("1984", "George Orwell", 1949)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def tearDown(self):
        """Удаление временного файла после тестирования."""
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')

if __name__ == '__main__':
    unittest.main()
