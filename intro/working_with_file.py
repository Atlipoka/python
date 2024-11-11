import os

# print(os.getcwd())
path = os.getcwd()

# with open(f'{path}/test.txt', 'r') as f:
#     print(f.read())
#
# with open(f'{path}/test.txt', 'w') as f:
#     f.write('Первая строка в файле')
#
# with open(f'{path}/test.txt', 'r') as f:
#     print(f.read())

cook_book = {}
elem2 = []
count = 0
list = []
with open(f'{path}/recipes.txt', 'r', encoding='utf-8') as f:
    print(f.readlines())
    # # print(f.read())
    # for item in f.readlines():
    #     # print(type(item))
    #     new_item=item.strip()
    #     # cook_book = {new_item: []}
    #     # print(type(item),type(new_item))
    #     # print(f'{new_item}', print(type(new_item)))
    #     # new_item.append()
    #     # print(idx, item.replace('\n',''))
    #     if new_item == '':
    #         continue
    #     else:
    #         cook_book[new_item] = [{}]
    #         if new_item.isdigit() == True:
    #             count = new_item
    #             cook_book[new_item] = [{}]*int(count)
    #             continue
    #         if ('|') in new_item:
    #             elem1 = new_item.split(' | ')
    #             elem2.append({f'ingredient_name': elem1[0], 'quantity': elem1[1], 'measure': elem1[2]})
    #             print(elem2)
    #         # print(cook_book)

            #cook_book[new_item] = [{}]*3

print(cook_book)

# with open(f'{path}/txt1.txt', 'w+', encoding='utf8') as file:
#     file.write('Винный уксус | 1 | ст.л')

# with open(f'{path}/txt1.txt', 'r', encoding='utf8') as file:
#     # print(file.readlines())
#     for elem1 in file:
#         elem1 = elem1.split(' | ')
#         cook_book = {f'ingredient_name': elem1[0], 'quantity': elem1[1], 'measure': elem1[2]}
#         print(cook_book)

# with open(f'{path}/txt1.txt', 'r', encoding='utf8') as file:
#     print(file.readlines())