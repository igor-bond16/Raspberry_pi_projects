import RPi.GPIO as GPIO
import time
import datetime
import picamera

channel = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)


def callback(channel):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        camera.start_preview()
        now = datetime.datetime.now()
        time.sleep(5)
        camera.stop_preview()
        camera.capture(str(now)+'.jpg')
    time.sleep(3)
        
    
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