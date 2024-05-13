months = ["январь", "февраль", "март", "апрель",
          "май", "июнь", "июль", "август", "сентябрь", "октябрь",
          "ноябрь", "декабрь"]

# Функция для проверки правильности ввода даты
def is_valid_date(date_str):
    parts = date_str.split('.')
    if len(parts) != 3:
        return False
    day, month, year = parts
    if not (day.isdigit() and month.replace(' ', '').isdigit() and year.isdigit()):
        return False
    month = int(month)
    if month < 1 or month > 12:
        return False
    return True

# Функция для получения номера месяца
def get_month_number(month_str):
    try:
        return int(month_str.replace(' ', ''))
    except ValueError:
        return months.index(month_str.lower()) + 1

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
month = get_month_number(month_str)  # Получаем номер месяца

# Проверка на корректность дня
if int(day) < 1 or int(day) > 31:
    print("Неправильный формат даты. Попробуйте еще раз.")
    exit()

# Форматируем вывод с нулем впереди при необходимости
print(f"{year}-{month:02}-{day:02}")
