import requests

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
responce = requests.get(url)

#Проверка статуса ответа
if responce.status_code == 200:
   print("Успешно получили страницу!")
else:
    print(f"Ошибка: {responce.status_code}")