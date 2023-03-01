from codecs import open
from pprint import pprint


# Задача №1
def get_cook_book_dict(file_name):
    f = open(file_name, encoding='utf-8')
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingridients_cnt = int(f.readline().strip())
        ingridients = []
        ingridient = {}
        for i in range(ingridients_cnt):
            ingr = f.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingridient['ingredient_name'] = ingredient_name
            ingridient['quantity'] = int(quantity)
            ingridient['measure'] = measure
            ingridients.append(ingridient)
            ingridient = {}
        cook_book[dish_name] = ingridients
        f.readline()
    f.close()
    return cook_book


print('\n' * 2, 'Задача №1')
pprint(get_cook_book_dict('recipes.txt'), sort_dicts=False)


# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book_dict('recipes.txt')
    print(type(cook_book))
    ingredients = {}
    for dish_name in dishes:
        for ingredient in cook_book[dish_name]:
            if ingredient['ingredient_name'] not in ingredients:
                ingredients[ingredient['ingredient_name']] = \
                    {'measure': ingredient['measure'],
                     'quantity': ingredient['quantity'] * person_count
                     }
            else:
                ingredients[ingredient['ingredient_name']]['quantity'] += \
                    ingredient['quantity'] * person_count

    return ingredients


res_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print('\n' * 3, 'Задача №2')
pprint(res_dict)


# Задача №3
def get_mutated_file():
    file_1 = open('1.txt', encoding='utf-8')
    file_2 = open('2.txt', encoding='utf-8')
    file_3 = open('3.txt', encoding='utf-8')

    lst_1 = file_1.readlines()
    lst_2 = file_2.readlines()
    lst_3 = file_3.readlines()

    file_1.close()
    file_2.close()
    file_3.close()

    mutated_lst = []

    for lst_len in sorted([len(lst_1), len(lst_2), len(lst_3)]):
        if len(lst_1) == lst_len:
            mutated_lst.append('1.txt')
            mutated_lst.append(str(len(lst_1)))
            for line in lst_1:
                mutated_lst.append(line.strip())
        elif len(lst_2) == lst_len:
            mutated_lst.append('2.txt')
            mutated_lst.append(str(len(lst_2)))
            for line in lst_2:
                mutated_lst.append(line.strip())
        elif len(lst_3) == lst_len:
            mutated_lst.append('3.txt')
            mutated_lst.append(str(len(lst_3)))
            for line in lst_3:
                mutated_lst.append(line.strip())

    result = open('mutated.txt', 'w', encoding='utf-8')
    result.write('\n'.join(mutated_lst))
    result.close()


get_mutated_file()