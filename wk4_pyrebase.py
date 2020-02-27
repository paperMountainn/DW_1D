import RPi.GPIO as GPIO
from libdw import pyrebase
import time

projectid = "omelette-8579f"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyAMJWExlvlmTnztTJHrBnC7eKAvX5jIl0o"
email = "limjunwei567@gmail.com"
password = "omelette"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED and GPIO18 for switch
command = [12, 16, 20, 21]
commandz = []
# Set GPIO23 as output.
GPIO.setup(command, GPIO.OUT)

# Set GPIO18 as input with a pull-down resistor.
GPIO.setup(command, GPIO.IN, GPIO.PUD_DOWN)

db = firebase.database()

done = False

while not done:

    if GPIO.input(command[0]) == GPIO.HIGH:
        commandz.append("UP")
        print("UP")
        time.sleep(0.5)
    elif GPIO.input(command[1]) == GPIO.HIGH:
        commandz.append("RIGHT")
        print("RIGHT")
        time.sleep(0.5)
    elif GPIO.input(command[2]) == GPIO.HIGH:
        commandz.append("LEFT")
        print("LEFT")
        time.sleep(0.5)

    elif GPIO.input(command[3]) == GPIO.HIGH:
        command.append("END")
        print("END")
        break
 

# Write to database once the OK button is pressed

root = lambda x: db.child("hi").set(x,user['idToken'])
#import code; code.interact(local=dict(globals(), **locals()))

[root(commandz) for i in command]
