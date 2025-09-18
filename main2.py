from machine import Pin , PWM , time_pulse_us
import time

servo = PWM(Pin(2) , freq = 50)
trig = Pin(5 , Pin.OUT)
echo = Pin(18 , Pin.IN)
led = Pin(32 , Pin.OUT)
led_2 = Pin(33 , Pin.OUT)

A1 = Pin(25 , Pin.OUT)
A2 = Pin(26 , Pin.OUT)
B1 = Pin(27 , Pin.OUT)
B2 = Pin(14 , Pin.OUT)

mane = 0

bonbast = False

Nahie1 = False
Nahie2 = False
Nahie3 = False
Nahie4 = False

def Front ():
    A1.on()
    A2.off()
    B1.on()
    B2.off()
    print("Front")
    
def Back ():
    A1.off()
    A2.on()
    B1.off()
    B2.on()
    print("Back")
    
def FR ():
    A1.off()
    A2.off()
    B1.on()
    B2.off()
    print("Front_Right")
    
def FL ():
    A1.on()
    A2.off()
    B1.off()
    B2.off()
    print("Front_Left")
    
def BL ():
    A1.off()
    A2.off()
    B1.off()
    B2.on()
    print("Back_Right")
    
def BR ():
    A1.off()
    A2.on()
    B1.off()
    B2.off()
    print("Back_Left")
    
def Stop():
    A1.off()
    A2.off()
    B1.off()
    B2.off()

def angel(drg):
    dut = int((drg / 180)*102+26)
    servo.duty(dut)
    #print(drg)
flag = False
A = 0
B = 0
myangin = 0
Stop()

while True:
    print("*******************")
    time.sleep_ms(100)
    for x in range(175):
        if(x >1):
            angel(x)
            time.sleep_ms(50)
            trig.value(0)
            time.sleep_us(5)
            trig.value(1)
            time.sleep_us(10)
         
            trig.value(0)
            Tool_Puls = time_pulse_us(echo , 1 , 30000)
            #print(Tool_Puls)
            Fasele = (340*Tool_Puls)/20000
    
            trig.value(0)
            time.sleep_us(5)
            trig.value(1)
            time.sleep_us(50)
            trig.value(0)
            Tool_Puls = time_pulse_us(echo , 1 , 30000)
            #print(Tool_Puls)
            Fasele = (340*Tool_Puls)/20000
#             print(Fasele)
#             print(Fasele)
            if (Fasele < 15 and Fasele > 5):
           # print("start")
#                 print(x)
               
                #print(Fasele)
                flag = True
                if (x >0 and x <45):
                    Nahie1 = True
#                     print('Nahie1')
                if (x >45 and x <90):
                    Nahie2 = True
#                     print('Nahie2')
                if (x >90 and x <110):
                    Nahie3 = True
#                     print('Nahie3')
                if (x >110 and x <180):
                    Nahie4 = True
#                     print('Nahie4')

             
                
                
#                 print(mane)
                Fasele =0
                Tool_Puls=0

            
        
    if (Nahie3 == True and Nahie2 == True):
        mane = 1
    if ( Nahie4 == True and Nahie3 == False and Nahie2 == False and Nahie1 ==False):
        mane = 2
    if (Nahie1 == True and Nahie3 == False and Nahie2 == False and Nahie4 ==False):
        mane = 3
    if (Nahie1 == True and Nahie2 == True and Nahie3 == False and Nahie4 == False):
        mane = 4
    if (Nahie3 == True and Nahie4 == True and Nahie1 == False and Nahie2 == False):
        mane = 5
    if (Nahie1 == True and Nahie4 == True and Nahie3 == False and Nahie2 == False):
        mane = 6
    if (Nahie1 == True and Nahie4 == True and Nahie3 == True and Nahie2 == True):
        mane = 7
    print(mane)

    Nahie1 = False
    Nahie2 = False
    Nahie3 = False
    Nahie4 = False
    
    for y in range(175 , -1 , -1):
        if(y >1):
            angel(y)
            time.sleep_ms(10)
         
    Front()
    time.sleep(.1)
    Stop()
    
    if (mane == 1 or mane == 5):
        FR()
        time.sleep(1)
        Stop()
    if (mane == 4):
        FL()
        time.sleep(1)
        Stop()
    if (mane == 2):
        Front()
        time.sleep(.1)
        Stop()
    if (mane == 3):
        Front()
        time.sleep(.1)
        Stop()
    if (mane == 6):
        Front()
        time.sleep(.1)
        Stop()
    if (mane == 7):
        bonbast = True
    if (mane == 6 and bonbast == True):
        Back()
        time.sleep(.3)
        Stop()
    mane = 0
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    

