import tkinter
from PIL import ImageTk
from pynput import mouse, keyboard
from time import sleep
from sys import exit

from config import camset_v3

version = 'v0.3.2.2'

root = tkinter.Tk()


### functions
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

##to co se stane na key2
def on_key1(event):
    global HandUpimageState, KBoardTapLimageState, KBoardTapRimageState, hold
    print("key1 is: " + camset_v3.KEY1)
    hold = True
    HandUpimageState = "hidden"
    KBoardTapLimageState = "normal"
    KBoardTapRimageState = "hidden"
    loadimages()

##to co se stane na key2
def on_key2(event):
    global HandUpimageState, KBoardTapLimageState, KBoardTapRimageState, hold
    print("key2 is: " + camset_v3.KEY2)
    hold = True
    HandUpimageState = "hidden"
    KBoardTapLimageState = "hidden"
    KBoardTapRimageState = "normal"
    loadimages()

##loaduje obrazky podle ##basic states
def loadimages(): 
    Canvas.create_image(320, 180, image = catbgimage)
    Canvas.create_image(320, 180, image = HandUpimage, state = HandUpimageState)
    Canvas.create_image(320, 180, image = KBoardTapLimage, state = KBoardTapLimageState)
    Canvas.create_image(320, 180, image = KBoardTapRimage, state = KBoardTapRimageState)


## tkinter window
root.resizable(width = False, height = False)
root.geometry(f"{camset_v3.WINDOW_W}x{camset_v3.WINDOW_H}")
root.configure(bg = camset_v3.BACKGROUND)
root.title("CamCat"  + version)
root.protocol("WM_DELETE_WINDOW", close_window)
root.update()

## mouse variables 
mousepos = mouse.Controller()
mpos = mousepos.position
xmpos = mpos[0]
ympos = mpos[1]

## hold variable
hold = False

## basic imgstates
HandUpimageState = "normal"
KBoardTapLimageState = "hidden"
KBoardTapRimageState = "hidden"

## cavans
Canvas = tkinter.Canvas(root, bg = camset_v3.BACKGROUND, width = camset_v3.WINDOW_W, height = camset_v3.WINDOW_H)
Canvas.pack()

## preload images
catbgimage = ImageTk.PhotoImage(file = "catcam_v3/cat/catbg.png")
HandUpimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/HandUp.png")
KBoardTapLimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/KBoardTapL.png")
KBoardTapRimage = ImageTk.PhotoImage(file = "Python/catcam/catcam_v3/cat/KBoardTapR.png")





## loop programu
def loop():
    global HandUpimageState, KBoardTapLimageState, KBoardTapRimageState, hold
    if root.bind(camset_v3.KEY1, on_key1) == True: # True protoze pak program nepreskakuje funkci if
        pass

    elif root.bind(camset_v3.KEY2, on_key2) == True: # True protoze pak program nepreskakuje funkci elif
        pass

    else:
        if hold == True:
            sleep(0.25)
            HandUpimageState = "normal"
            KBoardTapLimageState = "hidden"
            KBoardTapRimageState = "hidden"
            loadimages()

    root.after(500, loop)


loop()
mouse_position()


# ToDo: pohyb prave ruky --> pohyb mysi do leva/prava obrazek prave ruky se otoci, pohyb mysi nahoru/dolu obrazek se roztahuje/zkracuje
# ToDo: kdyz drzim jednu klavesu a pridam k tomu druhou a pak druhou pustim, zacne se to lagovat


# Protip: pokud se pruhledny obrazek zobrazuje cerne tak ma malou bit depth --> ve photopea se musi nechat zaskrtnuto "dont use paletts"

root.mainloop()