def get_month_number(month_name):
    months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    return months.index(month_name) + 1

def convert_to_iso(date_str):
    parts = date_str.split('-')
    if len(parts) == 3:
        year, month, day = parts
    else:
        parts = date_str.split()
        day = parts[0]
        month = get_month_number(parts[1].lower())
        year = parts[2]
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
