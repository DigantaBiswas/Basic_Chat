import socket
from threading import Thread

host = socket.gethostname()
port = 25072

mySocket = socket.socket()
mySocket.connect((host,port))

#message = input("?")

def send_data():
	while True:
		message = input("?")
		if message =='q':
			break
		mySocket.send(message.encode())
def recieve_data():
	while True:
		data = mySocket.recv(1024).decode()
		print('Recieve from server: '+ data)
#mySocket.close()

if __name__ == '__main__':

	thread1 = Thread(target = recieve_data)
	thread2 = Thread(target = send_data)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	mySocket.close()