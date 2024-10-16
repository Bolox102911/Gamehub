from win32gui import *
from win32api import  *
from win32ui import *
from win32con import *
from win32file import *
from random import *
from time import *
import ctypes


def main():

    if MessageBox("WARNING THIS DOES NOT HARM YOUR PC THE V2 IS GONNA SO TAKE THIS A LAST CHANSE TO TRY TO USE THIS MALWARE WITHOUT DESTROYING MBR", "WARNING!", MB_ICONWARNING | MB_YESNO) == 7:
        return

    if MessageBox("ARE YOU SURE NO DAMAGE CAN BE SUED BY ME", "LAST WARNING!", MB_ICONWARNING | MB_YESNO) == 7:
        return


    if True:
        desk = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)
        w = GetSystemMetrics(0)
        h = GetSystemMetrics(1)
        sw = GetSystemMetrics(0)
        sh = GetSystemMetrics(1)
        a = GetSystemMetrics(SM_CXSCREEN)
        b = GetSystemMetrics(SM_CYSCREEN)
        for i in range(0, 1000):
                brush = CreateSolidBrush(RGB(
                        0,
                        255,
                        0,
                        ))
                PatBlt(desk, 0, 0, x, y, PATINVERT)
                PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
                BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
                StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
                StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCINVERT)
                DeleteObject(brush)
                Sleep(10)

        ()

    if True:
        desk = GetDC(0)
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)



        for i in range(10, 100):
            brush = CreateSolidBrush(RGB(
                255,
                255,
                255,
                ))
            SelectObject(desk, brush)
            PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
            DeleteObject(brush)
            Sleep(10)
    

main()



    



