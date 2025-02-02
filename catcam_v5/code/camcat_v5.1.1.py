import tkinter
from PIL import ImageTk, Image
from pynput import mouse, keyboard
from time import sleep
from sys import exit

from config import camset_v5

group = "v5"
version = "v0.5.1.1"

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
    # print("X: " +  str(xmpos) + ", " "Y: " + str(ympos))
    # root.after(refrh_rate_angle, mouse_position) #(repiting loop after 0.01s)


def image_rotate():
    global catRightHandimageTk
    Canvas.delete("all")
    mouse_position()
    catRightHandimageTk = ImageTk.PhotoImage(catRightHandimage.rotate((xmpos / (root.winfo_screenheight() / angle)) - 20, expand=True, resample=Image.BICUBIC))
    loadimages()
    root.after(refrh_angle_rate, image_rotate)

##to co se stane na key1
def on_key1(event):
    global HandUpimageState, KBoardTapLimageState, KBoardTapRimageState, catRightHandimageTk
    print("key1 is: " + camset_v5.KEY1)
    HandUpimageState = "hidden"
    KBoardTapLimageState = "normal"
    KBoardTapRimageState = "hidden"
    loadimages()

##to co se stane na key2
def on_key2(event):
    global HandUpimageState, KBoardTapLimageState, KBoardTapRimageState, catRightHandimageTk
    print("key2 is: " + camset_v5.KEY2)
    HandUpimageState = "hidden"
    KBoardTapLimageState = "hidden"
    KBoardTapRimageState = "normal"
    loadimages()

def key_released(event):
    global HandUpimageState, KBoardTapLimageState, KBoardTapRimageState
    print("key released")
    HandUpimageState = "normal"
    KBoardTapLimageState = "hidden"
    KBoardTapRimageState = "hidden"
    loadimages()

##loaduje obrazky podle ##basic states
def loadimages(): 
    Canvas.create_image(320, 180, image = catbgimage)
    Canvas.create_image(320, 180, image = HandUpimage, state = HandUpimageState)
    Canvas.create_image(320, 180, image = KBoardTapLimage, state = KBoardTapLimageState)
    Canvas.create_image(320, 180, image = KBoardTapRimage, state = KBoardTapRimageState)
    Canvas.create_image(274, 178, image = catRightHandimageTk, anchor = "center")


## tkinter window
root.resizable(width = False, height = False)
root.geometry(f"{camset_v5.WINDOW_W}x{camset_v5.WINDOW_H}")
root.configure(bg = camset_v5.BACKGROUND)
root.title("CamCat " + version)
root.protocol("WM_DELETE_WINDOW", close_window)
root.update()

## mouse variables 
mousepos = mouse.Controller()
mpos = mousepos.position
xmpos = mpos[0]
ympos = mpos[1]

# rotation angle
angle = 45

# refresh rate for right gand image
refrh_angle_rate = 1 #ms


## basic imgstates
HandUpimageState = "normal"
KBoardTapLimageState = "hidden"
KBoardTapRimageState = "hidden"

## cavans
Canvas = tkinter.Canvas(root, bg = camset_v5.BACKGROUND, width = camset_v5.WINDOW_W, height = camset_v5.WINDOW_H)
Canvas.pack()

## preload images
filepath = "D:/DATA-Honza/coding/Python/catcam/assets/cat"

catbgimage = ImageTk.PhotoImage(file = filepath + "/catbg.png")
HandUpimage = ImageTk.PhotoImage(file = filepath + "/HandUp.png")
KBoardTapLimage = ImageTk.PhotoImage(file = filepath + "/KBoardTapL.png")
KBoardTapRimage = ImageTk.PhotoImage(file = filepath + "/KBoardTapR.png")
catRightHandimage = Image.open(filepath + "/catRightHand.png").resize((150, 150))
catRightHandimageTk = ImageTk.PhotoImage(catRightHandimage)


## key bindings
root.bind(camset_v5.KEY1, on_key1)
root.bind(camset_v5.KEY2, on_key2)
root.bind("<KeyRelease-" + camset_v5.KEY1 + ">", key_released)
root.bind("<KeyRelease-" + camset_v5.KEY2 + ">", key_released)


loadimages()
mouse_position()
image_rotate()


# ToDo: pohyb mysi nahoru/dolu obrazek se roztahuje/zkracuje


# Protip: pokud se pruhledny obrazek zobrazuje cerne tak ma malou bit depth --> ve photopea se musi nechat zaskrtnuto "dont use paletts"
# Protip: kdyz Error: 'PhotoImage' object has no attribute '_PhotoImage__photo'; tak se musi zkontrolovat file path napr: "D:/catcam/catcam_v3/cat/catbg.png" = filepath musi byt presna



# businessp plan: catcam bude na prodej; budou se tam moc davat obrazky (jine postavicky, oblecky na kocku, atd..) z vlastni webove stranky; obrazky se budou za neco mako prodavat 

root.mainloop()