import tkinter 
from PIL import ImageTk, Image 
from pynput import mouse, keyboard
from time import sleep
from sys import exit

from config import camset_v2

version = 'v0.2.1'

root = tkinter.Tk()

# window variables
window_w = 640
window_y = 360
aspect_ratio = window_w / window_y

# mouse position variables
mousepos = mouse.Controller()
mpos = mousepos.position
xmpos = mpos[0]
ympos = mpos[1]


frame = ""


def close_window():
    root.withdraw()
    exit() # Endešlus python window


def resize():
    window_y = root.winfo_height()
    window_w = root.winfo_width()

    new_aspect_ratio = window_w / window_y

    if new_aspect_ratio > aspect_ratio:
        desired_width = root.winfo_width()
        desired_height = int(window_w / aspect_ratio)
    else:
        desired_height = root.winfo_height()
        desired_width = int(window_y * aspect_ratio)

    if root.winfo_width() != desired_width or root.winfo_height() != desired_height:
        root.geometry(f'{desired_width}x{desired_height}')

    root.after(0, resize) # instant resize


def mouse_position():
    global xmpos, ympos  # global zpristupni promenne ostatnim funkcim, promennym, ...
    mpos = mousepos.position
    xmpos = mpos[0]
    ympos = mpos[1]
    print("X: " +  str(xmpos) + ", " "Y: " + str(ympos) + str(frame))

    root.after(10, mouse_position) # repiting loop after 0.01s


root.resizable(width = True, height = True)
root.geometry(f'{window_w}x{window_y}')
root.maxsize(width = 1280, height = 720) # Max size is the original image size
root.minsize(width = 160, height = 90)
root.configure(bg = camset_v2.BACKGROUND)
root.title('camcat ' + version)
root.protocol('WM_DELETE_WINDOW', close_window)
root.update()

# functions start
root.after(1000, resize) # starts loop after 1s
root.after(1000, mouse_position) # starts loop after 1s



print("-----")
print('Bongo Cat Live Cam ' + version + " by JDolik")
print("-----")
print('Note: You can configure some things in folder: "config --> camset_v2"')
print('Note: When re-sizing, hit k1 (default "F") or k2 (default "H") to reload the image!')







root.mainloop()