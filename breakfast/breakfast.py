def main():
    menu = {
        "кофе": 20.00,
        "чай": 10.00,
        "булочка": 5.00,
        "салат": 30.40,
        "пирожное": 45.50
    }

    total_cost = 0.0

    while True:
        try:
            dish = input("Блюдо: ").lower()
        except EOFError:
            break

        if dish in menu:
            total_cost += menu[dish]

    print(f"Сумма: {total_cost:.2f}")

if __name__ == "__main__":
    main()
