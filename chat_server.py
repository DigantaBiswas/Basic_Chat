import socket
import time
import webbrowser
from threading import Thread
from logic import match_with_url


host = socket.gethostname()
port = 25002

mySocket = socket.socket()

mySocket.bind((host,port))

mySocket.listen(1)
conn, addr = mySocket.accept()
print("Connection From: "+ str(addr))


def recieve_data():
    while True:
	    data = conn.recv(1024).decode()
	    print("Recieved from user: "+str(data))
	    #time.sleep(2)
	    match_with_url(data)



def send_data():
	while True:
		data = input("?")
		conn.send(data.encode())
		if data == "q":
			conn.close()




if __name__ == '__main__':
	thread1 = Thread(target = recieve_data)
	thread2 = Thread(target = send_data)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	conn.close()
    
