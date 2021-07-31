# Self-learning-Robotic-Arm
Course project of EC602, Boston University.

Neatened in July, 2021

This project consists of two parts: a game simulation in Unity, and a Python project that identifies the objects and gives instructions to grab it.
My work mainly exists in this Python program.

Our poster:
![Poster](https://github.com/jasonall-cauc/Self-learning-Robotic-Arm/blob/main/Poster_Robot.jpg)


## How it works:

### Step1, settings.

The Python program prompts a UI that allows the user to select which objects (yellow spheres, red cubes and blue cuboids) to grab.

### Step2, image acquisition

The Python program takes screenshots of the game, and cuts the image into very small ones that contain little but the image of the object in front of the robotic arm.

We could have used the Unity recorder to take the screenshots. However, this way is slower, and may result in failure in simultaneity. Using Python to take screenshots
 is faster, easier and more convenient.
 
However, the way we cut the screenshot into small close-ups of an object is still simple and immature. This is done by taking screenshots of the entire window, and cutting off 
a small square in a fixed position(As you see in the function def shoot(), we gave fixed coordinates. This is where the object shows up in the window). 
This program is not able to truely "identify" with intelligence a zone that contains the object, and I suspect that even if it could 
(with an advanced method perhaps), it will take so long that the Unity game simulation cannot accept. The object might already passed the robotic arm by the time 
the Python part has successfully identified the object.

### Step3, image identification

The Python program identifies the object and classifies it into three categories (spheres, cubes, cuboids). This is done by counting pixels of different colors.

### Step4, control

After identifying the object, the Python program writes the command in a word file under the directory of the Unity project. If the next object should be grabbed, 
it writes 1 in the file, otherwise 0. The robotic arm will read this file before deciding whether to grab the object.

This project is still immature. In a real system, a sensor can be placed above the conveyor belt, but in this game simulation we have to use screenshots as a camera. 
I keep this project as a record, and hope to improve it in the future.

## Developers

This is a group project in course EC602, which I took in Boston University in 2020. 

Authors:

Yongjie Yang yangyj@bu.edu Sen Zhang jasonall@bu.edu

Full document can be found here: https://github.com/lijinlunbeng/Project-RobotArm-
