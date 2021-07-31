'''


**********************************************************************************************
*                                                                                            *
*                                                                                            *
*                      Smart Robotic Arm in Unity Game Simulation                            *
*                                                                                            *
*                          Authors:    Yongjie Yang  yjyang@bu.edu                           *
*                                      Sen Zhang     jasonall@bu.edu                         *
*                                      https://github.com/lijinlunbeng/Project-RobotArm-     *
*                                                                                            *
*                                10th December 2020                                          *
*                                                                                            *
*                                                                                            *
*              Options:      Spheres(Yellow)        Cubes(Red)          Cuboids(Blue)        *
*                            All objects            Do not grab                              *
*                                                                                            *
*                                                                                            *
**********************************************************************************************

'''



from PIL import ImageGrab
from PIL import Image
import tkinter
import time
import numpy as np

global Target
global ImgColor
global Prompt

Target = "All"    # None, All, Yellow(Sphere), Red(Cube), Blue(Oblong)
ImgColor = "Else"  # Else, Yellow, Red, Blue
Prompt = "Please select your target:"



def shoot():
    # Unity Running in full window mode
    # play scale = 1.3 (important!)
    coordinate = (717, 332, 738, 355)  # (startpoint_x, startpoint_y, endpoint_x, endpoint_y)
    img = ImageGrab.grab(coordinate)
    img.save('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/shot.png')
    coordinate_ref = (665, 290, 788, 400)  # (startpoint_x, startpoint_y, endpoint_x, endpoint_y)
    refimg = ImageGrab.grab(coordinate_ref)
    refimg.save('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/shot_ref.png')
    refimg = Image.open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/shot_ref.png')
    refimg_arr = np.array(refimg)
    rows, cols, channels = refimg_arr.shape
    for i in range(rows):
        for j in range(cols):
            if (j >= 49 and j <= 51):
                if ((i >= 42 and i <= 68)):
                    refimg_arr[i, j, 0] = 255
                    refimg_arr[i, j, 1] = 0
                    refimg_arr[i, j, 2] = 0
            if (j >= 74 and j <= 77):
                if ((i >= 42 and i <= 68)):
                    refimg_arr[i, j, 0] = 255
                    refimg_arr[i, j, 1] = 0
                    refimg_arr[i, j, 2] = 0
            if (i >= 69 and i <= 71):
                if(j >= 49 and j <= 75):
                    refimg_arr[i, j, 0] = 255
                    refimg_arr[i, j, 1] = 0
                    refimg_arr[i, j, 2] = 0
            if (i >= 39 and i <= 41):
                if (j >= 49 and j <= 75):
                    refimg_arr[i, j, 0] = 255
                    refimg_arr[i, j, 1] = 0
                    refimg_arr[i, j, 2] = 0

    refimg = Image.fromarray(refimg_arr)
    refimg.save('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/shot_ref.png')


def Sel_Sphere():
    global Target
    global Prompt
    Target = 'Yellow'
    Prompt = 'Sphere selected'
    Label['text'] = Prompt
    print ('Sphere selected')



def Sel_Cube():
    global Target
    global Prompt
    Target = 'Red'
    Prompt = 'Cube selected'
    Label['text'] = Prompt
    print('Cube selected')


def Sel_Oblong():
    global Target
    global Prompt
    Target = 'Blue'
    Prompt = 'Cuboid selected'
    Label['text'] = Prompt
    print('Cuboid selected')

def Sel_All():
    global Target
    global Prompt
    Target = 'All'
    Prompt = 'All objects selected'
    Label['text'] = Prompt
    print('All selected')

def Sel_None():
    global Target
    global Prompt
    Target = 'None'
    Prompt = 'No object selected'
    Label['text'] = Prompt
    print('None selected')


