### Этот файл был создан для практики написания классов в рамках лекции по классам в Нетологии

## Определяем классы

class Goose:
   need_eat = 'Да'
   voice = 'Га-Га'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def have_eggs(self, none):
      val = input('Нужно ли собирать яйца, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Яйца собраны у гуся {self.name}')
      else:
         print('Яйца собирать не нужно')

class Cow:
   need_eat = 'Да'
   voice = 'Муу'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def make_milk(self, none):
      val = input('Нужно ли подоить корову, напишите Да или Нет')
      if val == 'Да':
         print(f'Корова {self.name} подоена')
      else:
         print('Корову доить ненужно')

class Sheep:
   need_eat = 'Да'
   voice = 'Бее'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def make_milk(self, none):
      val = input('Нужно ли подстричь офцу, напишите Да или Нет')
      if val == 'Да':
         print(f'Овца {self.name} подстрижена')
      else:
         print('Овцу стричь ненужно')

class Chiken:
   need_eat = 'yes'
   voice = 'coco'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def have_eggs(self, none):
      val = input('Нужно ли собирать яйца, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Яйца собраны у курочки {self.name}')
      else:
         print('Яйца собирать не нужно')

class Goat:
   need_eat = 'yes'
   voice = 'mee'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def make_milk(self, none):
      val = input('Нужно ли подоить козу, напишите Да или Нет')
      if val == 'Да':
         print(f'Коза {self.name} подоена')
      else:
         print('Козу доить ненужно')

class Duck:
   need_eat = 'yes'
   voice = 'kryia'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def have_eggs(self, none):
      val = input('Нужно ли собирать яйца, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Яйца собраны у утки {self.name}')
      else:
         print('Яйца собирать не нужно')

## Присваиваем значения классов объектам

# Гуси "Серый" и "Белый"
gray_goose = Goose('Серый', 2, 'Несет яйца')
gray_goose.have_eggs()
print(gray_goose.name, gray_goose.weight)
# print(dir(gray_goose)) # получение всех параметров метода
#
# white_goose = Goose()
# white_goose.name = 'Белый'
# print(f'Имена гусей - {gray_goose.name} и {white_goose.name}')
# print(f'Вес гуся {gray_goose.name} = {gray_goose.weight}кг.')
# # print(dir(white_goose)) # получение всех параметров метода
#
# # Корова "Манька"
#
# сow_manya = Cow()
# сow_manya.name = 'Манька'
# print(f'Имя коровы - {сow_manya.name}, дает молоко? - {сow_manya.milk}')
#
# # Овцы "Барашек" и "Кудрявый"
#
# sheep_barash = Sheep()
# sheep_curly = Sheep()
#
# sheep_barash.name = 'Барашек'
# sheep_curly.name = 'Кудрявый'
#
# print(f'Имя барашков - {sheep_barash.name} и {sheep_curly.name}')
#
# # Куры "Ко-ко" и "Кукареку"
#
# chiken_coco = Chiken()
# chiken_kykareky = Chiken()
#
# chiken_coco.name = 'Ко-ко'
# chiken_kykareky.name = 'Кукареку'
#
# print(f'Имя курочек - {chiken_coco.name} и {chiken_kykareky.name}')
#
# # Козы "Рога" и "Копыта"
#
# goat_horns = Goat()
# goat_hooves = Goat()
#
# goat_horns.name = 'Рога'
# goat_hooves.name = 'Копыта'
#
# print(f'Имя коз - {goat_horns.name} и {goat_hooves.name}')
#
# # Утка "Крыква"
#
# duck_krykva = Duck()
#
# duck_krykva.name = 'Крыква'
# print(duck_krykva.__dict__)
# print(f'Имя утки  - {duck_krykva.name}')
#
# duck_krykva.have_eggs()