# i = 0
# while i < 3000:
#     print(i)
#     i += 1

#                                                                        Строки

# Функция .format(тут указываем переменные, или сразу значения (строки, цифры, символы)), тут {} указываем ключи либо номер переменной (отсчет идет с 0) из () ,
# если ничего не указано то переменные будут браться по порядку .

# Пример с номером переменной. (отсчет идет с 0)
# name = 'Kirill'
# age = 33
# name_and_age = 'My name is {0}. I\'m {1} years old'.format(name, age)
# print(name_and_age)

# Пример с ключом переменной.
# weeks_days = 'There are 7 days in a week: {su}, {mo}'.format(su = 'Sunday', mo = 'Monday')
# print(weeks_days)

# Если мы не указали номер или ключ переменной то она берется по порядку.
# weeks_days_2 = 'There are 7 days in a week: {}, {}'.format('Sunday', 'Monday')
# print(weeks_days_2)

# Если нужно отформатировать строку по кол-во символов то после номера переменной через двоеточие (:) указываем кол-во символов в строке, и если число с точкой то
# ставим знак точки(.) и после указываем кол-во символов после точки и ставим букву f .
# float_result = 1000 / 7
# print(float_result)
# print('The result is devision is {0:10.3f}'.format(float_result))

# print('''
#     {0:20.2f} {1:20.2f} {2:20.2f}
#     {3:20.2f} {4:20.2f} {5:20.2f}
# '''.format(1.12345, 1.54321, 33.156897, 222.3333, 5555.4874875, 4564564545645465.878978789454567487545486))

# Если в начале строки указать букву f то данные из переменных будут переданы в фигурные скобки.
# name = 'Kirill'
# age = 33
# name_and_age = f'My name is {name}. I\'m {age} years old'
# print(name_and_age)

# Старый способ: указываем знак процента(%) далее ставим букву s если у нас буквенные данные, или букву d если цифровые данные. ЭТОТ СПОСОБ НЕ РЕКОМЕНДУЕТСЯ.
# name = 'Kirill'
# age = 33
# name_and_age = 'My name is %s. I\'m %d years old' % (name, age)
# print(name_and_age)

#                                                                       Списки
# Кол-во элементов в списке
# list = [3, 4, 10.1888]
# print(len(list))

# Получаем элемент из списка отсчет идет с 0
# list = [3, 4, 10.1888]
# print(list[2])

# Получаем элементы из списка
# list = [3, 4, 10.1888]
# some_list = list[:2]
# print(some_list)

# Изменяем элемент в списке
# list = [3, 4, 10.1888]
# list[2] = 'hi'
# print(list)

# Слияние списков
# list = [1, 2, 3]
# list_new = [4, 5, 6]
# general_list = list + list_new
# print(general_list)

# Добавляем элемент в конец списка .append()
# list = [1, 2, 3]
# list_new = [4, 5, 6]
# general_list = list + list_new
# general_list.append('new item')
# print(general_list)

# Добавляем элемент в любое место списка .insert (первым параметром указываем место куда хотим вставить элемент) (0 - это начало списка, 1 - вставить элемент на второе место в списке и т.д.)
# list = [1, 2, 3]
# list_new = [4, 5, 6]
# general_list = list + list_new
# general_list.insert(0, 'new item')
# general_list.insert(1, 'new item two')
# print(general_list)

# Удаление элементов из списка .pop (по умолчанию удаляется первый элемент с конца) указываем номер элемент который нужно удалить
# list = [1, 2, 3]
# list.pop(0)
# print(list)

# Если при удаление элемента из списка, создать новую переменную там будет удаленный элемент, т.е. при использование метода .pop возврашается удаленный элемент 
# list = [1, 2, 3]
# deleted_item = list.pop(1)
# print(deleted_item)

# Метод .remove удаляет элемент по значению (удаляется первый попавшийся элемент) так же удаленный элемент не возврашается
# list = [1, 2, 3, 4, 5, 6, 7, 1]
# deleted_item = list.remove(1) # удаленный элемент не вернется
# print(list)
# print(deleted_item)

# Метод сортировки листа .sort (этот метод ничего не возврашает)
# list = [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5, -6, -7]
# letter_list = ['c', 'd', 'a', 'b']
# list.sort()
# letter_list.sort()
# print(list)
# print(letter_list)

# Метод .reverse сортирует список в обратном порядке
# list = [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5, -6, -7]
# letter_list = ['c', 'd', 'a', 'b']
# list.reverse()
# letter_list.reverse()
# print(list)
# print(letter_list)

#                                                                                Словари
# Словари это не упорядоченные последовательности различных объектов с доступом по ключу

# dict = {'money': 5000, 'rubli': 10, 'dollar': 900} # словари пишутся в фигурных скобках сначала идет ключ далее его значение
# print(dict['rubli']) # получаем данные по ключу
# dict['tugriki'] = 1800 # добавляем элемент в словарь
# print(dict)
# dict['dollar'] = 9999 # изменяем данные так же по ключу
# print(dict)
# del dict ['tugriki'] # удаляем данные по ключу, если не укажем ключ то тогда удалим всю переменную
# print(dict)
# dict.clear() # очишаем переменную со словарем
# print(dict)

