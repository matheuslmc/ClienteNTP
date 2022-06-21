import socket
from random import random

if __name__ == "__main__":

	HOST = 'localhost'
	PORT = 7777

	senha = int(random() * 1000)
	print(F"SENHA: {senha}\n")

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))
	client.send(f'Coloque a {senha}.encode())
	response = client.recv(4096)
	print(response.decode())
	input("Digita qualquer tecla para sair")
