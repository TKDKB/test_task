import json
import os


class Book:
    """Класс для представления книги в библиотеке."""
    def __init__(self, book_id, title, author, year, status="в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Преобразует объект книги в словарь для сохранения в JSON."""
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }


class Library:
    """Класс для управления библиотекой книг."""
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Загружает книги из JSON файла."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.books = [Book(**book) for book in json.load(file)]

    def save_books(self):
        """Сохраняет книги в JSON файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """Добавляет новую книгу в библиотеку."""
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f'Книга "{title}" добавлена успешно!')

    def remove_book(self, book_id):
        """Удаляет книгу из библиотеки по ID."""
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f'Книга с ID {book_id} удалена успешно!')
                return
        print(f'Книга с ID {book_id} не найдена!')

    def search_books(self, search_query):
        """Ищет книги по заголовку, автору или году издания."""
        found_books = [
            book for book in self.books if (
                search_query.lower() in book.title.lower() or
                search_query.lower() in book.author.lower() or
                search_query == str(book.year)
            )
        ]
        return found_books

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Книг в библиотеке нет.")
            return
        for book in self.books:
            print(
                f'ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}'
            )

    def change_status(self, book_id, new_status):
        """Изменяет статус книги по ID."""
        for book in self.books:
            if book.book_id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print(f'Статус книги с ID {book_id} изменен на "{new_status}"')
                else:
                    print('Некорректный статус. Доступные статусы: "в наличии", "выдана".')
                return
        print(f'Книга с ID {book_id} не найдена!')


def main():
    # Инициализация библиотеки
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == '3':
            search_query = input("Введите название, автора или год для поиска: ")
            results = library.search_books(search_query)
            for book in results:
                print(
                    f'ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}'
                )
            if not results:
                print("Не найдено книг по вашему запросу.")

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, new_status)

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
