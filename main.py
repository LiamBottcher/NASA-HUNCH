from gpiozero import Servo
from picamera2 import Picamera2
from time import sleep

# Update pins to match your wiring
servo1 = Servo(17)
servo2 = Servo(18)

# Initialize camera
picam2 = Picamera2()
picam2.start()

print("Waiting 10 seconds before starting sequence...")
sleep(10)

for i in range(1, 5):
    print("Reorienting robot for picture", i)
    
    # Spin motors to rotate robot 90 degrees to the right
    servo1.max()   # forward
    servo2.min()   # backward
    sleep(5)       # adjust timing as needed for 90 degree rotation
    
    # Stop motors
    servo1.mid()
    servo2.mid()
    
    # Take picture
    filename = "picture" + str(i) + ".jpg"
    picam2.capture_file(filename)
    print("Picture saved as", filename)

print("Sequence complete.")
