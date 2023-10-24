menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

selected_items = []

while True:
    try:
        item = input("Блюдо: ")
        selected_items.append(menu[item])
    except EOFError:
        break
total = sum(selected_items)
print(f"Сумма: {total:.2f}")