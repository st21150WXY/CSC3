#Importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import sys
import os
import time

time_set = 0.25

SS_window = Tk()
image = PhotoImage(file='images/Amazing-Logo.png')

#setting up variables for Splash Screen
width_of_window = 427
height_of_window = 250
screen_width = SS_window.winfo_screenwidth()
screen_height = SS_window.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
SS_window.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
#w.configure(bg='#ED1B76')
SS_window.overrideredirect(True) #for hiding titlebar


#new window to open
def Open_Login_Screen():
    SS_window.withdraw()
    os.system("python AccountSystem.py")
    SS_window.destroy()


#Amazing_Logo_Animations
ALA_num = 1
for ALA in range(41):
    if ALA_num < 40:
        image = PhotoImage(file=f'images/Amazing_Logo_Animations/Amazing_Logo_Anim{ALA_num}.png')
    if ALA_num == 41:
        image = PhotoImage(file=f'images/Amazing-Logo.png')

    Frame(SS_window, width=427, height=250, bg='#f7f7f7').place(x=0, y=0)
    logo_label = Label(SS_window, image=image, bg='#f7f7f7')
    logo_label.place(x=100, y=-9)
    ALA_num += 1
    SS_window.update_idletasks()
    time.sleep(0.0625)


loading_text = Label(SS_window, text='Loading...', fg='#585959', bg='#f7f7f7')
loading_text.configure(font=("Calibri", 11, "bold"))
loading_text.place(x=10, y=215)


#Animation of Amazing Logo
image_a = ImageTk.PhotoImage(Image.open('images/splash_screen_loading_dots/loading_dot2.png'))
image_b = ImageTk.PhotoImage(Image.open('images/splash_screen_loading_dots/loading_dot1.png'))

Loading_Animation_Dots = [image_a, image_b, image_b, image_b]
cycle_anim = [image_b, image_a]
change_anim = 0
increment_of_anim = 1

for i in range(5):
    change_anim = 0
    increment_of_anim = 1
    for loading_dots_anim in range(4):
        Label(SS_window, image=Loading_Animation_Dots[0], border=0, relief=SUNKEN).place(x=180, y=160)
        Label(SS_window, image=Loading_Animation_Dots[1], border=0, relief=SUNKEN).place(x=200, y=160)
        Label(SS_window, image=Loading_Animation_Dots[2], border=0, relief=SUNKEN).place(x=220, y=160)
        Label(SS_window, image=Loading_Animation_Dots[3], border=0, relief=SUNKEN).place(x=240, y=160)

        Loading_Animation_Dots[loading_dots_anim] = cycle_anim[change_anim]
        change_anim += 1
        Loading_Animation_Dots[loading_dots_anim + increment_of_anim] = cycle_anim[change_anim]

        if loading_dots_anim == 2:
            increment_of_anim = 0
        if loading_dots_anim == 3:
            increment_of_anim = 1
            Loading_Animation_Dots[loading_dots_anim] = image_b
            Loading_Animation_Dots[0] = image_a

        if change_anim >= 1:
            change_anim = 0

        SS_window.update_idletasks()
        time.sleep(time_set)


#SS_window.destroy()
Open_Login_Screen()
SS_window.mainloop()
