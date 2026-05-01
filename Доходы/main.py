from utils import input_int
from expenses import *
from storage import save_expenses, load_expenses


DATA_FILE = 'data/expenses.csv'
expenses = load_expenses(DATA_FILE)

print("Приложение для учета расходов")
print('Версия 1.0')
while True:
    print('\nМеню:')
    print('1. Показать расходы')
    print('2. Добавить расход')
    print('3. Удалить расход')
    print('4. Калькулятор расходов')
    print('5. Выход')

    choice = input_int("Выберите пункт меню: ", 1, 5)

    if choice == 1:
        show_expenses(expenses)

    elif choice == 2:
        category = input('Введите категорию расхода: ') 
        amount = input('Введите сумму расхода: ')
        comment = input('Введите комментарий: ')

        add_expense(expenses, category, amount, comment)
        save_expenses(DATA_FILE, expenses)
        print('\nРасход добавлен в список и файл')

    elif choice == 3:
        if len(expenses) == 0:
            print('Удалять нечего')
        else:
            show_expenses(expenses)
            number = input_int('Введите номер расхода для удаления: ', 1, len(expenses))

            is_deleted = delete_expense(expenses, number)

            if is_deleted:
                save_expenses(DATA_FILE, expenses)
                print('Расход удален')
            else:
                print('Не удалось удалить расход')

    elif choice == 4:
        if len(expenses) == 0:
            print('Расходов пока нет')
        else:
            total = calculate_total(expenses)
            # average, max_expense

            print('\nСтатистика расходов:')
            print(f'Общая сумма {total} руб.')
            print('Средний рахсод')
            print(
                f'Самый большой расход: '
                f'Категория расхода - цена в руб. (комментарий)'
                
            )

    elif choice == 5:
        print('Программа завершена')
        break
        
    else:
        print('Такого пункта меню не существует.')