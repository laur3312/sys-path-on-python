#import argparse

#parser = argparse.ArgumentParser(description="Калькулятор CLI")
#parser.add_argument("--output", type=str, required=True, help="Название файла")
#parser.add_argument("--first", "-f", type=int, required=True, help="Первое число в выражении")
#parser.add_argument("--second", "-s", type=int, required=True, help="Второе число в выражении")
#arser.add_argument("--operation", "-o", choices=["+", "-", "*", "/"], default="+", help="Операция")

#args = parser.parse_args()


#match args.operation:
#   case "+":
#       result = args.first + args.second
#    case "-":
#       result = args.first - args.second
#    case "*":
#        result = args.first * args.second
#    case "/":
#        result = args.first / args.second

#message = f"Выражение: {args.first} {args.operation} {args.second} = {result}"

#with open(args.output, "w", encoding="utf-8") as f:
#    f.write(message)


import argparse

parcer = argparse.ArgumentParser(description="Калькулятор CLI")
parcer.add_argument("--input", "-i", type=str, required=True, help="Название входного файла")
parcer.add_argument("--output", "-o", type=str, required=True, help="Название выходного файла")


args = parcer.parse_args()

# Пример использования аргументов
print(f"Входной файл: {args.input}")
print(f"Выходной файл: {args.output}")