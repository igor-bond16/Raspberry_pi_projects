#import RPi.GPIO as GPIO
#from gpiozero import MCP3008
import time
import spidev

#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)


#try:
#    while True:
#        pot = MCP3008(channel=0,device=0)
#        ad = (pot.value * 5.0)
#        print("A/D="+str(ad))

#        v = ad*3.3/1023
#        print("Volt = {0:.3f}".format(v))
        
#        if(v == 0):
#            v = 0.01

#        water = 5.0*100*ad%1023
#        time.sleep(1)
#except KeyboardInterrupt:
#    pass

#GPIO.cleanup()
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
spi.bits_per_word=8
dummy = 0xff
start = 0x47
sgl = 0x20
ch0 = 0x00
ch1 = 0x10
msdf = 0x08

def measure(ch):
    ad = spi.xfer2([(start+sgl+ch+msdf),dummy])
    val = ((((ad[0] & 0x03) << 8)+ad[1])*3.3)/1023
    return val

try:
    while 1:
        mes_ch0 = measure(ch0)
        mes_ch1 = measure(ch1)
        print('ch0=%2.2f' % mes_ch0,'[V]','ch1=%2.2f' %mes_ch1,'[V]')
        time.sleep(1)
except KeyboardInterrupt:
    pass

spi.close()