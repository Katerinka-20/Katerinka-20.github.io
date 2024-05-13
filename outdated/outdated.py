Looks like there's an issue with running the Python script through Node.js, causing an EOF (End of File) error. We can't directly execute Python scripts in this environment, but I can help you correct the Python code.

The problem seems to stem from trying to read input interactively while running the script non-interactively. Let's simplify the script to just accept command-line arguments for dates and print the converted ISO dates.

Here's the modified Python script:

python
# outdated.py

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

def main(date_str):
    try:
        iso_date = convert_to_iso(date_str)
        print(iso_date)
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите дату в формате 'год-месяц-день'.")

if __name__ == "__main__":
    import sys
    for date_str in sys.argv[1:]:
        main(date_str)
