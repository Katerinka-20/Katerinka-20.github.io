menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

total_cost = 0

try:
    while True:
        dish = input("Блюдо: ").lower()
        if dish in menu:
            total_cost += menu[dish]
except EOFError:
    print(f"Сумма: {total_cost:.2f}")