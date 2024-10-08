### Этот файл был создан для практики написания энкапсуляции, наследования и полиморфизма в рамках лекции ООП: наследование, инкапсуляция и полиморфизм в Нетологии

# Задача №1 "Ферма Дядюшки Джо". Продолжение.

class Animal:
    need_eat = 'Да'
    def __init__(self, name, voice, weight, features):
        self.name = name
        self.voice = voice
        self.weight = weight
        self.features = features

    def eat(self):
        val = input(f'Чем вы хотите покормить животное {self.name}? Можно покрмить травой, комбикормом или сеном: ')
        if val in ('Травой', 'Комбикормом', 'Сеном'):
            self.weight = self.weight + 0.01
            print(f'Вы покрмили животное {val}, теперь вес {self.name} стал {self.weight}')
        else:
            print(f'Кормить животное {self.name} не нужно')

class Goose(Animal):
    def __init__(self, name, voice, weight, features):
        self.name = name
        self.voice = voice
        self.weight = weight
        self.features = features

    def have_eggs(self):
        val = input(f'Нужно ли собирать яйца у гуся {self.name}, напишите Да или Нет: ')
        if val == 'Да':
            print(f'Яйца собраны у гуся {self.name}')
        else:
            print('Яйца собирать не нужно')

goose_test = Goose('Гусь', 'Га-га', 2, 'Несет яйца')
# print(dir(goose_test), goose_test.__dict__)

# for method in dir(goose_test):
#     print(method)

## Задача №2 "Аудиоколлекция". Продолжение.

class Track:

   def __init__(self, name, duration):
      self.name = name
      self.duration = duration

   def __str__(self):
      return f'Название трэка {self.name}, длительность {self.duration} мин'


class Album:

   def __init__(self, name, group, tracks):
      self.name = name
      self.group = group
      self.tracks = tracks

   # def __str__(self):
   #    print('Ниже быдет выведена информация по всем трэкам в альбоме')
   #    for track in self.tracks:
   #        print(track)
   #    return f'инфа'

   def add_track(self, track):
      self.tracks.append(track)

   def __repr__(self):
       val = []
       for track in self.tracks:
           val.append(f'{track.name}-{track.duration}')
       return f'Группа: {self.group}\nАльбом: {self.name}\nТреки:\n     {val}'.replace(",", '\n    ').replace('[','').replace("'",'').replace(']','')

   def get_duration(self):
      album_duration = 0
      for duration in self.tracks:
         album_duration += duration.duration
      print(f'Общая длительность альбома - {album_duration} мин')

track1 = Track('Personal Jesus', 5)
track2 = Track('Enjoy the Silence', 4)
track3 = Track('Clean', 3)

# violator_tracks = [Track('Personal Jesus', 5), Track('Enjoy the Silence', 4), Track('Clean', 3)]
violator_tracks = [track1, track2, track3]
violator = Album('Violator', 'Depeche Mode', violator_tracks)

# print(track2)

# Проверям методы класса
# violator.add_track(Track('Оblivion', 5))
# print(violator_tracks)
print(violator)
# violator.get_duration()
---end---