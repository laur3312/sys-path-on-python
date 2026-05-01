import csv
import os

def save_expenses(path, expenses): # path = 'data/expenses.csv'
    """
    Сохраняет расходы в CSV-файл
    """
    
    folder = os.path.dirname(path) # 'data/expenses.csv' = 'data/'

    if folder:
        os.makedirs(folder, exist_ok=True)


    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['category','amount','comment'])

        for expense in expenses:
            writer.writerow([
                expense['category'],
                expense['amount'],
                expense['comment']
            ])

def load_expenses(path):
    """
    Загружает расходы из CSV-файла
    """
    expenses = []

    if not os.path.exists(path):
        return expenses
    
    with open(path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense = {
                'category': row['category'],
                'amount': float(row['amount']),
                'comment': row['comment']     
            }

            expenses.append(expense)
    
    return expenses