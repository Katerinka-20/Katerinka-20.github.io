months = ["январь", "февраль", "март", "апрель",
          "май", "июнь", "июль", "август", "сентябрь", "октябрь",
          "ноябрь", "декабрь"]

# Функция для проверки правильности ввода даты
def is_valid_date(date_str):
    parts = date_str.split('.')
    if len(parts) != 3:
        return False
    day, month, year = parts
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    month = int(month)
    if month < 1 or month > 12:
        return False
    return True

# Цикл для ввода даты в старом формате
while True:
    try:
        date = input("Дата: ").lower()  # Приводим введенное значение к нижнему регистру
        if is_valid_date(date):
            break
        else:
            print("Неправильный формат даты. Попробуйте еще раз.")
    except EOFError:  # Пользователь нажал control-d
        print("Программа завершена.")
        exit()

# Разбиваем введенную дату на составляющие
day, month_str, year = date.split('.')
month = months.index(month_str) + 1  # Получаем номер месяца

# Форматируем вывод с нулем впереди при необходимости
print(f"{year}-{month:02}-{day:02}")
