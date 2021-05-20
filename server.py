from socket import *
from _thread import *
import threading



def recieved_thread(c):	
	while True:
		val = c.recv(500)
		print("client: ", val.decode("utf=8"))

def client_thread(session):
	start_new_thread(recieved_thread, (session,))
	while True:
		session.send(input("server: ").encode("utf=8"))

socket_file_discrptor=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7000
socket_file_discrptor.bind((host,port))
socket_file_discrptor.listen(5)

while True:
	session, client_info = socket_file_discrptor.accept()
	print("connedcted device ip: " + client_info[0])
	start_new_thread(client_thread, (session, ))
session.close()