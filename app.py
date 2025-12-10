from flask import Flask, render_template, jsonify, request
app = Flask(__name__, template_folder='template', static_folder='static')

try:
    import RPi.GPIO as GPIO     # Imports the RPi.GPIO library
except ImportError:
    print("RPi.GPIO not found. Using Mock GPIO.")
    class MockGPIO:
        BCM = 10
        BOARD = 11
        OUT = 0
        IN = 1
        HIGH = 1
        LOW = 0
        def setwarnings(self, flag): pass
        def setmode(self, mode): pass
        def setup(self, pin, mode): pass
        def output(self, pin, state): pass
        def cleanup(self): pass
        def input(self, pin): return 0
    GPIO = MockGPIO()

import time                 #Imports Python’s built-in time module     #Allows you to use functions like time.sleep() to create delays.
import os                   #Imports the os (Operating System) module    #Provides a way of using operating system-dependent functionality.
from time import sleep      #Imports only the sleep function from the time module.
GPIO.setwarnings(False)     #If GPIO pins were not cleaned up properly in a previous run, warnings appear — this hides them       #Useful when testing code repeatedly.
GPIO.setmode(GPIO.BCM)      #Sets the GPIO pin numbering mode.    #BCM mode uses the Broadcom SOC channel numbers.



global pwmobj                    # declare the pmwobj as a global variable



# Route for the home page
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


# Main Page
if(__name__=='__main__'):

    # Run the Flask app
    app.run(host='0.0.0.0',debug=True)     