def Analyze_Color():
    global ImgColor
    # here image is an array
    image = Image.open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/shot.png')
    img_arr = np.array(image)
    # print(img_arr)
    rows, cols, channels = img_arr.shape
    R_count = 0
    Y_count = 0
    B_count = 0

    result = np.array(image)

    # print(rows, cols)

    # print(img_arr[int(rows/2), int(cols/2), 0]) # R value
    # print(img_arr[int(rows/2), int(cols/2), 1]) # G value
    # print(img_arr[int(rows/2), int(cols/2), 2]) # B value

    # img_arr[i, j, k] : rows, cols, channels(R = 0, G = 1, B = 2)
    # 255, 255, 255 white
    for i in range(rows):
        for j in range(cols):
            if (img_arr[i, j, 0] > 200 and img_arr[i, j, 1] < 50 and img_arr[i, j, 2] < 50):
                R_count += 1
                result[i, j, 0] = 255
                result[i, j, 1] = 0
                result[i, j, 2] = 0
                # typical red: 255, 0, 0
            elif (img_arr[i, j, 2] > 115 and img_arr[i, j, 0] < 50 and img_arr[i, j, 1] < 50 ):
                B_count += 1
                result[i, j, 0] = 0
                result[i, j, 1] = 0
                result[i, j, 2] = 255
                # typical blue: 0, 0, 255
            elif (img_arr[i, j, 0] > 230 and img_arr[i, j, 1] > 230 and img_arr[i, j, 2] < 20):
                Y_count += 1
                result[i, j, 0] = 255
                result[i, j, 1] = 255
                result[i, j, 2] = 0
            elif (img_arr[i, j, 0] > 3 * img_arr[i, j, 2] and img_arr[i, j, 1] > 3 * img_arr[i, j, 2]):
                if (img_arr[i, j, 0] < 1.25 * img_arr[i, j, 1] and img_arr[i, j, 0] > 0.75 * img_arr[i, j, 1]):
                    Y_count += 1
                    result[i, j, 0] = 255
                    result[i, j, 1] = 255
                    result[i, j, 2] = 0
            else:
                result[i, j, 0] = 0
                result[i, j, 1] = 0
                result[i, j, 2] = 0
            # if (img_arr[i, j, 0] > 250 & img_arr[i, j, 1] > 250 & img_arr[i, j, 2] > 250) :
                # white
            #    pass
    # print('Red:', R_count, 'Yellow:', Y_count, 'Blue:', B_count)
    img_result = Image.fromarray(result)
    img_result.save('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/result.png')

    # out of 690 pixels:
    if (R_count > 40):
        ImgColor = 'Red'
    elif (Y_count > 40):
        ImgColor = 'Yellow'
    elif (B_count > 20):
        ImgColor = 'Blue'
    else:
        ImgColor = 'Else'






    shoot()
    Analyze_Color()

    root = tkinter.Tk()
    root.title("Control Panel")
    root.geometry("800x400")
    Label = tkinter.Label(root, text=Prompt)
    Label.place(relx=0.2, rely=0.1, width=500)
    BTN_Yellow = tkinter.Button(root, text="Spheres", command=Sel_Sphere)
    BTN_Yellow.place(relx=0.1, rely=0.4, width=200)
    BTN_Red = tkinter.Button(root, text="Cube", command=Sel_Cube)
    BTN_Red.place(relx=0.4, rely=0.4, width=200)
    BTN_Blue = tkinter.Button(root, text="Cuboid", command=Sel_Oblong)
    BTN_Blue.place(relx=0.7, rely=0.4, width=200)
    BTN_All = tkinter.Button(root, text="All", command=Sel_All)
    BTN_All.place(relx=0.1, rely=0.8, width=200)
    BTN_None = tkinter.Button(root, text="None", command=Sel_None)
    BTN_None.place(relx=0.4, rely=0.8, width=200)
    root.mainloop()

    log = open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/log.txt', 'w')
    log.write("0\n")
    log.close()

    while(1):
        shoot()
        Analyze_Color()
        if Target == 'None':
            control = open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Control.txt', 'w')
            control.write('0')
            control.close()
            # print(Target, ' selected')
        elif Target == 'All' :
            control = open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Control.txt', 'w')
            control.write('1')
            control.close()
            # print (Target,' selected')
        else :
            if Target == ImgColor :
                control = open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Control.txt', 'w')
                control.write('1')
                control.close()
                # print(Target, ' found')
                log = open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Shots/log.txt', 'a')
                localtime = time.localtime(time.time())
                logstr = Target + ' found: ' + time.asctime(localtime) + '\n'
                log.write(logstr)
                log.close()
                time.sleep(0.4)
            else :
                # C:/Users/86189/Desktop/ARM/Assets/Resources/Control.txt
                control = open('C:/Users/86189/Desktop/EC602Robot_ImgRec/Control.txt', 'w')
                control.write('0')
                control.close()
                # print(Target, ' not found')




'''
References:

Colors' RGB values:
https://blog.csdn.net/qq_30541261/article/details/71440001?ops_request_misc=%257B%2522request%255Fid%2522
%253A%2522160670567719195265112145%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request
_id=160670567719195265112145&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_cli
ck~default-1-71440001.pc_first_rank_v2_rank_v28&utm_term=%E9%A2%9C%E8%89%B2rgb%E5%AF%B9%E7%85%A7%E8%A1%A8
&spm=1018.2118.3001.4449


Reading files using C#:
https://blog.csdn.net/ybhjx/article/details/53706715?ops_request_misc=%257B%2522request%255Fid%2522%253A%
2522160671210919726885881539%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&req
uest_id=160671210919726885881539&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~fir
st_rank_v2~rank_v28-7-53706715.pc_first_rank_v2_rank_v28&utm_term=c#%20读取txt&spm=1018.2118.3001.4449

Accessing an occupied file:
https://blog.csdn.net/nihao198503/article/details/9412497?ops_request_misc=%257B%2522request%255Fid%2522%
253A%2522160671330519724848168701%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257
D&request_id=160671330519724848168701&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~al
l~first_rank_v2~rank_v28-2-9412497.pc_first_rank_v2_rank_v28&utm_term=c#%20读取txt%20不占用&spm=1018.2118.3
001.4449

'''