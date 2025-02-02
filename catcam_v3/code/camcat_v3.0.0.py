import tkinter
from PIL import ImageTk, Image 
from pynput import mouse, keyboard
from time import sleep
from sys import exit

from config import camset_v3

version = 'v0.3.0'

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

def on_press(key):
    print("Pressed: {}".format(key))
    global imgstate1, imgstate2, imgstate3
    if key == camset_v3.KEY1:
        imgstate1 = "hidden"
        imgstate2 = "normal"
        imgstate3 = "hidden"
    
    elif key == camset_v3.KEY2:
        imgstate1 = "hidden"
        imgstate2 = "hidden"
        imgstate3 = "normal"

    root.after(10, on_press) #(repiting loop after 0.01s)

def on_release(key):
    print("Released: {}".format(key))
    global imgstate1, imgstate2, imgstate3
    if key == camset_v3.KEY1:
        imgstate1 = "normal"
        imgstate2 = "hidden"
        imgstate3 = "hidden"

    elif key == camset_v3.KEY2:
        imgstate1 = "normal"
        imgstate2 = "hidden"
        imgstate3 = "hidden"

    elif key == keyboard.Key.esc:
        return False

    root.after(10, on_release) #(repiting loop after 0.01s)


## tkinter variables
root.resizable(width = False, height = False)
root.geometry(f'{camset_v3.WINDOW_W}x{camset_v3.WINDOW_H}')
root.configure(bg = camset_v3.BACKGROUND)
root.title('CamCat ' + version)
root.protocol('WM_DELETE_WINDOW', close_window)
root.update()


## variables 
mousepos = mouse.Controller()
mpos = mousepos.position
xmpos = mpos[0]
ympos = mpos[1]

imgstate1 = "normal"
imgstate2 = "hidden"
imgstate3 = "hidden"

## functions start
#root.after(1000, mouse_position) #(starts loop after 1s)
root.after(1000, on_press) #(starts loop after 1s)

## cavans
Canvas = tkinter.Canvas(root, bg = camset_v3.BACKGROUND, width = camset_v3.WINDOW_W, height = camset_v3.WINDOW_H)
Canvas.pack()


## images
catbgimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/catbg.png")
HandUpimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/HandUp.png")
KBoardTapLimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/KBoardTapL.png")
KBoardTapRimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/KBoardTapR.png")

loadimage = Canvas.create_image(320, 180, image = catbgimage)
loadimage1 = Canvas.create_image(320, 180, image = HandUpimage, state = imgstate1)
loadimage2 = Canvas.create_image(320, 180, image = KBoardTapLimage, state = imgstate2)
loadimage3 = Canvas.create_image(320, 180, image = KBoardTapRimage, state = imgstate3)



root.mainloop()