import hashlib

string = input('Introduza o texto a ser gerado: ')

menu = int(input(''' ### MENU - Escolha o tipo de HASH ###
				1) MD5
				2) SHA1
				3) SHA256
				4) SHA512
				Digite o número do hash a ser gerado'''))
if menu == 1:
	resultado = hashlib.md5(string.encode('utf-8'))
	print('A hash MD5 da string é: ', string, 'e:', resultado.hexdigest())

elif menu == 2:
	resultado = hashlib.sha1(string.encode('utf-8'))
	print('A hash SHA1 da string é: ', string, 'e: ', resultado.hexdigest())
elif menu == 3:
	resultado = hashlib.sha256(string.encode('utf-8'))
	print('A hash SHA256 da string é: ', string, 'e: ', resultado.hexdigest())
elif menu == 4:
	resultado = hashlib.sha512(string.encode('utf-8'))
	print('A hash SHA512 da string é: ', string, 'e: ', resultado.hexdigest())
else:
	print('erro! Tente novamente...')	