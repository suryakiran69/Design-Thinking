import serial
import re
import time
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print("------->WASTE MANAGEMENT SYSTEM_IoT BASED<-------")
time.sleep(2)
print("")
print("CONNECTING TO SERVER......!!!!")
time.sleep(2)
email = "coderinfo69@gmail.com"
server.login(email,'pwff hurl zftv kwjb')
print("SERVER_CONNECTED_SUCCESSFULLY")
print("")
time.sleep(1)
print("ACTIVATING SERIAL PORT......!!!!")
ser = serial.Serial('COM10', 9600)
time.sleep(2)
print("SERIAL_PORT_ACTIVATED")
print("")
time.sleep(1)
print("DECRYPTING HEIGHT ......!!!!")
print("")
time.sleep(2)
while True:
    string = ser.readline().decode().strip()
    height = re.search(r'\d+', string)
    if height:
        height_final = int(height.group())
        h2 = height_final
        print("HEIGHT OF THE WASTE IS ",h2,"CM")
        time.sleep(0.5)
        if 0 < height_final < 5:
            print("")
            time.sleep(2)
            print("DUST BIN IS FULL.PLEASE COME AFTER SOME TIME")
            time.sleep(2)
            msg="Your dustbin is going to fill \n now present height is "+str(height_final)+" cm"
            print("SENDING MAIL......!!!!")
            server.sendmail(email,'suryakiran3849@gmail.com',msg)
            time.sleep(3)
            print("")
            print("MAIL_SENT_SUCCESSFULLY___ :)")
            print("")
            time.sleep(2)
            print("KEEP SMILING :) \n THANK_YOU")
            time.sleep(10)
    else:
        print("No numeric value found in the input string:", string)
