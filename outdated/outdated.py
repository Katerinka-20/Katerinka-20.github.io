months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

def get_month_number(month_str):
    return months.index(month_str) + 1

def is_valid_date(date_str):
    parts = date_str.split('.')
    if len(parts) == 3:
        day, month, year = parts
        if month.isdigit():
            month = int(month)
            if month < 1 or month > 12:
                return False
        else:
            month = get_month_number(month)
        if day.isdigit():
            day = int(day)
            if day < 1 or day > 31:
                return False
        if len(year) == 4 and year.isdigit():
            return True
    return False

def convert_to_iso_date(date_str):
    parts = date_str.split('.')
    day, month, year = parts
    if not month.isdigit():
        month = str(get_month_number(month)).zfill(2)
    else:
        month = month.zfill(2)
    day = day.zfill(2)
    return f"{year}-{month}-{day}"
