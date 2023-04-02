import lcd
#import face

import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
LED_ON = 15

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

def main():

<<<<<<< HEAD
    lcd.init()    
    lcd.GPIO.cleanup() 
=======
    lcd_init()

>>>>>>> fddc9afbd90432488d1918f7a39cdef68cab6004
    people = [0, 0, 0, 0]
    default_range = ultrasonic()

    while True:
        #outputting the string information to the screen
        lcd_string(f"A:{people[0]} Q:{people[1]} K:{people[2]} R:{people[3]}", 1)
        range = ultrasonic()
        if(range < default_range):
            #use the camera, identify the person, and increment their counter
            id = 0 #numeric value returned by facial recognition software

            #increment the identified person's number
            people[id] += 1
        
        while range != default_range: #so that the counter doesn't continue to update while person is putting dish in
            range = ultrasonic()
            
            
#Source: https://www.kitflix.com/how-to-interface-raspberry-pi-with-ultrasonic-sensor
def ultrasonic():

    TRIG=21
    ECHO=20

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)

    return distance

def lcd_start:


                


                





