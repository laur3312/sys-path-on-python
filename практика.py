import pandas as pd
from bs4 import BeautifulSoup
import requests

travel_books = []

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

responce = requests.get(url)

html_content = responce.text

soup = BeautifulSoup(html_content, "html.parser")

book_list = soup.find_all("article", class_="product_pod")

for book in book_list:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][-1]

    print(f"Название: {title}, Цена: {price}, Рейтинг: {rating}")

    travel_books.append({
        "Title": title,
        "Price": price,
        "Rating":rating
    })

    df = pd.DataFrame(travel_books)
    df.to_csv("travel_books.csv", index=False)
    print("Готово!")