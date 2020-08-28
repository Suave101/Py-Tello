# Documentation
## Basic Command's
### takeoff()
- Takes no arguments
- Makes the aircraft takeoff
### land()
- Takes no arguments
- Makes aircraft land
### up(x)
- Takes 1 argument:
  - Argument x is how many centimeters up the drone goes(takes string 20 through 500)
- Makes the aircraft go up x centimeters
### down(x)
- Takes 1 argument:
  - Argument x is how many centimeters down the drone goes(takes string 20 through 500)
- Makes the aircraft go down x centimeters
### left(x)
- Takes 1 argument:
  - Argument x is how many centimeters left the drone goes(takes string 20 through 500)
- Makes the aircraft go left x centimeters
### right(x)
- Takes 1 argument:
  - Argument x is how many centimeters right the drone goes(takes string 20 through 500)
- Makes the aircraft go right x centimeters
### forward(x)
- Takes 1 argument:
  - Argument x is how many centimeters forward the drone goes(takes string 20 through 500)
- Makes the aircraft go forward x centimeters
### back(x)
- Takes 1 argument:
  - Argument x is how many centimeters back the drone goes(takes string 20 through 500)
- Makes the aircraft go back x centimeters
### clockwise(degrees)
- Takes 1 argument:
  - Argument degrees is how many degrees clockwise the drone goes(takes string 1 through 360)
- Makes the aircraft go clockwise degrees degrees
### counterclockwise(degrees)
- Takes 1 argument:
  - Argument degrees is how many degrees counterclockwise the drone goes(takes string 1 through 360)
- Makes the aircraft go counterclockwise degrees degrees
### flip()
- Takes 1 argument:
  - Argument x is the direction the drone goes(takes string "l" is left, "r" is right, "f" is forward, and "b" is backward)
- Makes the aircraft go up x centimeters
### speed()
- Takes 1 argument:
  - Argument x is how many centimeters per second the drone goes(takes string 10 through 100)
- Makes the aircraft go x centimeters per second
### init()
- Takes no arguments
- Makes the program start communicating with the drone
## Advanced Command's
### send()
- Takes 1 argument
  - Argument
- Sends information to the aircraft
- Sendable information can be found at: https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
### eland()
- Takes no arguments
- Cuts power to all motors of the aircraft
### command()
- Takes no arguments
- Puts the drone in command mode(not required if using "init()" command)
### recv()
- recives information from drone and prints it in cli
- Use the following command if you do not use "init()" command to recive informantion from the drone

recvthread = threading.Thread(target=recv)

recvthread.start()

## Swarm Commander Info
The swarm commander is a part of the package that lets you swarm drones. The following program is an example of how swarm commander works.

```
import hsupytello.Swarm_Nest as swarmnest
import time as t

drone1 = swarmnest.drone("192.168.56.1")
drone2 = swarmnest.drone("192.168.56.2")
drone3 = swarmnest.drone("192.168.56.3")

drone1.tello_address = "192.168.56.2"
drone2.tello_address = "192.168.56.3"
drone3.tello_address = "192.168.56.1"

drone1.takeoff()
drone2.takeoff()
drone3.takeoff()
drone1.up(100)
drone2.forward(100)
drone3.backward(100)
drone1.down(100)
drone2.backward(100)
drone3.forward(100)
print("Drone 1 Crash Landing")
drone1.eland()
t.sleep(2)
print("Drone 2 Crash Landing")
drone2.eland()
t.sleep(2)
print("Drone 3 Regular Landing")
drone3.land()
```
