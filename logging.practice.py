import logging

logging.basicConfig (filename = "qwerty.py", level = logging.DEBUG)

logging.debug ("Переменная x после вычисления стала равна")
logging.info("Пользователь Petr успешно вошел в систему")
logging.warning("Век-пароль не подошел с первой попытки, но со второй всё сработало")
logging.critical("База данных стерта, сайту не откуда брать информацию, работа полностью остановлена.")