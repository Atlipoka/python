### TASK 1

## data

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
}

## define functions

def find_people(documents):
    """ Функция запрашивает номер документа и отображает ФИО владельца документа """
    inputs = str(input('Для поиска ФИО владельца, введите номер документа: '))
    for doc in documents:
        if inputs == doc['number']:
            print('Фамилия найдена - {0}'.format(doc['name']))
            break
    else:
        print('Номер документа, который вы ввели, не существует')

def find_shelf(directories):
    """ Функция запрашивает номер документа и отображает номер полки, на которой лежит документ """
    inputs = str(input('Для поиска номера полки, введите номер документа: '))
    shelf_num = []
    for key, value in directories.items():
        if inputs in value:
            shelf_num = key
    if shelf_num != []:
        print(f'Номер полки - {shelf_num}')
    else:
        print('Вы ввели некорректный номер документа или запись с таким документом отсутствует')

def doc_list(documents):
    """ Функция отображает список типа документа, номера документа и ФИО владельца документа """
    for doc in documents:
        print('{0} "{1}" "{2}"'.format(doc['type'], doc['number'], doc['name']))

def add_new_document(documents, directories):
    """ Функция запрашивает данные, такие как тип документа, номер документа, номер полки, ФИО и добавляет новый документ """
    print('Начинаем процедуру добавления новой записи')
    doc_type = input('Введите тип документа, который хотите добавить: ')
    doc_num = input('Введите номер документа, который хотите добавить: ')
    shelf = input('Введите номер полки, на которй должен лежать документ: ')
    fio = input('Введите Имя и Отчество, кому принадлежит документ: ')

    if shelf not in directories.keys():
        print(f'Такой полки не существует,есть полки - {list(directories.keys())}')
        exit()
    else:
        ## добавляем документ на полку
        directories[shelf] += [doc_num]
        ## добавляем документ в список
        documents.append({"type": doc_type, "number": doc_num, "name": fio})

    print(documents)

### TASK 2

def delete_document(documents, directories):
    """ Функция запрашивает номер документа и удаляет его из списка """
    doc_num = input('Введите номер докуметна, который хотите удалить: ')
    new_list = []
    for doc_lists in documents:
        new_list += [doc_lists['number']]

    if doc_num not in new_list:
        print(f'Такого номера документа не существует, доступные номера {new_list}')
    else:
        for doc_number in documents:
            if doc_number['number'] == doc_num:
                doc_number['number'] = ''
        for shelf_key, shelf_values in directories.items():
            if doc_num in shelf_values:
                directories[shelf_key].remove(doc_num)

    print(documents)
    print(directories)


def move_doc_on_new_shelf(documents, directories):
    """ Функция запрашивает номер документа и номер полки, на которую должен быть перемещен документ """
    document = input('Введите номер документа, который нужно переместить: ')
    shelf = input('Введите номер полки, на который нужно переместить документ: ')
    doc_list = []
    shelf_list = []

    for key, val in directories.items():
        shelf_list += key
        for va in val:
            doc_list += [va]

    if document not in doc_list:
        print(f'Вы ввели номер документа, которого не существует, доступный список документов {doc_list}')
        exit()
    elif shelf not in shelf_list:
        print(f'Вы ввели номер полки, которой не существует, доступный список полок {shelf_list}')
        exit()
    else:
        for k, v in directories.items():
            if document in v:
                directories[k].remove(document)
                directories[shelf].append(document)

    print(f'Документ {document} успешно перемещен на полку {shelf}')
    print(directories)

def add_new_shelf(directories):
    """ Функция запрашивает номер полки и добавляет ее в список """
    shelf = input('Введите номер полки, которую хотите добавить: ')
    shelf_list = []

    for key in directories.keys():
        shelf_list += key

    if shelf in shelf_list:
        print(f'Номер полки, который вы ввели, уже существует, список существующих полок {shelf_list}')
        exit()
    else:
        directories[shelf] = []

    print(directories)

## below we can execute function

# find_people(documents)
# find_shelf(directories)
# doc_list(documents)
# add_new_document(documents, directories)
# delete_document(documents, directories)
# move_doc_on_new_shelf(documents, directories)
# add_new_shelf(directories)