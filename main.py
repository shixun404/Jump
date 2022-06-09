import PIL
import pyautogui
import numpy as np
from PIL import Image
print(pyautogui.position())
print( pyautogui.size())
im1 = pyautogui.screenshot()
im1 = np.array(im1)
print(im1.shape)
# 55, 55, 96
# x = 245, y=199
# x=589, y=662
chess_color = np.array([55, 55, 96])
x_start = 323
y_start = 255
x_end = 726
y_end = 838
def find_next(im, x_start, x_end, y_start, y_end, y_c, x_c):
    t = []
    gap = 20
    gap_ = 15
    t.append(int(im[y_start, x_start, 0]))
    t.append(int(im[y_start, x_start, 1]))
    t.append(int(im[y_start, x_start, 2]))
    t = np.array(t)
    c = []
    x = -1
    y = -1
    for i in range(y_start, y_end):
        for j in range(x_start, x_end):
            if abs(x_c - j) < 40:
                continue
            if  abs(int(im[i,j, 0]) - t[0]) > gap or abs(int(im[i,j, 1]) - t[1]) > gap or abs(int(im[i,j, 2]) - t[2]) > gap:
                
                c.append(int(im[i + 5,j + 5,0]))
                c.append(int(im[i + 5,j + 5,1]))
                c.append(int(im[i + 5,j + 5,2]))
                x = j + 5
                y = i + 5
                break
        if x > 0:
            break
    c = np.array(c)
    x_ = x
    y_ = y
    print(x, y)
    for i in range(y, y_end):
        if abs(int(im[i,x_, 0]) - c[0]) > gap_ or abs(int(im[i,x_, 1]) - c[1]) > gap_ or abs(int(im[i,x_, 2]) - c[2]) > gap_:
            y_ = i
            break  
        for j in range(x_, x_start, -1):
            if abs(int(im[i,j, 0]) - c[0]) > gap_ or abs(int(im[i,j, 1]) - c[1]) > gap_ or abs(int(im[i,j, 2]) - c[2]) > gap_:
                x_ = j + 1
                break
    
    return y_, x

def find_curr(im, x_start, x_end, y_start, y_end):
    x = -1
    y = -1
    gap = 10
    im = im.astype(int)
    for i in range(y_end, y_start, -1):
        for j in range(x_start, x_end):
            tmp = (im[i-1, j] + im[i - 2, j] + im[i-3, j] + im[i,j]) / 4
            if abs(int(tmp[0]) - 55) < gap and abs(int(tmp[ 1]) - 55) < gap and abs(int(tmp[2]) - 96) < gap:
                # if abs(int(im[i - 1,j, 0]) - 55) < gap and abs(int(im[i - 1,j, 1]) - 55) < gap and abs(int(im[i - 1,j, 2]) - 96) < gap:
                print(tmp)
                x = j + 5
                break
        if x > 0:
            break
    
    for j in range(x_start, x_end):
        for i in range(y_start, y_end):
            if abs(int(im[i,j, 0]) - 55) < gap and abs(int(im[i,j, 1]) - 55) < gap and abs(int(im[i,j, 2]) - 96) < gap:
                y = i
                break
        if y > 0:
            break
    return y, x
        

            
k = 0
import time
while True:
    im1 = pyautogui.screenshot()
    im1 = np.array(im1)
    y_1, x_1 = find_curr(im1,x_start, x_end, y_start, y_end)
    y_2, x_2 = find_next(im1,x_start, x_end, y_start, y_end, y_1, x_1)
    print("curr y: ", y_1,"curr x: ", x_1)
    print("next y: ", y_2,"next x: ", x_2)
    d = np.sqrt((y_1 - y_2) ** 2 + (x_1 - x_2) ** 2)
    print("distance: ", d)
    
    # pyautogui.MINIMUM_DURATION = d * 0.5
    pyautogui.mouseDown(x_start, y_start, button='left')
    if d < 90:
        time.sleep(d*0.00279 * 0.7)
    elif d < 105:
        time.sleep(d*0.00279 * 0.85)
    elif d < 120:
        time.sleep(d*0.00279 * 0.95)
    else:
        time.sleep(d*0.00279)
    pyautogui.mouseUp(x_start, y_start, button='left')
    time.sleep(1)
    for i in range(5):
        for j in range(5):
            im1[y_1 - i,x_1 - j] = np.array([255,255,255])
            im1[y_1 + i,x_1 - j] = np.array([255,255,255])
            im1[y_1 + i,x_1 + j] = np.array([255,255,255])
            im1[y_1 - i,x_1 + j] = np.array([255,255,255])
    for i in range(5):
        for j in range(5):
            im1[y_2 - i,x_2 - j] = np.array([0,0,0])
            im1[y_2 + i,x_2 - j] = np.array([0,0,0])
            im1[y_2 + i,x_2 + j] = np.array([0,0,0])
            im1[y_2 - i,x_2 + j] = np.array([0,0,0])
    im = Image.fromarray(im1[y_start:y_end, x_start:x_end])
    im.save(f"./fig/{k}.png", format='png')
    k += 1
    
    
    
    
    
