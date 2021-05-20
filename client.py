from socket import *
from _thread import *
import threading

socket_file_discriptor = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000

def recieved_thread(c):
	while True:
		val=c.recv(500)
		print(val.decode("utf=8"))

socket_file_discriptor.connect((host, port))
start_new_thread(recieved_thread, (socket_file_discriptor,))

while True:
    socket_file_discriptor.send(input("client: ").encode("utf=8"))