# person = {
#     'first_name': 'Kirill',
#     'last_name': "Neizvestnyi",
#     'age': 33,
#     'hobbies': ['footbal', 'singing', 'photo'], # создаем список с доступом по ключу
#     'children': {'son': 'Ilya', 'daugter': 'Alena'} # создаем словарь с доступом по ключу
# }
# print(person['age'])
# print(person['hobbies'])
# hob = person['hobbies'] # получаем все хобби в переменную
# print(hob[2]) # получаем конкретное значение из переменной
# print(person['hobbies'] [2]) # получаем сразу нужное значение
# print(person['children'] ['son']) # получаем сразу нужное значение по ключу
# person['car'] = 'porsche' # добавляем значение
# person['car'] = {'porsche': 'the best'} # добавляем значение
# person['age'] = 30 # изменяем данные
# person['hobbies'] [0] = 'basketball' # меняем значение по индексу
# print(person.keys()) # получаем все ключи
# print(person.values()) # получаем все значения
# print(person.items()) # получаем все элементы в виде списка
# print(person)

#                                                                     Tuple - Кортежи (immutable - не изменяемое содержимое)
# tuple_1 = (1, 2, 3)
# tuple_2 = ('one', 'hello')
# tuple_3 = (3, 2.3, 'three')

# tup = (tuple_1[0], 3, tuple_1[2]) # взяли первое значение из переменной + добавили "3" + третье значение
# print(tup)

# print(tuple_1[1])
# print(tuple_2)
# print(tuple_3)

# person_tuple = ('Jonn', 'Smith', 1988)
# a, b, c = person_tuple # распаковываем кортеж в переменные
# print(a, b, c)

# # .count() служит для определения сколько раз встречается значение в кортеже 
# t1 = (1, 2, 3, 4, 5, 1, 7, 9, 'privet', 'privet')
# print(t1.count(1)) # .count(1)  в скобках указываем значение кол-во которых нужно посчитать
# print(t1.count('privet'))
# greetings_tuple = ('hi', 'hello', 'hi', 'hey', 'hi')
# print(greetings_tuple.count('hi'))

# print(t1.index(5)) # .index() получаем индекс значения в кортеже (порядковый номер значения в кортежи)
# print(greetings_tuple.index('hi')) # если в кортеже содержиться более одного индекса, то будет показан первый по порядку индекс


#                                   Sets - Множества (неупорядоченная коллекция уникальных элементов) (в множестве не может быть двух одинаковых элементов)

# rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
# print(rainbow_colors)
# print(type(rainbow_colors)) # получаем класс элемента

# empty_set = set() # что бы создать пустое множество пишем set(), если напишем empty_set = {} то будет создан словарь
# print(type(empty_set))

# number_list = [10, 21, 32, 47, 53] # список
# text_tuple = ('audi', 'porshe', 'bmw') # кортеж
# set_list = set(number_list) # преобразовываем список в множество
# set_tuple = set(text_tuple) # преобразовываем кортеж в множество
# print(set_list)
# print(set_tuple)

# set_list.add(333) # добавляем элемент в множество
# set_tuple.add('hello') # добавляем элемент в множество
# print(set_list)
# print(set_tuple)
# # если добавить повторяющийся элемент в множество то он не будет добавлен

# # если в кортеже или в списке есть повторяющиеся элементы, при преобразовние в множество эти элементы остануться в единствинном экземпляре
# number_list = [10, 21, 32, 47, 53, 3, 3, 3, 3] # список
# text_tuple = ('audi', 'porshe', 'bmw', 'hi', 'hi', 'hi') # кортеж
# set_list = set(number_list) # преобразовываем список в множество
# set_tuple = set(text_tuple) # преобразовываем кортеж в множество
# print(set_list)
# print(set_tuple)

# set_list.pop() # удаляем случайный элемент из множества (элемент возвращается)
# print(set_list)
# set_list.remove(10) # удаляем конкретный элемент из множества (элемент не возвращается)
# set_tuple.remove('audi') # удаляем конкретный элемент из множества (элемент не возвращается) (при попытке удалить элемент которо нет - будет ошибка)
# print(set_list)
# print(set_tuple)

# number_list = [10, 21, 32, 47, 53, 3, 3, 3, 3] # список
# text_tuple = ('audi', 'porshe', 'bmw', 'hi', 'hi', 'hi') # кортеж
# set_list = set(number_list) # преобразовываем список в множество
# set_tuple = set(text_tuple) # преобразовываем кортеж в множество
# a = set_list.pop() # при удалении методом .pop() элемент возвращается при удалении
# b = set_tuple.remove('audi') # при удалении методом .remove() элемент не возвращается при удалении
# set_tuple.discard('audi') # при удалении методом .discard() не будет ошибки если элемента не существует, в отличие от .remove()
# print(a)
# print(b)
# print(set_tuple)

# set_tuple.clear() # методом .clear() можно удалить все элементы из множества
# print(set_tuple)

#                                                 Boolen and comarison operators - Булин значения (Истина или ложь (True или False)) и операторы сравнения

# print(1 < 2) # оператор сравнения первое число меньше чем второе?
# print(type(True)) # узнаем тип данных
# print(type(False))
# print('Hello' == 'hello') # оператор сравнения равно ли первое значение второму
# print(1 == 1) # оператор сравнения равно ли первое значение второму
# print(1 != 1) # оператор сравнения НЕ равно ли первое значение второму


# a = 82 // 3 ** 2 % 7
# print(a)
# a = 300
# h = a // 60
# print(h)
# print("Привет")

# По умолчанию команда print() принимает несколько аргументов (параметров), выводит их через один пробел, после чего ставит перевод строки.
#  Это поведение можно изменить, используя необязательные именованные параметры sep (separator, разделитель) и end (окончание)
# Если перевод строки делать не нужно или требуется указать специальное окончание, то следует явно указать значение для параметра end.

# Последовательность символов \n называется управляющей последовательностью и задает перевод строки.
#  Значения по умолчанию у параметров sep и end следующие:
#  sep=' '   # пробел
#  end='\n'  # перевод строки

# Для того, чтобы преобразовать строку к целому числу, мы используем команду int().

**	Возведение в степень, %	Остаток от деления, //	Целочисленное деление.