# LED Controller For Bell Targets

This a small python script that utilises the Raspberry PI GPIO pins to light up LEDs when a certain button is pressed. Then another button resets the lights.

# Requirements

<p>This script is intended to ran on a Raspberry PI running linux</p>
<p>This script uses MPG321 to play the audio files so install it before running</p>
<p>Install it on the command line using the following command:</p>

``` 
sudo apt-get -y install mpg321
```
# GPIO Setup

The script has default pin numbers for certain components set they are as follows:

<p>Pins 4,5,23,25 and 24 are set to be the LED's that light up when a BELL is scored</p>
<p>Pin 13 is set to be the LED that lights up while the program registers a BELL</p>
<p>Pin 6 is set to be the LED that lights up when the program starts and only turns off while the LED on Pin 13 is on</p>
<p>Pin 17 is set to be the button that turns on the LED's</p>
<p>Pin 27 is set to be the button that resets the LED's</p>
