import RPi.GPIO as GPIO
import tkinter as tk

pinlist = [2,3,4,17]
GPIO.setmode(GPIO.BCM)
root = tk.Tk()

label = tk.Label(root,text='Smart Home')
label1 = tk.Label(root,text='Light is off')
label2 = tk.Label(root,text='Com[uter is off')
label3 = tk.Label(root,text='PS4 is off')
label4 = tk.Label(root,text='Security System is off')
label.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()

for i in pinlist:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.HIGH)
    
def Light():
    GPIO.output(2,GPIO.LOW)
    label1.config(text='Light is on')
    
def Computer():
    GPIO.output(3,GPIO.LOW)
    label2.config(text='Computer is on')
    
def PS():
    GPIO.output(4,GPIO.LOW)
    label3.config(text='PS4 is on')
    
def SS():
    GPIO.output(17,GPIO.LOW)
    label4.config(text='Security System is on')
    
button1 = tk.Button(root,text='Light_on',command=Light)
button2 = tk.Button(root,text='Computer_on',command=Computer)
button3 = tk.Button(root,text='PS4_on',command=PS)
button4 = tk.Button(root,text='SecuritiSystem_on',command=SS)
button1.pack(padx=2,pady=2,fill='x')
button2.pack(padx=2,pady=2,fill='x')
button3.pack(padx=2,pady=2,fill='x')
button4.pack(padx=2,pady=2,fill='x')

def Light_off():
    GPIO.output(2,GPIO.HIGH)
    label1.config(text='Light is off')
    
def Computer_off():
    GPIO.output(3,GPIO.HIGH)
    label2.config(text='Computer is off')
    
def PS_off():
    GPIO.output(4,GPIO.HIGH)
    label3.config(text='PS4 is off')
    
def SS_off():
    GPIO.output(17,GPIO.HIGH)
    label4.config(text='Security System is off')
    
button1 = tk.Button(root,text='Light_off',command=Light_off)
button2 = tk.Button(root,text='Computer_off',command=Computer_off)
button3 = tk.Button(root,text='PS4_off',command=PS_off)
button4 = tk.Button(root,text='Security System_off',command=SS_off)
button1.pack(padx=2,pady=2,fill='x')
button2.pack(padx=2,pady=2,fill='x')
button3.pack(padx=2,pady=2,fill='x')
button4.pack(padx=2,pady=2,fill='x')

root.mainloop()

GPIO.cleanup()