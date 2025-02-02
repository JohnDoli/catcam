import tkinter 
from pynput import mouse, keyboard
from time import sleep
from sys import exit

from config import camset


mousepos = mouse.Controller()


version = 'v0.1.1'


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
    mpos = mousepos.position
    xmpos = mpos[0]
    ympos = mpos[1]
    print("X: " +  str(xmpos) + ", " "Y: " + str(ympos))

    root.after(1000, mouse_position) # repiting loop after 1s


root = tkinter.Tk()
root.resizable(width = True, height = True)
root.geometry(camset.WINDOW_SIZE)
root.maxsize(width = 1280, height = 720) # Max size is the original image size
root.minsize(width = 160, height = 90)
root.configure(bg = camset.BACKGROUND)
root.title('camcat ' + version)
root.protocol('WM_DELETE_WINDOW', close_window)
root.update()
root.after(2000, resize) # starts loop after 2s
root.after(2000, mouse_position) # starts loop after 2s


# zjisti velikost obrazovky 
scrx = root.winfo_screenwidth()
scry = root.winfo_screenheight()
xframe = scrx / 10
yframe = scrx / 4

# urcovani polohy pro obrazky
x_1 = xframe * 1 # "*1" tu nemusi byt
x_2 = xframe * 2
x_3 = xframe * 3
x_4 = xframe * 4
x_5 = xframe * 5
x_6 = xframe * 6
x_7 = xframe * 7
x_8 = xframe * 8
x_9 = xframe * 9
x_10 = xframe * 10 # misto "* 10" tu muze byt "scrx"

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


root.mainloop()