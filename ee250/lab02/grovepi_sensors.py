""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd as lcd

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
	# Ultrasonic ranger is plugged into D4
	ultrasonic_ranger = 4

    # Connect the Grove Rotary Angle Sensor to analog port A0
	potentiometer = 0
	grovepi.pinMode(potentiometer, "INPUT")
	time.sleep(1)

	# The maximum number the ultrasonic can accept is around 517
	MAX_ULTRASONIC = 517
	# The max number to potentiometer can measure is 1023
	MAX_POTENTIOMETER = 1023


	# Clear lcd screen
	lcd.setText("")
	lcd.setRGB(0,255,0)
	# Main Program loop
	while True:
		try:
			###############################################################
			# Read sensor value from potentiometer
			sensor_value = grovepi.analogRead(potentiometer)
			
			# Calculate the distance threshold in cm from the raw value of the potentiometer
			threshold = round((float)(sensor_value) * MAX_ULTRASONIC / MAX_POTENTIOMETER, 1)

			###############################################################

			#obtain the ranger's data on how close the object is
			time.sleep(0.2)
			ranger_raw = grovepi.ultrasonicRead(ultrasonic_ranger)

			###############################################################
			# Set the LCD text to what was calculated
			obj_pres = ""
			# Check if the threshold is met
			if ranger_raw <= threshold:
				lcd.setText_norefresh("%dcm  OBJ PRES\n distance: %dcm" %(threshold,ranger_raw))
				obj_pres = "OBJ PRES"
				# lcd.setRGB(255,0,0)
			else:
				lcd.setText_norefresh("%dcm  \n distance: %dcm" %(threshold, ranger_raw))
				# lcd.setRGB(0,255,0)

			# lcd.setText_norefresh("%dcm  %s\n distance: %dcm" %(threshold, obj_pres, ranger_raw))
			# lcd.setText_norefresh("angle is: %.1f \n distance: %d" %(degrees, ranger_raw))

		

		except KeyboardInterrupt:
			lcd.setText("Program Quit")
			print("Program quit")
			break
		except IOError:
			lcd.setText("IOError")
			break
    # while True:
    #     #So we do not poll the sensors too quickly which may introduce noise,
    #     #sleep for a reasonable time of 200ms between each iteration.
    #     time.sleep(0.2)

    #     print(grovepi.ultrasonicRead(PORT))

