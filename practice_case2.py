import json
import os
from datetime import datetime

# Имя файла для сохранения данных
DATA_FILE = "finance_data.json"

def load_data():
    """Загружает данные из JSON-файла или возвращает пустую структуру."""
    if not os.path.exists(DATA_FILE):
        return {"balance": 0.0, "transactions": []}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Ошибка чтения файла данных. Создан новый профиль.")
        return {"balance": 0.0, "transactions": []}

def save_data(data):
    """Сохраняет текущие данные в JSON-файл."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError:
        print("Ошибка: Не удалось сохранить данные на диск.")

def add_transaction(data, action_type):
    """Добавляет новую операцию (доход или расход)."""
    label = "дохода" if action_type == "income" else "расхода"
    
    # Ввод и валидация суммы
    while True:
        try:
            amount = float(input(f"Введите сумму {label}: "))
            if amount <= 0:
                print("Сумма должна быть больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число.")

    category = input(f"Введите категорию {label}: ").strip()
    if not category:
        category = "Разное"

    # Автоматическое определение текущей даты
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Создание записи транзакции
    transaction = {
        "type": action_type,
        "amount": amount,
        "category": category,
        "date": date_str
    }

    # Обновление баланса
    if action_type == "income":
        data["balance"] += amount
    else:
        data["balance"] -= amount

    data["transactions"].append(transaction)
    save_data(data)
    print(f"Запись успешно добавлена! Текущий баланс: {data['balance']:.2f}")

def view_statistics(data):
    """Отображает общую статистику и список операций с фильтрацией."""
    print("\n--- Финансовая статистика ---")
    print(f"Текущий баланс: {data['balance']:.2f}")
    print(f"Всего операций: {len(data['transactions'])}")
    
    if not data["transactions"]:
        print("История операций пуста.")
        return

    print("\nВыберите вариант просмотра:")
    print("1. Показать все операции")
    print("2. Фильтр по типу (Доходы)")
    print("3. Фильтр по типу (Расходы)")
    print("4. Фильтр по категории")
    
    choice = input("Выберите пункт меню: ").strip()
    filtered_list = data["transactions"]

    if choice == "2":
        filtered_list = [t for t in data["transactions"] if t["type"] == "income"]
    elif choice == "3":
        filtered_list = [t for t in data["transactions"] if t["type"] == "expense"]
    elif choice == "4":
        cat_search = input("Введите название категории для фильтра: ").strip().lower()
        filtered_list = [t for t in data["transactions"] if cat_search in t["category"].lower()]

    if not filtered_list:
        print("Операций по заданным критериям не найдено.")
        return

    print("\nСписок операций:")
    print(f"{'Дата':<20} | {'Тип':<10} | {'Сумма':<10} | {'Категория'}")
    print("-" * 60)
    for t in filtered_list:
        t_type = "Доход" if t["type"] == "income" else "Расход"
        print(f"{t['date']:<20} | {t_type:<10} | {t['amount']:<10.2f} | {t['category']}")

def main():
    """Главный цикл консольного приложения."""
    data = load_data()
    
    while True:
        print("\n=== Управление доходами и расходами ===")
        print(f"Текущий баланс: {data['balance']:.2f}")
        print("1. Добавить доход")
        print("2. Добавить расход")
        print("3. Просмотр статистики и фильтрация")
        print("4. Выйти из программы")
        
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == "1":
            add_transaction(data, "income")
        elif choice == "2":
            add_transaction(data, "expense")
        elif choice == "3":
            view_statistics(data)
        elif choice == "4":
            print("Программа завершена. Данные сохранены.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 4.")

if __name__ == "__main__":
    main()

