# import os library for playing audio files
import os
# import GPIO and Sleep libraries
import RPi.GPIO as GPIO
from time import sleep
# setup the GPIO system
GPIO.setmode(GPIO.BCM)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname) 

# define path to audio file
dingfile = "Sound_Files/bell_sound.mp3"
announcefile = "Sound_Files/announce_sound.mp3"

# define given pins
# to set your own pins enter the GPIO number in the list below
ledpins = [4,5,23,6,26]
maxcount = -1
for pinumber in ledpins:
    # if pinnumber undefined  skip and stop defining
    if pinumber == "":
        break
    else:
        # setup led pin
        GPIO.setup(pinumber, GPIO.OUT)
        maxcount += 1    

# to set your own pin numbers replace the numbers below with your own
onpin = 17 # set led on button pin
offpin = 22 # define led off button pin
resetledpin = 27 # defines the pin for the reset led
activeledpin = 25 # defines the pin for the active led
GPIO.setup(activeledpin, GPIO.OUT)
GPIO.setup(resetledpin, GPIO.OUT)
GPIO.setup(offpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(onpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # with pull up resistor

# function to turn on an led, takes the GPIO pin of the LED as an argument
def turnon(lednum):
    print("turnon"+str(lednum))
    # turn led on
    GPIO.output(lednum, 1)
    
    
# function that turns off all leds
def turnoff(leds):
    # if led GPIO pin is undefined skip and stop function
    for led in leds:
        if led == "":
            return()
        else:
          # turn led off  
          GPIO.output(led, 0)

# count is set to zero as number of led's turned on is 0
count = 0
# not all the leds are turned on
allturnedon = False
# starts the main loop
program_running  = True
# turns off any leds that were left on
turnoff(ledpins)

GPIO.output(activeledpin, 1)

# main loop for program
while program_running == True:
    # if not all the LED's are turned on the user can turn more on
    if allturnedon == False:
        # if the on button is pressed
        if GPIO.input(onpin) == 0:
            print(count)
            # turn bell light on
            turnon(ledpins[count])
            # turn reset led on and active led off
            GPIO.output(activeledpin, 0)
            GPIO.output(resetledpin, 1)
            # play audio files
            try:
                os.system("mpg321 " + dingfile)
            except: 
                print("Audio File Not Found")
            try:
                os.system("mpg123 " + announcefile)
            except:
                print("Audio File Not Found")
            count += 1
            # checks if all the led's are on, if so prevents user from attempting to turn more on
            if count > maxcount:
                allturnedon = True
            # sleep prevetns one input being registered as many
            sleep(4)
            # turns reset led off and active led on
            GPIO.output(resetledpin, 0)
            GPIO.output(activeledpin, 1)
        # if the off button is pressed, all leds turned off and count reset
        if GPIO.input(offpin) == 0:
            turnoff(ledpins)
            count = 0
        # pass if not input recorded
        else:
            ...
    # if all the leds are on the user can only turn them off
    # no input from the on button is registered
    if allturnedon == True:
        if GPIO.input(offpin) == 0:
            print("turnedoff")
            turnoff(ledpins)
            count = 0
            allturnedon = False 
