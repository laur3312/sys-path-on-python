def add_expense(expenses, category, amount, comment):
    """
    Добавляет новый расход в список.
    """
    expense = {
        'category':category,
        'amount':amount,
        'comment':comment
    }

    expenses.append(expense)

def show_expenses(expenses):
    """
    Показывает список расходов
    """
    if len(expenses) == 0:
        print('Пока расходов нет')
    else:
        print('\nСписок расходов:')

        for index, expense in enumerate(expenses, start=1):
            print(
                f'{index}. {expense['category']} - '
                f'{expense['amount']} руб. '
                f'({expense['comment']})'
            )

def delete_expense(expenses, index):
    """
    Удаляет расход по номеру.
    """

    real_index = index - 1

    if real_index < 0 or real_index >= len(expenses):
        return False
    
    expenses.pop(real_index)

    return True

# Калькулятор
def calculate_total(expenses):
    """
    Считает общую сумму расходов
    """

    total = 0
    for expense in expenses:
        total += expense['amount']

    return total

def calculate_average(expenses):
    """
    Считает средний расход
    """
    pass

def find_max_expense(expenses):
    """
    Находит самый большой расход
    """
    pass