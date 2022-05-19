"""В файле содержится последовательность целых чисел. Элементы последовательности могут
принимать целые значения от 1 до 10 000 включительно. Найдите числа, которые удовлетворяют
следующим условиям:
− кратны 9, но не кратны 24 и 11;
− последняя цифра отлична от 4.
Найдите количество таких чисел и минимальное из них.
Ответ запишите в порядке, описанном выше, используя пробел между числовыми значениями."""
file = open("zadanie_17.txt") #открываем файл
buf = [] #пустой массив
for a in file.readlines(): #читаем каждую строку файла
	a = int(a) #меняем тип данных, переводим str в int
	if (a % 9 == 0 and a % 24 != 0 and a % 11 != 0): #проверка кратности и некратности
		"""
		
		"""
		if str(a)[-1] != "4": #Проверяем последнюю цифру, не забываем что это текст потому записываем "отличную" цифру в ковычках так как это текст  
			"""
			если присвоить текстовой переменной отрицательный индекс [-1] то мы пойдем с конца
			пример:
			a = "hello world"
			print(a[-1])

			output: d
			"""
			buf.append(a) #добавляем число в массив
print(len(buf),min(buf)) #ОТВЕТ: 816 9
"""
Считываем количество чисел в массиве с помощью функции len
и получаем минимальное число с помощью функции min
(помимо min есть еще и функция max которая получает максимальное число )
a = [1,2,3]
print(min(a),max(a))
output: 1 3
---------------------------------------------------------------------------------------------\
len позволяет считать не только количество объектов в массиве но и количество символов в слове
a = "hello world"
print(len(a))
output: 11
----------------------------------------------------------------------------------------------\
"""