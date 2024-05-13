def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0 or x > y:
            return None
        percent = round((x / y) * 100)
        if percent <= 1:
            return 'E'
        elif percent >= 99:
            return 'F'
        else:
            return percent
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

def main():
    while True:
        fraction_input = input("Дробь: ")
        result = calculate_fuel_percentage(fraction_input)
        if result is not None:
            if result == 'E':
                print(result)
            elif result == 'F':
                print(result)
            else:
                print(result, end='')
            break
        else:
            print("Пожалуйста, введите корректную дробь.")

if __name__ == "__main__":
    main()
