cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file:
    while True:
        dish_name = file.readline().strip()
        if not dish_name:
            break
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient_data = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_data[0],
                'quantity': int(ingredient_data[1]),
                'measure': ingredient_data[2]
            })
        cook_book[dish_name] = ingredients
        file.readline()  # Пропуск пустой строки

print(cook_book)
