months = ["январь", "февраль", "март", "апрель",
          "май", "июнь", "июль", "август", "сентябрь", "октябрь",
          "ноябрь", "декабрь"]

def get_iso_date(date_str):
    parts = date_str.split()
    if len(parts) == 3:
        day, month, year = parts
        if month.isdigit():
            month = int(month)
            if 1 <= month <= 12:
                month = months[month - 1]
            else:
                return None
        else:
            month = month.lower()
            if month not in months:
                return None
        month_index = months.index(month) + 1
        return f"{year}-{month_index:02d}-{int(day):02d}"
    else:
        return None

def main():
    while True:
        date_input = input("Дата: ")
        iso_date = get_iso_date(date_input)
        if iso_date:
            print(iso_date)
            break
        else:
            print("Неправильный формат. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
