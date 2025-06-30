# Задача по парсингу списка и записи в другой файл
import os, pprint

path = os.getcwd()

def create_cook_book():
    with open(f'{path}/recipes.txt', 'r', encoding='utf-8') as f:
        # env block
        cook_book = {}
        # pprint.pprint(f.readline())
        # begin code
        file = f.readline().strip()
        while file != '':
            # env block
            elem2 = []
            ingridient_count = 0
            list_ingridient = []
            # begin code
            if ('|') not in file and file.isdigit() != True:
                dishes_name = file
                file = f.readline().strip()

            if file.isdigit() == True:
                ingridient_count = (int(file))
                file = f.readline().strip()

            if ('|') in file:
                for _ in range(ingridient_count):
                    elem2 = file.split('|')
                    list_ingridient.append({f'ingredient_name': elem2[0], 'quantity': elem2[1], 'measure': elem2[2]})
                    file = f.readline().strip()
            # print(dishes_name,ingridient_count,list_ingridient)
            cook_book[dishes_name] = list_ingridient
            file = f.readline().strip()
    return cook_book

# pprint.pprint(create_cook_book())

# Принимаем на вход название блюда, кол-во первос и выводим список ингридиентов с учетом кол-ва персон

for key, val in create_cook_book().items():
    list = {}
    # print(key,val)
    for item in val:
        # print(item.values())
        # list.append(item.values())
        # print(list)
        item["quantity"] = int(item["quantity"].strip())*2
        # print(f'{item.pop("ingredient_name").strip()}: {item}')
        list[item.pop("ingredient_name").strip()] = item
        print(list)
    # if key == 'Омлет':
    #     print(key,val)
    #     for item1 in val:
    #         print(item1)
    #         for item2 in item1.values():
    #             print(item2)

pprint.pprint(list)


# Тестирование разных вариантов

# with open(f'{path}/txt1.txt', 'w+', encoding='utf8') as file:
#     file.write('Винный уксус | 1 | ст.л')

# with open(f'{path}/txt1.txt', 'r', encoding='utf8') as file:
#     # print(file.readlines())
#     for elem1 in file:
#         elem1 = elem1.split(' | ')
#         cook_book = {f'ingredient_name': elem1[0], 'quantity': elem1[1], 'measure': elem1[2]}
#         print(cook_book)

# with open(f'{path}/recipes.txt', 'r', encoding='utf8') as file:
#     file1 = file.readline().strip()
#     while file1 != '':
#         print(f'зашли с {file1}')
#         file.readline()
#         file1 = file.readline().strip()
#         print(f'вышли с {file1}')