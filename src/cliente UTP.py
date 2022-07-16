import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket Criado com Sucesso!')

host = 'localhost'
porta = 5432
mensagem = 'Testando servidor'

try:
	print('Cliente: ' + mensagem)
	s.sendto(mensagem.encode(), (host, 5433))
	
	dados, servidor = s.recvfrom(4065)	
	dados = dados.decode()
	print("Cliente: " + dados)
finally:
	print('Cliente: Fechando a conexão')
	s.close()