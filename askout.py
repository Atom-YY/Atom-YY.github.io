import ctypes
import pygame
import time
import threading
import keyboard  # Install this with: pip install keyboard
from win32gui import FindWindow, FindWindowEx, SendMessage
from win32con import LVM_GETITEMCOUNT, LVM_SETITEMPOSITION, GWL_STYLE, LVS_AUTOARRANGE, SM_CXSCREEN, SM_CYSCREEN

pygame.mixer.init()
pygame.mixer.music.load('recording3.mp3')  
pygame.mixer.music.play(-1)

zm_wnd = FindWindow('Program', None)
bz_wnd = FindWindowEx(zm_wnd, 0, 'SHELLDLL_DefView', None)
tb_wnd = FindWindowEx(bz_wnd, 0, 'SysListView32', 'FolderView')

user32 = ctypes.windll.user32
dwStyle = user32.GetWindowLongW(tb_wnd, GWL_STYLE)
if dwStyle & LVS_AUTOARRANGE:
    user32.SetWindowLongW(tb_wnd, GWL_STYLE, dwStyle & ~LVS_AUTOARRANGE)

count = SendMessage(tb_wnd, LVM_GETITEMCOUNT)
CX = user32.GetSystemMetrics(SM_CXSCREEN)
CY = user32.GetSystemMetrics(SM_CYSCREEN)

love = [
    [868 * CX // 1920, 316 * CY // 1080],
    [730 * CX // 1920, 207 * CY // 1080],
    [591 * CX // 1920, 221 * CY // 1080],
    [515 * CX // 1920, 327 * CY // 1080],
    [542 * CX // 1920, 449 * CY // 1080],
    [610 * CX // 1920, 624 * CY // 1080],
    [723 * CX // 1920, 746 * CY // 1080],
    [870 * CX // 1920, 814 * CY // 1080],
    [1130 * CX // 1920, 626 * CY // 1080],
    [1219 * CX // 1920, 485 * CY // 1080],
    [1225 * CX // 1920, 328 * CY // 1080],
    [1156 * CX // 1920, 225 * CY // 1080],
    [1012 * CX // 1920, 217 * CY // 1080]
]

# Graceful shutdown flag
running = True

def monitor_exit():
    global running
    keyboard.wait('esc')  # Press ESC to quit
    running = False
    pygame.mixer.music.stop()
    print("Program stopped.")

threading.Thread(target=monitor_exit, daemon=True).start()

# Main loop
while running:
    for i in range(count):
        if i < len(love):
            SendMessage(tb_wnd, LVM_SETITEMPOSITION, i, (love[i][1] << 16) + love[i][0])
    time.sleep(1)
