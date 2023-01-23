import socket, threading
player = 1
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = '172.31.128.11'
port = 12333
error = '0'
sock.bind((ip, port))
print('server started, ERRORS = ', error)

sock.listen()

class clientTh(threading.Thread):
	def __init__(self, adres, user):
		threading.Thread.__init__(self)
		self.csocket = user
		print ("Новое подключение: ", adres)
	def run(self):
		msg = ''
		while True:
			data = self.csocket.recv(4096)
			msg = data.decode()
			if msg != '':
				print(msg)
			else:
				print('отключение!')
				break

while True:
	if player != 5:
		user, adres = sock.accept()
		newtheard = clientTh(adres, user)
		newtheard.start()
