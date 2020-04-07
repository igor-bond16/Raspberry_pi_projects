import time
import RPi.GPIO as GPIO
from gpiozero import MCP3008 as mcp

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def adget():
    cs = 18
    din = 22
    clk = 26
    dout = 24
    
    GPIO.setup(clk,GPIO.OUT)
    GPIO.setup(cs,GPIO.OUT)
    GPIO.setup(dout,GPIO.IN)
    GPIO.setup(din,GPIO.OUT)
    
    GPIO.output(cs,True)
    GPIO.output(clk,False)
    time.sleep(0.001)
    GPIO.output(cs,False)
    
    txdat = 0b0110100000000000
    rxdat = 0
    
    bitmask = (1<<15)
    while(bitmask != 0 ):
        if(txdat & bitmask):
            GPIO.output(din,True)
        else:
            GPIO.output(din,False)
            
        time.sleep(0.001)
        GPIO.output(clk,True)
        
        if(GPIO.input(dout)==True):
            rxdat = rxdat | bitmask
            
        time.sleep(0.001)
        GPIO.output(clk,False)
        bitmask = bitmask>>1
        
    GPIO.output(cs,True)
    if(rxdat & (1<<10)):
        print("format error")
            
    rxdat = rxdat & 1023
    return rxdat