"""
Значение арифметического выражения: −21^4 + 4^16 − 16^3 + 4^2
записали в системе счисления с основанием
4. Сколько цифр 3 содержится в этой записи?

"""
var = -2**14+4**16-16**3+4**2 #записываем выражение
newvar = "" #создаем пустой словарь
while var > 0: #цикл пока выражение больше нуля 
	newvar = str(var % 4) + newvar #| Перевод из десятичной
	var //= 4                      #| в четвертичную

"""-------------------------------------------
           -АЛГОРИТМ ПЕРЕВОДА-
	новое_значение = str(выражение % система_счисления) + новое_значение
	выражение //= система_счисления
   -------------------------------------------
"""
print(newvar.count("3"), newvar) #считаем количество троек по условию задачи