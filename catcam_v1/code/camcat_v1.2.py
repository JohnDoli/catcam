import tkinter 
from PIL import ImageTk, Image 
from pynput import mouse, keyboard
from time import sleep
from sys import exit

from config import camset

version = 'v0.1.2'

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
    window_x = int(window_y / 9) * 16

    if window_x != int(window_y / 9) * 16:
        root.geometry(f"{window_x}x{window_y}")

    if window_y != int(window_x / 16) * 9:
        root.geometry(f"{window_x}x{window_y}")
    
    root.after(250, resize) # repiting loop after 0.25s

def mouse_position():
    global xmpos, ympos  # global zpristupni promenne ostatnim funkcim, promennym, ...
    mpos = mousepos.position
    xmpos = mpos[0]
    ympos = mpos[1]
    print("X: " +  str(xmpos) + ", " "Y: " + str(ympos) + str(frame))

    root.after(10, mouse_position) # repiting loop after 1s


root = tkinter.Tk()
root.resizable(width = True, height = True)
root.geometry(camset.WINDOW_SIZE)
root.maxsize(width = 1280, height = 720) # Max size is the original image size
root.minsize(width = 160, height = 90)
root.configure(bg = camset.BACKGROUND)
root.title('camcat ' + version)
root.protocol('WM_DELETE_WINDOW', close_window)
root.update()

root.after(10, resize) # starts loop after 2s
root.after(10, mouse_position) # starts loop after 2s


# zjisti velikost obrazovky 
scr_x = root.winfo_screenwidth()
scr_y = root.winfo_screenheight()
xframe = scr_x / 6
yframe = scr_y / 4

# urcovani polohy pro obrazky
x_1 = xframe * 1 # "*1" tu nemusi byt
x_2 = xframe * 2
x_3 = xframe * 3
x_4 = xframe * 4
x_5 = xframe * 5
x_6 = xframe * 6

y_1 = yframe * 1 # "*1" tu nemusi byt
y_2 = yframe * 2
y_3 = yframe * 3
y_4 = yframe * 4 # misto "* 4" tu muze byt "scry"


print("-----")
print('Bongo Cat Live Cam ' + version + " by JDolik")
print("Inspirated by ZeCryptic")
print("-----")
print('Note: You can configure some things in folder: "config --> camset"')
print('Note: When re-sizing, hit k1 (default "F") or k2 (default "H") to reload the image!')


def frames():
    global frame
    if xmpos <= x_1 and ympos <= y_1:
        frame = ", frame1"
    elif xmpos <= x_1 and ympos <= y_2:
        frame = ", frame2"
    elif xmpos <= x_1 and ympos <= y_3:
        frame = ", frame3"
    elif xmpos <= x_1 and ympos <= y_4:
        frame = ", frame4"
    elif xmpos <= x_2 and ympos <= y_1:
        frame = ", frame5"
    elif xmpos <= x_2 and ympos <= y_2:
        frame = ", frame6"
    elif xmpos <= x_2 and ympos <= y_3:
        frame = ", frame7"
    elif xmpos <= x_2 and ympos <= y_4:
        frame = ", frame8"
    elif xmpos <= x_3 and ympos <= y_1:
        frame = ", frame9"
    elif xmpos <= x_3 and ympos <= y_2:
        frame = ", frame10"
    elif xmpos <= x_3 and ympos <= y_3:
        frame = ", frame11"
    elif xmpos <= x_3 and ympos <= y_4:
        frame = ", frame12"
    elif xmpos <= x_4 and ympos <= y_1:
        frame = ", frame13"
    elif xmpos <= x_4 and ympos <= y_2:
        frame = ", frame14"
    elif xmpos <= x_4 and ympos <= y_3:
        frame = ", frame15"
    elif xmpos <= x_4 and ympos <= y_4:
        frame = ", frame16"
    elif xmpos <= x_5 and ympos <= y_1:
        frame = ", frame17"
    elif xmpos <= x_5 and ympos <= y_2:
        frame = ", frame18"
    elif xmpos <= x_5 and ympos <= y_3:
        frame = ", frame19"
    elif xmpos <= x_5 and ympos <= y_4:
        frame = ", frame20"
    elif xmpos <= x_6 and ympos <= y_1:
        frame = ", frame21"
    elif xmpos <= x_6 and ympos <= y_2:
        frame = ", frame22"
    elif xmpos <= x_6 and ympos <= y_3:
        frame = ", frame23"
    elif xmpos <= x_6 and ympos <= y_4:
        frame = ", frame24"
    else:
        frame = ""

    root.after(10, frames)

root.after(10, frames)





root.mainloop()