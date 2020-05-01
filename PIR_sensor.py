import RPi.GPIO as GPIO
import time

channel = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)   

def callback(channel):
    print('Motion Detected')
    
    time.sleep(2)
    
print("Motion Sensor Alarm (CTRL + C to exit)")
time.sleep(3)
print("Ready")

try:
    GPIO.add_event_detect(channel,GPIO.BOTH,callback=callback)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
