import tkinter
from PIL import ImageTk, Image 
from pynput import mouse, keyboard
from time import sleep
from sys import exit

from config import camset

version = 'v0.3.1'

root = tkinter.Tk()


## functions
def close_window():
    root.withdraw()
    exit() #(Endešlus python window)

def mouse_position():
    global xmpos, ympos  #(global zpristupni promenne ostatnim funkcim, promennym, ...)
    mpos = mousepos.position
    xmpos = mpos[0]
    ympos = mpos[1]
    print("X: " +  str(xmpos) + ", " "Y: " + str(ympos))

    root.after(10, mouse_position) #(repiting loop after 0.01s)

def on_key1(event):
    global imgstate1, imgstate2, imgstate3
    print("key1 is: " + camset.KEY1)
    imgstate1 = "hidden"
    imgstate2 = "normal"
    imgstate3 = "hidden"
    
def on_key2(event):
    global imgstate1, imgstate2, imgstate3
    print("key2 is: " + camset.KEY2)
    imgstate1 = "hidden"
    imgstate2 = "hidden"
    imgstate3 = "normal"

"""
def on_key1(event):
    print("key1 is: " + camset.KEY1)
    global imgstate1, imgstate2, imgstate3
    imgstate1 = "normal"
    imgstate2 = "hidden"
    imgstate3 = "hidden"

def on_key2(event):
    print("key2 is: " + camset.KEY2)
    global imgstate1, imgstate2, imgstate3
    imgstate1 = "normal"
    imgstate2 = "hidden"
    imgstate3 = "hidden"
"""

## tkinter window
root.resizable(width = False, height = False)
root.geometry(f'{camset.WINDOW_W}x{camset.WINDOW_H}')
root.configure(bg = camset.BACKGROUND)
root.title('CamCat ' + version)
root.protocol('WM_DELETE_WINDOW', close_window)
root.update()


## variables 
mousepos = mouse.Controller()
mpos = mousepos.position
xmpos = mpos[0]
ympos = mpos[1]

## basic imgstates
imgstate1 = "normal"
imgstate2 = "hidden"
imgstate3 = "hidden"

## functions start
#root.after(1000, mouse_position) #(starts loop after 1s)

## key listener
root.bind(str(camset.KEY1), on_key1)
root.bind(str(camset.KEY2), on_key2)

## cavans
Canvas = tkinter.Canvas(root, bg = camset.BACKGROUND, width = camset.WINDOW_W, height = camset.WINDOW_H)
Canvas.pack()

## images
catbgimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/catbg.png")
HandUpimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/HandUp.png")
KBoardTapLimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/KBoardTapL.png")
KBoardTapRimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/KBoardTapR.png")

## preload images
loadimage = Canvas.create_image(320, 180, image = catbgimage)
loadimage1 = Canvas.create_image(320, 180, image = HandUpimage, state = imgstate1)
loadimage2 = Canvas.create_image(320, 180, image = KBoardTapLimage, state = imgstate2)
loadimage3 = Canvas.create_image(320, 180, image = KBoardTapRimage, state = imgstate3)


# Note: dodelat a zpravit levou ruku na stisk klavesnice, pravou ruku a pohyb prave ruky, mys a klavesnici
# Note: v teto verzi je problem, ze imgstate1, imgstate2, imgstate3 se nezmeni z funkce, ale jsou furt basic imgstates

root.mainloop()