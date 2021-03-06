"""
У исполнителя Калькулятор три команды, которым присвоены номера:
• прибавь 1
• прибавь 2
• прибавь предыдущее
Первая команда увеличивает число на экране на 1, вторая увеличивает это число на 2, третья
прибавляет к числу на экране число, меньшее на 1 (к числу 3 прибавляется 2, к числу 11
прибавляется 10 и т. д.). Программа для исполнителя – это последовательность команд. Сколько
существует программ, которые число 2 преобразуют в число 9?
"""

def F(x,y):
	#----ОСНОВНОЙ ШАБЛОН---- Бывают и траектории, та еще залупа
	if x > y: #or y == N   | Врагу не пожелаешь задачу на ЕГЭ
		return 0 #     | с траекториями но я их разберу
	if x == y: #           | 
		return 1 #     |
	#-----------------------
	return F(x,y-1) + F(x,y-2) + F(x,(y+1)/2) 
	"""
	Создаем рекурсивные функции в которые вкладываем отрицательные команды
	x никогда не изменяется!
	передаем его в функцию снова и снова

	прибавь 1 - вычитаем 1
	умножь на 2 - раздели на 2
	к примеру:
		• прибавь 1
		• прибавь 4
		• прибавь 5
	РЕШЕНИЕ:
	F(x,y-1) + F(x,y-4) + F(x,y-5)

	"""
print(F(2,9)) #Вызываем функцию
#ОТВЕТ 57

#-----ЗАДАЧА НА ТРАЕКТОРИИ)))-----#
"""
Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть две
команды, которым присвоены номера:
1. Прибавь 1
2. Умножь на 2
3. Умножь на 2 и прибавь 1
Первая команда увеличивает число на 1, вторая – вдвое, третья делает умножает на два и прибавляет
1. Сколько существует таких программ, которые исходное число 10 преобразуют в число 100 и при 
 этом траектория вычислений программы содержит число 65?

"""
def Z(x,y):
	#----ОСНОВНОЙ ШАБЛОН---- А вот и траектории
	if x > y:# or y == N   | ЕСЛИ НАДО УБРАТЬ КАКОЕ ТО КОНТКРЕТНО ЧИСЛО ИЗ ПОСЛЕДОВАТЕЛЬНОСТИ 
		return 0 #     | Структура or y == число таким образом мы избавляемся от ненужного числа
	if x == y: #           | 
		return 1 #     |
	#-----------------------
	if y % 2 == 0 and (y - 1) % 2 != 0:
		return Z(x,y-1) + Z(x, y // 2)

	if (y - 1) % 2 == 0 and y % 2 != 0:
		return Z(x,y-1) + Z(x, (y - 1) // 2)

	if y % 2 == 0 and (y - 1) % 2 == 0:
		return Z(x,y-1) + Z(x, y // 2) + Z(x,(y - 1) // 2)
	#-----------------------
	return Z(x,y-1)
print(Z(10,65)*Z(65,100)) #умножаем траектории
#от 10 до 65 и от 65 до 100 по условию задания
#ОТВЕТ 229

#-----ЗАДАЧА НА ТРАЕКТОРИИ С ИСКЛЮЧЕНИЯМИ)))-----#
"""
Исполнитель Вычислитель преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:

1.Прибавить 1
2.Умножить на 2

Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
Программа для Вычислителя— это последовательность команд. Сколько существует программ,
для которых при исходном числе 1 результатом является число 22 и при этом траектория 
вычислений содержит число 10 и не содержит числа 15?


"""
def B(x,y):
	#----ОСНОВНОЙ ШАБЛОН---- А вот и траектории
	if x > y or y == 15: # | ПРИШЛО ТВОЕ ВРЕМЯ ЗАКОММЕНТИРОВАННОЕ УСЛОВИЕ!
		return 0 #     | 
	if x == y: #           | 
		return 1 #     |
	#-----------------------
	if y % 2 == 0:
		return B(x,y-1) + B(x, y // 2)
	return B(x,y-1)
print(B(1,10) * B(10,22)) #умножаем траектории
#ОТВЕТ 28 :)

