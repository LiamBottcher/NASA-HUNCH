# NASA HUNCH Lunar Ejecting Robot
Hello and welcome to my NASA HUNCH Project

This is my reconstruction of my submission for NASA HUNCH Lunar Ejecting Robot, which granted my team first place in the Rutgers evaluation and a all expenses paid for trip to Houston Texas to present with other finalists in front of Nasa Engineer and Interns

The reason this is a reconstruction and not the original code is because when programming this project as a solo developer in highschool, I did not have nearly as much experience with Git and Github as I do now. So, when the end of the year came along, all of my code, scripts, and created images were in my google drive with my school account and that was deactivated so it is rendered inaccessible. They were also all stored in a 16gb sd card in the raspberry pi zero 2 w that I used, which is stored in a cabinet in my Engineering 4 Computer Integrated Manufacturing classroom so I can't access that either. So for the sake of showing off this project here is the python scripts used.

My team was Liam Bottcher (me), Salman Choudhury, Ahnaf Ali, and Jason Lazoff

## PART 1: SETUP

Make sure the Rapsberry Pi Zero 2 W is has 2 wires, one in each gpio pin, going to the separate servo motor slots for input, 2 more wires one from each 5v pin to the power wire in each servo motor, and 2 more wires one for each servo motor that is a ground wire

Also make sure the Picamera is attached correctly

Only after all of that has been done can you safely plug the power into the rapsberry pi, 5 volts, since moving wires and camera connections around with it being powered on can be dangerous and possibly mess with the rapsberry pi

Most raspberry pis have these libraries pre installed but just in case, run:

sudo apt update
sudo apt install python3-gpiozero
sudo apt install python3-picamera2

then clone this repo and you'll have the files ready

## PART 2: RUNNING

now you can test the files, so start by testing the camera with
python cameraTest.py

you should also test the motors, so run:
python motorTest.py

finally, you can run the main program, assuming complete setup and using a duplicate prototype of our lunar ejecting robot, run:
python main.py

