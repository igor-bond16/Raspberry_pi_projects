import RPi.GPIO as GPIO          
import adinput

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

while  True:
    command = raw_input("[Enter]:start A/D / [Q]:quit : ")
    if command.upper() == ("Q"):
        break
    
    cnt = adinput.adget()
    print("A/D count(0-1023) = %d" % cnt)
    
    v = cnt*3.3/1023
    print("Volt=%.3f V" % v)
    
    if(v==0):
        v = 0.01
        
    cm = (33.60 - v*4)/v
    print("Distance = %d cm" % cm)
    
GPIO.cleanup()