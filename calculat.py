from utils import input_to_int

while True:
    print("\nКалькулятор")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
    print("5 - Выход")

    choice = input("Выберите пункт меню - ")
    
    match choice:
        case "1" | "сложение":
            print("Сложение")
            numbers = input("Введите 2 целых числа через пробел: ")
            numbers = numbers.split()
            if len(numbers) != 2:
                print("Введено не 2 числа через пробел")
            else:
                try:
                    a = input_to_int(numbers[0])  # Убираем лишний input
                    b = input_to_int(numbers[1])  # Убираем лишний input
                except:
                    print("Введены некорректные значения")
                    print("Установлены значения по умолчанию")
                    a, b = 0, 0
                    
                print(a + b)

        case "2" | "вычитание":
            print("Вычитание")
            a = input_to_int(input("Введите первое число: "))
            b = input_to_int(input("Введите второе число: "))
            print(a - b)

        case "3" | "умножение":
            print("Умножение")
            a = input_to_int(input("Введите первое число: "))
            b = input_to_int(input("Введите второе число: "))
            print(a * b)
        
        case "4" | "деление":
            print("Деление")
            a = input_to_int(input("Введите первое число: "))
            b = input_to_int(input("Введите второе число: "))
            if b == 0:
                print("Ошибка: деление на ноль")
            else:
                print(a / b)
        
        case "5" | "выход":
            print("До свидания")
            break
        
        case _:
            print("Ошибка!!! Неверный выбор. Пожалуйста, выберите пункт из меню.")

            
        
        
        
        
        
  
        

 
    