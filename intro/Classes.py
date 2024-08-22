### Этот файл был создан для практики написания классов в рамках лекции по классам в Нетологии
#
## Задача №1 "Ферма Дядюшки Джо"

class Goose:
   need_eat = 'Да'
   voice = 'Га-Га'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def have_eggs(self):
      val = input(f'Нужно ли собирать яйца у гуся {self.name}, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Яйца собраны у гуся {self.name}')
      else:
         print('Яйца собирать не нужно')

   def eat(self):
      val = input(f'Чем вы хотите покормить гуся {self.name}? Можно покрмить травой, комбикормом или сеном: ')
      if val in ('Травой', 'Комбикормом', 'Сеном'):
         self.weight = self.weight + 0.01
         print(f'Вы покрмили животное {val}, теперь вес {self.name} стал {self.weight}')
      else:
         print(f'Кормить {self.name} не нужно')

class Cow:
   need_eat = 'Да'
   voice = 'Муу'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def make_milk(self):
      val = input(f'Нужно ли подоить корову {self.name}, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Корова {self.name} подоена')
      else:
         print(f'Корову {self.name} доить ненужно')

   def eat(self):
      val = input(f'Чем вы хотите покормить корову {self.name}? Можно покрмить травой, комбикормом или сеном: ')
      if val in ('Травой', 'Комбикормом', 'Сеном'):
         self.weight = self.weight + 0.2
         print(f'Вы покрмили животное {val}, теперь вес {self.name} стал {self.weight}')
      else:
         print(f'Кормить корову {self.name} не нужно')

class Sheep:
   need_eat = 'Да'
   voice = 'Бее'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def сut(self):
      val = input(f'Нужно ли подстричь овцу {self.name}, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Овца {self.name} подстрижена')
      else:
         print(f'Овцу {self.name} стричь ненужно')

   def eat(self):
      val = input(f'Чем вы хотите покормить барашка {self.name}? Можно покрмить травой, комбикормом или сеном: ')
      if val in ('Травой', 'Комбикормом', 'Сеном'):
         self.weight = self.weight + 0.1
         print(f'Вы покрмили животное {val}, теперь вес {self.name} стал {self.weight}')
      else:
         print(f'Кормить овцу {self.name} не нужно')

class Chiken:
   need_eat = 'yes'
   voice = 'coco'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def have_eggs(self):
      val = input(f'Нужно ли собирать яйца у курочки {self.name}, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Яйца собраны у курочки {self.name}')
      else:
         print(f'У курочки {self.name} яйца собирать не нужно')

   def eat(self):
      val = input(f'Чем вы хотите покормить курочку {self.name}? Можно покрмить травой, комбикормом или сеном: ')
      if val in ('Травой', 'Комбикормом', 'Сеном'):
         self.weight = self.weight + 0.01
         print(f'Вы покрмили животное {val}, теперь вес {self.name} стал {self.weight}')
      else:
         print(f'Кормить курочку {self.name} не нужно')

class Goat:
   need_eat = 'yes'
   voice = 'mee'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def make_milk(self):
      val = input(f'Нужно ли подоить козу {self.name}, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Коза {self.name} подоена')
      else:
         print(f'Козу {self.name} доить ненужно')

   def eat(self):
      val = input(f'Чем вы хотите покормить козу {self.name}? Можно покрмить травой, комбикормом или сеном: ')
      if val in ('Травой', 'Комбикормом', 'Сеном'):
         self.weight = self.weight + 0.1
         print(f'Вы покрмили животное {val}, теперь вес {self.name} стал {self.weight}')
      else:
         print(f'Кормить козу {self.name} не нужно')


class Duck:
   need_eat = 'yes'
   voice = 'kryia'

   def __init__(self, name, weight, feature):
      self.name = name
      self.weight = weight
      self.feature = feature

   def have_eggs(self):
      val = input(f'Нужно ли собирать яйца у утки {self.name}, напишите Да или Нет: ')
      if val == 'Да':
         print(f'Яйца собраны у утки {self.name}')
      else:
         print(f'Яйца у утки {self.name} собирать не нужно')

   def eat(self):
      val = input(f'Чем вы хотите покормить утку {self.name}? Можно покрмить травой, комбикормом или сеном: ')
      if val in ('Травой', 'Комбикормом', 'Сеном'):
         self.weight = self.weight + 0.1
         print(f'Вы покрмили животное {val}, теперь вес {self.name} стал {self.weight}')
      else:
         print(f'Кормить козу {self.name} не нужно')

