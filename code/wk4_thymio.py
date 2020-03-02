from pythymiodw import *
from time import sleep
from libdw import pyrebase

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


# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()

robot = ThymioReal()  # create a robot object

no_movements = True


#Define functions
def forward():
    robot.wheels(100, 100)
    robot.sleep(1)

def right():
    robot.wheels(100, -100)
    robot.sleep(1)
    
def left():
    robot.wheels(-100, 100)
    robot.sleep(1)

def stop():
    robot.wheels(0, 0)
    
    
while no_movements:

    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the robot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here
    dict = db.child("hi").get(user['idToken'])
    array = dict.val()
    print(array)
    
    if len(array) != 0:
        no_movements = False
    else:
        time.sleep(0.5)


# Write the code to control the robot here
while len(array) != 0:
    if array[0] == "UP":
        forward()
        array.pop(0)  
    elif array[0] == "RIGHT":
        right()
        array.pop(0)
    elif array[0] == "LEFT":
        left()
        array.pop(0)
    elif array[0] == "STOP":
        stop()
        array.pop(0)
        
no_movement = True
        

robot.quit()
# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)

