### Этот файл был создан для практики написания классов в рамках лекции по классам в Нетологии

## Определяем классы

class Goose:
   name = ''
   need_eat = 'yes'
   need_eggs = 'yes'
   voice = 'gaga'
   weight = '0'

class Cow:
   name = ''
   need_eat = 'yes'
   milk = 'yes'
   voice = 'moo'
   weight = '0'

class Sheep:
   name = ''
   need_eat = 'yes'
   need_cutting = 'yes'
   voice = 'bee'
   weight = '0'

class Chiken:
   name = ''
   need_eat = 'yes'
   voice = 'coco'
   eggs = 'yes'
   weight = '0'

class Goat:
   name = ''
   need_eat = 'yes'
   milk = 'yes'
   voice = 'mee'
   weight = '0'

class Duck:
   name = ''
   need_eat = 'yes'
   eggs = 'yes'
   voice = 'kryia'
   weight = '0'

## Присваиваем значения классов объектам

# Гуси "Серый" и "Белый"
gray_goose = Goose()
gray_goose.name = 'Серый'
# print(dir(gray_goose)) # получение всех параметров метода

white_goose = Goose()
white_goose.name = 'Белый'
print(f'Имена гусей - {gray_goose.name} и {white_goose.name}')
# print(dir(white_goose)) # получение всех параметров метода

# Корова "Манька"

сow_manya = Cow()
сow_manya.name = 'Манька'
print(f'Имя коровы - {сow_manya.name}, дает молоко? - {сow_manya.milk}')

# Овцы "Барашек" и "Кудрявый"

sheep_barash = Sheep()
sheep_curly = Sheep()

sheep_barash.name = 'Барашек'
sheep_curly.name = 'Кудрявый'

print(f'Имя барашков - {sheep_barash.name} и {sheep_curly.name}')

# Куры "Ко-ко" и "Кукареку"

chiken_coco = Chiken()
chiken_kykareky = Chiken()

chiken_coco.name = 'Ко-ко'
chiken_kykareky.name = 'Кукареку'

print(f'Имя курочек - {chiken_coco.name} и {chiken_kykareky.name}')

# Козы "Рога" и "Копыта"

goat_horns = Goat()
goat_hooves = Goat()

goat_horns.name = 'Рога'
goat_hooves.name = 'Копыта'

print(f'Имя коз - {goat_horns.name} и {goat_hooves.name}')

# Утка "Крыква"

duck_krykva = Duck()

duck_krykva.name = 'Крыква'
print(f'Имя утки  - {duck_krykva.name}')