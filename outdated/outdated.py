def month_to_number(month):
    months = {
        "январь": "01",
        "февраль": "02",
        "март": "03",
        "апрель": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "август": "08",
        "сентябрь": "09",
        "октябрь": "10",
        "ноябрь": "11",
        "декабрь": "12"
    }
    return months.get(month.lower(), None)

def validate_date(date_str):
    parts = date_str.split('.')
    if len(parts) == 3:
        day, month, year = parts
        if month.isdigit() and 1 <= int(month) <= 12:
            month = month.zfill(2)
        else:
            month = month_to_number(month)
            if not month:
                return None
        if day.isdigit() and 1 <= int(day) <= 31:
            day = day.zfill(2)
        else:
            return None
        if len(year) == 4 and year.isdigit():
            return f"{year}-{month}-{day}"
    return None

def main():
    while True:
        date_input = input("Дата: ")
        formatted_date = validate_date(date_input)
        if formatted_date:
            print(f"Дата: {formatted_date}")
            break
        else:
            print("Неправильный формат даты. Пожалуйста, введите снова.")

if __name__ == "__main__":
    main()
