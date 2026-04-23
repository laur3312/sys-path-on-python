import requests
from bs4 import BeautifulSoup
import pandas as pd

# Сюда будем собирать информацию о книгах
travel_books = []

# Ссылка на раздел с книгами о путешествиях
url1 = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# Стучимся на сайт и получаем ответ
response = requests.get(url1)

# Вытаскиваем из ответа «сырой» HTML-код
html_content = response.text

# Превращаем код в понятную для Python структуру (дерево тегов)
soup = BeautifulSoup(html_content, "html.parser")

# Находим все карточки книг на странице
books_list = soup.find_all("article", class_="product_pod")

# Проходимся по каждой карточке и вытаскиваем детали
for book in books_list:
    # Достаем полное название книги
    title = book.h3.a["title"]
    
    # Забираем цену в виде текста
    price = book.find("p", class_="price_color").text
    
    # Узнаем рейтинг (он спрятан в названии класса, например, "star-rating Three")
    rating = book.p["class"][-1] 
    
    # Показываем в консоли, что мы нашли
    print(f"Название: {title}, Цена: {price}, Рейтинг: {rating}")

    # Складываем данные о книге в список в виде словаря
    travel_books.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

# Оформляем список в красивую таблицу (DataFrame)
df = pd.DataFrame(travel_books)

# Сохраняем результат в CSV-файл, чтобы открыть его потом в Excel
df.to_csv("travel_books.csv", index=False)

print("Готово! Все данные в файле travel_books.csv")

# Ради интереса выведем еще и заголовок самой вкладки браузера
page_title = soup.title.text
print(f"\nМы парсили страницу: {page_title}")
