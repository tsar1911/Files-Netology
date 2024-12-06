from cook_book import cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }
        else:
            print(f"Блюдо '{dish}' не найдено в рецептах.")
            return {}

    return shop_list


print("Доступные блюда: ", ", ".join(cook_book.keys()))
dishes_input = input("Введите блюда, разделённые запятой (например, 'Омлет, Запеченный картофель'): ")

dishes = [dish.strip() for dish in dishes_input.split(',')]
valid_dishes = [dish for dish in dishes if dish in cook_book]

while len(valid_dishes) != len(dishes):
    invalid_dishes = set(dishes) - set(valid_dishes)
    print(f"Некоторые блюда не найдены: {', '.join(invalid_dishes)}. Попробуйте снова.")
    dishes_input = input("Введите блюда, разделённые запятой (например, 'Омлет, Запеченный картофель'): ")
    dishes = [dish.strip() for dish in dishes_input.split(',')]
    valid_dishes = [dish for dish in dishes if dish in cook_book]


person_count = int(input("Введите количество персон: "))

shop_list = get_shop_list_by_dishes(valid_dishes, person_count)

if shop_list:
    print("\nСписок покупок для ", person_count, " персон:")
    for ingredient, data in shop_list.items():
        print(f"{ingredient}: {data['quantity']} {data['measure']}")