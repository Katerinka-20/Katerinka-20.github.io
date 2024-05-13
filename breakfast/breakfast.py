menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

total_cost = 0


while True:
    try:
        item = input("Блюдо: ").lower()
        if item in menu:
            total_cost += menu[item]
    except EOFError:
        break


print()
print(f"Сумма: {total_cost:.2f}")
