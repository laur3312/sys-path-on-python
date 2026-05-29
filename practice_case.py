import json
import os

# Имя файла для хранения базы данных склада
DB_FILE = 'inventory.json'

def load_data():
    """Загружает данные из JSON файла. Если файла нет, возвращает пустой словарь."""
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Ошибка чтения файла базы данных. Создан новый склад.")
            return {}
    return {}

def save_data(data):
    """Сохраняет текущие данные в JSON файл."""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_product(data):
    """Добавляет новый товар на склад."""
    name = input("Введите название товара: ").strip()
    if name in data:
        print("Такой товар уже существует! Используйте редактирование.")
        return
    
    category = input("Введите категорию товара: ").strip()
    while True:
        try:
            quantity = int(input("Введите количество: "))
            if quantity < 0:
                print("Количество не может быть отрицательным.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")
            
    data[name] = {"category": category, "quantity": quantity}
    save_data(data)
    print(f"Товар '{name}' успешно добавлен.")

def view_inventory(data):
    """Выводит текущие запасы на экран."""
    if not data:
        print("\nСклад пуст.")
        return
    
    print("\n--- ТЕКУЩИЕ ЗАПАСЫ НА СКЛАДЕ ---")
    for name, info in data.items():
        print(f"Товар: {name} | Категория: {info['category']} | Количество: {info['quantity']}")
    print("--------------------------------")

def edit_product(data):
    """Редактирует количество товара при поступлениях или продажах."""
    name = input("Введите название товара для редактирования: ").strip()
    if name not in data:
        print("Товар не найден.")
        return
    
    print(f"Текущее количество товара '{name}': {data[name]['quantity']}")
    print("1 - Поступление (добавить)")
    print("2 - Продажа (списать)")
    choice = input("Выберите действие: ").strip()
    
    if choice not in ['1', '2']:
        print("Неверный выбор.")
        return
        
    while True:
        try:
            amount = int(input("Введите количество единиц товара: "))
            if amount <= 0:
                print("Число должно быть больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")
            
    if choice == '1':
        data[name]['quantity'] += amount
        print("Баланс успешно пополнен.")
    elif choice == '2':
        if data[name]['quantity'] < amount:
            print(f"Ошибка списания! На складе недостаточно товара (доступно: {data[name]['quantity']}).")
            return
        data[name]['quantity'] -= amount
        print("Товар успешно списан.")
        
    save_data(data)

def delete_product(data):
    """Удаляет позицию товара со склада."""
    name = input("Введите название товара для удаления: ").strip()
    if name in data:
        del data[name]
        save_data(data)
        print(f"Товар '{name}' успешно удален из базы данных.")
    else:
        print("Товар не найден.")

def main():
    # Загружаем сохраненную базу данных при старте
    data = load_data()
    
    while True:
        print("\n*** СУБД: УЧЕТ ТОВАРНЫХ ОСТАТКОВ ***")
        print("1 - Просмотреть текущие запасы")
        print("2 - Добавить новый товар")
        print("3 - Редактировать количество (Поступление/Продажа)")
        print("4 - Удалить товар")
        print("0 - Выход из программы")
        
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == '1':
            view_inventory(data)
        elif choice == '2':
            add_product(data)
        elif choice == '3':
            edit_product(data)
        elif choice == '4':
            delete_product(data)
        elif choice == '0':
            print("Программа завершена. Данные сохранены.")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")

if __name__ == '__main__':
    main()
