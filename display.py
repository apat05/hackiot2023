import lcd
import face

def main():

    people = [0, 0, 0, 0]
    default_range = ultrasonic()

    while True:
        #outputting the string information to the screen
        lcd_string("A: " + people[0] + " Q: " + people[1] + " K: " + people[2] + " R: " + people[3], 1)
        range = ultrasonic()
        if(range < default_range):
            #use the camera, identify the person, and increment their counter
            id = #numeric value returned by facial recognition software

            #increment the identified person's number
            people[id] += 1
        
        while range != default_range: #so that the counter doesn't continue to update while person is putting dish in
            range = ultrasonic()
            
            
#Source: https://www.kitflix.com/how-to-interface-raspberry-pi-with-ultrasonic-sensor
def ultrasonic():

    TRIG = 21
    ECHO = 20
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

                


                





