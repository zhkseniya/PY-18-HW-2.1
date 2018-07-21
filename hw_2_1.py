# Задание №1
def get_cookbook(count):
    with open('cookbook.txt') as cookbook_file:
        for cookbook_line in cookbook_file:
            if cookbook_line.strip() == "":
                count = 1
                continue
            if count == 1:
                dish = cookbook_line.strip()
                count += 1
            elif count == 2:
                count_ingredients = cookbook_line.strip()
                count += 1
            elif count == 3:
                list_ingredients = cookbook_line.split('|')
                if dish not in cookbook.keys():
                    cookbook[dish] = list()
                cookbook[dish].append({'ingridient_name':list_ingredients[0].strip(), 'quantity':list_ingredients[1].strip(), 'measure':list_ingredients[2].strip()})
    print(cookbook)

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for list_dishes in dishes:
        if list_dishes in cookbook:
            cookbook[list_dishes]
            for dish in cookbook[list_dishes]:
                if dish['ingridient_name'] in shop_list.keys():
                    shop_list[dish['ingridient_name']] = {'measure': dish['measure'], 'quantity': (int(dish['quantity'])*person_count)+int(result_dict[dish['ingridient_name']]['quantity'])}
                else:
                    shop_list[dish['ingridient_name']] = {'measure': dish['measure'], 'quantity': int(dish['quantity'])*person_count}
        else:
            print('Рецепта блюда {} нет в кулинарной книге'.format(list_dishes))
            continue
    print(shop_list)

cookbook = {}
line_count = 1
get_cookbook(line_count)
get_shop_list_by_dishes(['Пельмени','Омлет'], 2)