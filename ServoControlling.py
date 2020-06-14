'''
                                                 
### 20,November,2018                                                 ###
### By : Reza Amini , University of Tabriz                           ###
########################################################################
### Controlling Servo via python                                     ###
### Via Rpi                                                          ###

'''

import RPi.GPIO as GPIO
import time

servo = 3
'''
pin 9 used As GND
5v Battery supplied Power(instead of pin 2 or 4)
'''

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)


'''
frequency pf pwf =50hz
T=20ms

'''

pwm = GPIO.PWM(servo, 50)
''' pwm.start("duty cycle") '''
pwm.start(5)
key=0
print("PRESS \'e\' for exit\n\n\n")
while key!='e':
      
    key=input('Enter duty cycle: ')
    pwm.ChangeDutyCycle(int(key))
    
    
if key=='e':
        
    GPIO.cleanup()
    print('EXIT')
        




