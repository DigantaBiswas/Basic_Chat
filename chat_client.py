import socket
import re
import time
import webbrowser
from threading import Thread
from logic import match_with_url

host = socket.gethostname()
port = 25002

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

		#time.sleep(2)
		match_with_url(data)


if __name__ == '__main__':

	thread1 = Thread(target = recieve_data)
	thread2 = Thread(target = send_data)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	mySocket.close()