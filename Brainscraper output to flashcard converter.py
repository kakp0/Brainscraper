import time
import pyautogui as p
import pyperclip

f = open('insertNameOfFile.txt',encoding='utf-8')

counter = 0
lister = []


def new_card(list):
    pyperclip.copy(list[0])
    p.hotkey("ctrl", "v")
    p.press('tab')
    pyperclip.copy(list[1])
    p.hotkey("ctrl", "v")
    p.press('enter')
    pyperclip.copy(list[2])
    p.hotkey("ctrl", "v")
    p.press('tab')
    time.sleep(0.5)

time.sleep(4)
for line in f:
    if counter != 3:
        lister.append(line[0:-1])
        counter += 1


    else:
        new_card(lister)
        print(lister)
        counter = 0
        lister = []


new_card(lister)
print(lister)
counter = 0
lister = []