## Присваиваем значения классов объектам

# Гуси "Серый" и "Белый"
gray_goose = Goose('Серый', 2, 'Несет яйца')
white_goose = Goose('Белый', 2, 'Несет яйца')
# print(gray_goose.name, white_goose.name)
# gray_goose.have_eggs()
# gray_goose.eat()

# Корова Манька

cow_manya = Cow('Манька', 50, 'Дает молоко')
# cow_manya.make_milk()
# cow_manya.eat()
# print(cow_manya.name)

# Овцы Барашек и Кудрявый

sheep_barashek = Sheep('Барашек', 15, 'Дает шерсть')
sheep_curly = Sheep('Кудрявый', 15, 'Дает шерсть')
# sheep_barashek.сut(), sheep_barashek.eat()
# sheep_curly.сut(), sheep_curly.eat()
# print(sheep_barashek.name, sheep_curly.name)

# Курочки Ко-Ко и Кукареку

chiken_coco = Chiken('Ко-Ко', 3, 'Несет яйца')
chiken_kukareku = Chiken('Кукареку', 3, 'Несет яйца')
# chiken_coco.eat(), chiken_kukareku.eat()
# chiken_coco.have_eggs(), chiken_kukareku.have_eggs()
# print(chiken_coco.name, chiken_kukareku.name)

# Козы Рога и Копыта

goat_horns = Goat('Рога', 10, 'Дает молоко')
goat_hoofs = Goat('Копыта', 10, 'Дает молоко')
# goat_horns.eat(), goat_hoofs.eat()
# goat_horns.make_milk(), goat_hoofs.make_milk()
# print(goat_horns.name, goat_hoofs.name)

# Утка Кряква

duck_cryakva = Duck('Кряква', 3, 'Несет яйца')
# duck_cryakva.eat(), duck_cryakva.have_eggs()
# print(duck_cryakva.name)

### Считаем общий вес всех животных и вывести самого тяжелого животного

summary_weight = gray_goose.weight + white_goose.weight + cow_manya.weight + sheep_curly.weight + sheep_barashek.weight + chiken_coco.weight + chiken_kukareku.weight + goat_hoofs.weight + goat_horns.weight + duck_cryakva.weight
# print(f'Общий вес всех животных составляет - {summary_weight}кг')

list = [[gray_goose.name, gray_goose.weight], [white_goose.name, white_goose.weight], [cow_manya.name, cow_manya.weight], [sheep_curly.name, sheep_curly.weight], [sheep_barashek.name, sheep_barashek.weight], [chiken_coco.name, chiken_coco.weight], [chiken_kukareku.name, chiken_kukareku.weight], [goat_horns.name, goat_horns.weight], [goat_hoofs.name, goat_hoofs.weight], [duck_cryakva.name, duck_cryakva.weight]]

weight = 0
animal_name = ''
for name, weig in list:
   if weig > weight:
      weight = weig
      animal_name = name

# print(f'Животное, с самым большим весом - {animal_name}')

## Задача №2 "Аудиоколлекция"

class Track:

   def __init__(self, name, duration):
      self.name = name
      self.duration = duration

   def show(self):
      print(f'Название трэка {self.name}, длительность {self.duration} мин')


class Album:

   def __init__(self, name, group, tracks):
      self.name = name
      self.group = group
      self.tracks = tracks

   def get_tracks(self):
      print('Ниже быдет выведена информация по всем трэкам в альбоме')
      for track in self.tracks:
         track.show()

   def add_track(self, track):
      self.tracks.append(track)

   def get_duration(self):
      album_duration = 0
      for duration in self.tracks:
         album_duration += duration.duration
      print(f'Общая длительность альбома - {album_duration} мин')

# talling = Track('talling', 4)
# soul = Track('soul', 5)
# print(talling.name, talling.duration)

violator_tracks = [Track('Personal Jesus', 5), Track('Enjoy the Silence', 4), Track('Clean', 3)]
violator = Album('Violator', 'Depeche Mode', violator_tracks)

# Проверям методы класса
violator.add_track(Track('Оblivion', 5))
violator.get_tracks()
violator.get_duration()

# best = Album('best', 'madonna', talling.name)
# best.add_track()
# best.get_tracks()
# print(best.tracks)

