import itertools

string = input("String a ser permutato: ")

resultado = itertools.permutations(strting, len(string))

for i in resultado:
	print(''.join(i))
