import socket
import sys

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, )

	except socket.error as e:
		print('A conexão falhou!')
		print('Erro: {}'.format(e))
		sys.exit()
	
	print('Socket criado com sucesso')

	Host_Target = input('Introduza o Host ou Ip a ser conectado')
	Port_Target = input('Introduza a porta a ser conectada')
	try:
		s.connect((Host_Target, int(Port_Target)))
		print("Cliente TCP connectado com sucesso no Host: " + Host_Target + "e na porta: " + Port_Target)
		s.shutdown(2)
	except socket.error as e:
		print('Não foi possível connectar no Host: ' + Host_Target + "-- Porta: " + Port_Target)
		print('Error: {}'.format(e))
		sys.exit()

if __name__ == "__main__":
	main()	