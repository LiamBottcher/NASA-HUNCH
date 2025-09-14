# cameraTest.py
# Test the Pi Camera

from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()
picam2.capture_file("test_picture.jpg")
print("Picture saved as test_picture.jpg")
