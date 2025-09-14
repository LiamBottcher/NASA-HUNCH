# motorTest.py
# Test two continuous servo motors

from gpiozero import Servo
from time import sleep

# GPIO pins in parameter
servo1 = Servo(17)
servo2 = Servo(18)

print("Spinning servos forward/backward for 3 seconds each...")

# Forward/backward sequence
servo1.max()  # full speed forward
servo2.min()  # full speed backward
sleep(3)

servo1.min()  # reverse
servo2.max()
sleep(3)

# Stop both servos
servo1.mid()
servo2.mid()
print("Servos stopped.")
