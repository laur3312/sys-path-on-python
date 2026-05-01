
# вызов функции 
# input_int("Выберите пункт меню: ", 1, 5)
def input_int(message, min_value, max_value):
    """
    Запрашивает у пользователя целое число в заданном диапазоне.
    """

    while True:
        value = input(message)

        if not value.isdigit():
            print('Ошибка: нужно ввести число')
            continue

        number = int(value)

        if min_value <= number <= max_value:
            return number
        
        print(f'Ошибка: число должно быть от {min_value} до {max_value}')