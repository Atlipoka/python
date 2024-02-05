# Домашнее задание к лекции 2.«Условные конструкции. Операции сравнения»
## Задача №1
Задачи на [hackerrank](https://www.hackerrank.com/):<br>
Решить задачу на hackerrank ["Python If-Else"](https://www.hackerrank.com/challenges/py-if-else/problem.)

## Задача №2
На лекции мы рассматривали пример для военкомата. Сейчас мы знаем про его рост. Расширить это приложение следующими условиями:

Проверка на возраст призывника.<br>
Количество детей.<br>
Учится ли он сейчас.
## Задание №3
Разработать приложение для определения знака зодиака по дате рождения.
Пример:
````
Введите месяц: март
Введите число: 6

Вывод:
Рыбы
````
# Решение

## Задача №1

https://www.hackerrank.com/challenges/py-if-else/problem

## Задача №2

````
# variables block
height = int(input('Введите рост: '))
age = int(input('Введите возраст: '))
children = int(input('Введите количество детей: '))


# block code
if (age < 18) or (age > 27):
  print('Не призывной возраст')
else:
  if (age >= 18) or (age <= 27):
    if children >= 2:
      print('Во дает, когда успел столько детей сделать...')
    else:
      if height < 170:
        print('В танкисты')
      elif height < 185:
        print('На флот')
      elif height < 200:
        print('В десантники')
      else:
        print('В другие войска')
````

## Задача №3

````
# variables block
month = input('Введите месяц: ')
day = int(input('Введите число: '))

# block code
if month == 'Январь':
  if day < 20:
    print('Вывод:', 'Козерог')
  elif day >= 20:
    print('Вывод:', 'Водолей')
if month == 'Февраль':
  if day <= 19:
    print('Вывод:', 'Водолей')
  elif day >= 20:
    print('Вывод:', 'Рыбы')
if month == 'Март':
  if day <= 20 :
    print('Вывод:', 'Рыбы')
  elif day >= 21:
    print('Вывод:', 'Овен')
if month == 'Апрель':
  if day <= 19:
    print('Вывод:', 'Овен')
  elif day >= 20:
    print('Вывод:', 'Телец')
if month == 'Май':
  if day <= 20:
    print('Вывод:', 'Телец')
  elif day >= 21:
    print('Вывод:', 'Близнецы')
if month == 'Июнь':
  if day <= 20:
    print('Вывод:', 'Близнецы')
  elif day >= 21:
    print('Вывод:', 'Рак')
if month == 'Июль':
  if day <= 22:
    print('Вывод:', 'Рак')
  elif day >= 23:
    print('Вывод:', 'Лев')
if month == 'Август':
  if day <= 22:
    print('Вывод:', 'Лев')
  elif day >= 23:
    print('Вывод:', 'Дева')
if month == 'Сентябрь':
  if day <= 22:
    print('Вывод:', 'Дева')
  elif day >= 23:
    print('Вывод:', 'Весы')
if month == 'Октябрь':
  if day <= 23:
    print('Вывод:', 'Весы')
  elif day >= 24:
    print('Вывод:', 'Скорпион')
if month == 'Ноябрь':
  if day <= 22:
    print('Вывод:', 'Скорпион')
  elif day >= 23:
    print('Вывод:', 'Стрелец')
if month == 'Декабрь':
  if day < 22:
    print('Вывод:', 'Стрелец')
  elif day >= 21:
    print('Вывод:', 'Козерог')
````
