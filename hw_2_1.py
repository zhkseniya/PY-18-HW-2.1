# Задание №1
def get_cookbook():
    READ_EMPTY_LINE = 1
    READ_DISH = 2
    READ_INGREDIENT = 3

    cookbook = {}
    current_state = READ_EMPTY_LINE
    
    with open('cookbook.txt') as cookbook_file:
        for cookbook_line in cookbook_file:
            cookbook_line_without_space = cookbook_line.strip()
            if not cookbook_line_without_space:
                current_state = READ_EMPTY_LINE
                continue
            if current_state == READ_EMPTY_LINE:
                dish = cookbook_line_without_space
                current_state = READ_DISH
            elif current_state == READ_DISH:
                current_state = READ_INGREDIENT
            elif current_state == READ_INGREDIENT:
                list_ingredients = cookbook_line_without_space.split('|')
                if dish not in cookbook:
                    cookbook[dish] = list()
                cookbook[dish].append({
                    'ingridient_name': list_ingredients[0].strip(),
                    'quantity': int(list_ingredients[1].strip()), 
                    'measure': list_ingredients[2].strip()
                })
        return cookbook

# Задание 2
def get_shop_list_by_dishes(dishes, person_count, cookbook):
    shop_list = {}
    for selected_dish in dishes:
        if selected_dish in cookbook:
            for dish in cookbook[selected_dish]:
                if dish['ingridient_name'] in shop_list:
                    shop_list[dish['ingridient_name']]['quantity'] += (dish['quantity'])*person_count
                else:
                    shop_list[dish['ingridient_name']] = {'measure': dish['measure'], 'quantity': int(dish['quantity'])*person_count}
        else:
            print('Рецепта блюда {} нет в кулинарной книге'.format(selected_dish))
    print(shop_list)


cookbook = get_cookbook()
get_shop_list_by_dishes(['Пельмени', 'Омлет'], 2, cookbook)