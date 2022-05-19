"""Логическая функция F задаётся выражением (x ≡ z ) ∨ (x → (y ∧ z)) v w.
Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности
функции F.
Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w"""
#---------------------------------------------------------------------------------------------

print("x y z w F")
for x in range(0,2): #перебор значений для x
	for y in range(0,2): #перебор значений для y
		for z in range(0,2): #перебор значений для z
			for w in range(0,2): #перебор значений для w
				"""
				._________.
				|?|?|?|?|F|
				|0|0|0|1|0|
				|1|0|0|1|0|
				'¯¯¯¯¯¯¯¯¯'
					≡ - a == b         | x ≡ y                          | if (x == y):
					∨ - a or b         | (x ≡ y)∨ z                     | if ((x == y) or z):
					∧ - a and b        | ((x ≡ y)∨ z) ∧ (x ∨ z)         | if (((x == y) or z) and (x or z)):
					→ - not(a) or b    | ((x ≡ y)∨ z) ∧ (x ∨ z) → w     | if (((x == y) or z) and not(x or z) or w):
					¬ - not(a)         | ((¬x ≡ y)∨ z) ∧ (¬x ∨ z) → ¬w  | if (((not(x) == y) or z) and not(not(x) or z) or not(w)):
				"""
				#      (x ≡ z ) ∨ (x → (y ∧ z)) v w. {условие}
				if not((x == z) or (not(x) or (y and z)) or w):
					print(x,y,z,w,0)
					#ОТВЕТ: yzwx



