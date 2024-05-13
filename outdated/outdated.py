def get_month_number(month_name):
    months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    return months.index(month_name) + 1

def convert_to_iso(date_str):
    if "." in date_str:
        parts = date_str.split('.')
    elif " " in date_str:
        parts = date_str.split()
    else:
        parts = date_str.split("-")
    if len(parts) == 3:
        day, month, year = parts
    else:
        raise ValueError("Неверный формат даты.")
    return f"{year}-{month:02}-{day:02}"

def main():
    while True:
        date = input("Дата: ")
        try:
            iso_date = convert_to_iso(date)
            print(iso_date)
            break
        except (IndexError, ValueError):
            print("Неверный формат даты. Пожалуйста, введите дату снова.")

if __name__ == "__main__":
    main()
