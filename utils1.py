def input_to_int(text, default_value=0):
    try:
        result = int(text)
    except:
        result = default_value
        print("Ошибка ввода. Установлено значение по умолчанию")
    return result