def get_month_number(month_name):
    months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    return months.index(month_name) + 1

def convert_to_iso(date_str):
    if "-" in date_str:
        parts = date_str.split('-')
    elif "." in date_str:
        parts = date_str.split('.')
    elif " " in date_str:
        parts = date_str.split()
    else:
        raise ValueError("Неверный формат даты.")
    if len(parts) == 3:
        year, month, day = parts
    else:
        raise ValueError("Неверный формат даты.")
    if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
        raise ValueError("Неверный формат даты.")
    return f"{year}-{month:02}-{day:02}"

def main():
    while True:
        date = input("Дата: ")
        try:
            iso_date = convert_to_iso(date)
            print(iso_date)
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату снова.")

if __name__ == "__main__":
    main()
