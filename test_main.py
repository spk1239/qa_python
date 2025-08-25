from main import BooksCollector
import pytest

class TestBooksCollector:
    #Добавление книг с валидным числом символов
    @pytest.mark.parametrize("books", ["И", "Мастер и Маргар", "Властелин колец: Братство кольцааааааааа"])
    def test_add_new_book_books_lens_1_15_40_added_collector(self, books):
        collector = BooksCollector()
        collector.add_new_book(books)
        assert len(collector.get_books_genre()) == 1

    #Добавление книг с невалидным числом символов
    @pytest.mark.parametrize("books", ["", "Властелин колец: Братство кольцаааааааааа", "Божественный Пятячок: 55555555555555555555555555555555"])
    def test_add_new_book_books_lens_0_41_55_not_added_collector(self, books):
        collector = BooksCollector()
        collector.add_new_book(books)
        assert len(collector.get_books_genre()) == 0
    #Установка жанра
    def test_set_book_genre_horror_genre_added(self):
        collector= BooksCollector()
        collector.add_new_book("Маньяки 16")
        collector.set_book_genre("Маньяки 16","Ужасы")
        assert collector.get_book_genre("Маньяки 16") == "Ужасы"
    #Установка жанра не из списка
    def test_set_book_genre_add_not_list_genre_melodram(self):
        collector= BooksCollector()
        collector.add_new_book("Слёзы, боль и рак селезёнки")
        collector.set_book_genre("Слёзы, боль и рак селезёнки", "Мелодраммы")
        assert collector.get_book_genre("Слёзы, боль и рак селезёнки") == ""
        
    #Получение жанра по названию книги
    def test_get_book_genre_horror_genre_view(self):
        collector= BooksCollector()
        collector.add_new_book("Маньяки 16")
        collector.set_book_genre("Маньяки 16","Ужасы")
        assert collector.get_book_genre("Маньяки 16") == "Ужасы"

    #Получение списка книг с определенным жанром
    def test_get_books_with_specific_genre_detectiv_genre_show_books(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс","Детективы")
        assert collector.get_books_with_specific_genre("Детективы") == ["Шерлок Холмс"]

    #Получение словаря 
    def test_get_books_genre_two_books_show_books(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс","Детективы")
        collector.add_new_book("Маньяки 16")
        collector.set_book_genre("Маньяки 16","Ужасы")
        assert collector.get_books_genre() == {"Шерлок Холмс": "Детективы", "Маньяки 16": "Ужасы"}

    #Получение книг для детей
    def test_get_books_for_children_two_books_show_one_cartoon_book(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс","Детективы")
        collector.add_new_book("Мишки Гамми")
        collector.set_book_genre("Мишки Гамми", "Мультфильмы")
        assert collector.get_books_for_children() == ["Мишки Гамми"]

    #Добавление книги в избранный список
    def test_add_book_in_favorites_one_book_added_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.add_book_in_favorites("Шерлок Холмс")
        assert collector.get_list_of_favorites_books() == ["Шерлок Холмс"]

    #Удаление книги из избранного списка
    def test_delete_book_from_favorites_one_book_deleted_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.add_book_in_favorites("Шерлок Холмс")
        collector.delete_book_from_favorites("Шерлок Холмс")
        assert collector.get_list_of_favorites_books() == []

    #Получение списка избранных книг
    def test_get_list_of_favorites_books_one_book_getting_book(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.add_book_in_favorites("Шерлок Холмс")
        assert collector.get_list_of_favorites_books() == ["Шерлок Холмс"]
