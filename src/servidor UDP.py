import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('socket criado com sucesso')


host = 'localhost'
port = 5432


s.bind((host, port))
mensagem = 'Servidor: Olá cliente, tudo ok?'


while 1:
	dados, endereco = s.recvfrom(4096)

	if dados == True:
		print('Servidor enviando mensagem...')
		s.sendto(dados + (mensagem.encode()), end)