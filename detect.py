import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(1, GPIO.IN)         #LED output pin

if __name__ == '__main__':
    try:
        while True:
            i7=GPIO.input(7)
            i1=GPIO.input(1)
            if i7==0:                 #When output from motion sensor is LOW
                print "7 No intruders",i7
                time.sleep(0.1)
            elif i7==1:               #When output from motion sensor is HIGH
                print "7 Intruder detected",i7
                time.sleep(0.1)

            if i1==0:                 #When output from motion sensor is LOW
                print "1 No intruders",i1
                time.sleep(0.1)
            elif i1==1:               #When output from motion sensor is HIGH
                print "1 Intruder detected",i1
                time.sleep(0.1)

            time.sleep(1)
    except KeyboardInterrupt:
         print("stopped by User")
         GPIO.cleanup()

"""
       if i1==0:                 #When output from motion sensor is LOW
             print "1 No intruders",i1
             time.sleep(0.1)
       elif i1==1:               #When output from motion sensor is HIGH
             print "1 Intruder detected",i1
             time.sleep(0.1)
"""
