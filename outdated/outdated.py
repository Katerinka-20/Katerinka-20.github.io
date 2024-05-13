def is_valid_date(day, month, year):
    # Проверяем корректность дня, месяца и года
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if year < 1:
        return False
    # Проверяем корректность дня в зависимости от месяца
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        elif day > 28:
            return False
    return True

def convert_to_iso_date(date_str):
    # Словарь для соответствия месяца его числовому представлению
    months = {
        "январь": 1, "февраль": 2, "март": 3, "апрель": 4,
        "май": 5, "июнь": 6, "июль": 7, "август": 8,
        "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12
    }
    try:
        # Разбиваем строку на день, месяц и год
        parts = date_str.split('.')
        if len(parts) == 3:
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        else:
            parts = date_str.split()
            day, month, year = int(parts[0]), months[parts[1]], int(parts[2])
        # Проверяем корректность введенной даты
        if is_valid_date(day, month, year):
            # Форматируем дату в ISO 8601
            iso_date = f"{year:04d}-{month:02d}-{day:02d}"
            return iso_date
    except (ValueError, KeyError):
        pass
    return None

def main():
    while True:
        date_str = input("Дата: ")
        iso_date = convert_to_iso_date(date_str)
        if iso_date:
            print(f"Дата в формате ISO 8601: {iso_date}")
            break
        else:
            print("Неправильный формат даты. Пожалуйста, введите снова.")

if __name__ == "__main__":
    main()
