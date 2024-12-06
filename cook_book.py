data = """
Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт
"""

cook_book = {}

lines = data.strip().split('\n')

i = 0

while i < len(lines):
    dish_name = lines[i].strip()
    i += 1

    if i >= len(lines):
        break

    try:
        num_ingredients = int(lines[i].strip())
    except ValueError:
        continue

    i += 1

    ingredients = []

    for _ in range(num_ingredients):
        ingredient_data = lines[i].split(' | ')
        ingredients.append({
            'ingredient_name': ingredient_data[0].strip(),
            'quantity': int(ingredient_data[1].strip()),
            'measure': ingredient_data[2].strip()
        })
        i += 1

    cook_book[dish_name] = ingredients

print(cook_book)