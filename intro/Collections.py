### task 1

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

for value in geo_logs:
    for key, lists in value.items():
        if "Россия" in lists:
            print(value)

### task 2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


new_ids = set()
for value in ids.values():
    for elem in value:
        new_ids.add(elem)

print(list(new_ids))

### task 3


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

number_words = [query.split() for query in queries]
print(number_words)

one = 0
two = 0
tree = 0

for line in queries:
    if line.count(' ') == 0:
        one += 1
    if line.count(' ') == 1:
        two += 1
    if line.count(' ') == 2:
        tree += 1

print(f'Общее число запросов {len(queries)}',
      f'Процент запросов с одни словом -  {round(one / len(queries) * 100)}%',
      f'Процент запросов с двумя словами - {round((two / len(queries)*100), 2)}%',
      f'Процент запросов с тремя словами - {round((tree / len(queries) * 100), 2)}%',
      sep = '\n')

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]
number_words = [len(query.split()) for query in queries]
result = dict.fromkeys(set(number_words), 0)
print(result)
for count_word in result:
    result[count_word] = number_words.count(count_word)
for word in result.items():
    print(f'Запросов с {word[0]} словами(словом) -  {round((word[1] * 100 / len(queries)), 2)}%')

### task 4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98, 'other': {'twitter': 200, 'telegram': 300}}
print(max(stats.values()))

key = {}
max_value = -1

for word,value in stats.items():
    if value > max_value:
        max_value = value
        key = word
        #print (key,value)

print(f'Канал, с максимальным объемом продаж - "{key}"')

new_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)

new_stats = sorted(stats.items())
print(new_stats)

tables = [lambda x = x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())

### task 5

lists = ['2018-01-01', 'yandex', 'cpc', 100]
new_list = dict()

for elem in lists[::-1]:
    #print(elem)
    if new_list == {}:
        new_list = elem
    else:
        new_list = {elem: new_list}

print(new_list)