import socket
import time
from threading import Thread


host = socket.gethostname()
port = 25072

mySocket = socket.socket()
mySocket.bind((host,port))

mySocket.listen(1)
conn, addr = mySocket.accept()
print("Connection From: "+ str(addr))

def recieve_data():
    while True:
	    data = conn.recv(1024).decode()
	    
	    #print("from conected user: "+str(data))
	    #data = str(data).upper()
	    print("Recieved from user: "+str(data))

def send_data():
	while True:
		data = input("?")
		conn.send(data.encode())

#conn.close()


if __name__ == '__main__':
	thread1 = Thread(target = recieve_data)
	thread2 = Thread(target = send_data)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	conn.close()
    
