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

# Добавляем элемент в конец списка
# list = [1, 2, 3]
# list_new = [4, 5, 6]
# general_list = list + list_new
# general_list.append('new item')
# print(general_list)

# Добавляем элемент в любое место списка (первым параметром указываем место куда хотим вставить элемент) (0 - это начало списка, 1 - вставить элемент на второе место в списке и т.д.)
# list = [1, 2, 3]
# list_new = [4, 5, 6]
# general_list = list + list_new
# general_list.insert(0, 'new item')
# general_list.insert(1, 'new item two')
# print(general_list)

# Удаление элементов из списка
#  