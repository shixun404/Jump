import PIL
import pyautogui
import numpy as np
from PIL import Image
import cv2
print(pyautogui.position())
print( pyautogui.size())
im1 = pyautogui.screenshot()
im1 = np.array(im1)
print(im1.shape)
# 55, 55, 96
# x = 245, y=199
# x=589, y=662
chess_color = np.array([55, 55, 96])
# 左上角坐标
x_start = 227
y_start = 178
# 右下角坐标
x_end = 542
y_end = 644

def find_next(im, x_start, x_end, y_start, y_end, y_c, x_c):
    t = []
    gap = 20#20
    gap_ = 15 #15
    t.append(int(im[y_start, x_start]))
    t = np.array(t)
    c = []
    x = -1
    y = -1
    for i in range(y_start, y_end):
        for j in range(x_start, x_end):
            if abs(x_c - j) < 40:
                continue
            if  abs(int(im[i,j]) - t[0]) > gap :
                tmp = 0
                for jj in range(j, x_end):
                    if im[i, jj] > 0:
                        tmp += 1
                    else:
                        break
                c.append(255)
                x = int(tmp / 2) + j
                y = i
                break
        if x > 0:
            break
    x_ = x
    y_ = y
    if x > x_c:
        y = int(-59 / 106 * (x - x_c)) + y_c
    else:
        y = int(59 / 106 * (x - x_c)) + y_c
    # for i in range(y, y_end):
    #     if abs(int(im[i,x_]) - c[0]) > gap_:
    #         y_ = i
    #         break  
    #     for j in range(x_, x_start, -1):
    #         if abs(int(im[i,j]) - c[0]) > gap_ :
    #             x_ = j + 1
    #             break
    x__ = x_
    y__ = y_
    while(True):
        flag = True
        x_ += 1
        if int((im[y_, x_] + im[y_ + 1, x_] + im[y_ + 2, x_] + im[y_ + 3, x_]) / 4) > 0:
            flag = False
        if flag:
            break
        for j in range(4):
            if im[y_ + j, x_] == 255:
                y_ = y_ + j
                break
    while(True):
        flag = True
        x__ -= 1
        if int((im[y__, x__] + im[y__ + 1, x__] + im[y__ + 2, x__] + im[y__ + 3, x__]) / 4) > 0:
            flag = False
        if flag:
            break
        for j in range(4):
            if im[y__ + j, x__] == 255:
                y__ = y__ + j
                break
    
    return int(y_ * 0.6 + y * 0.1 + y__ * 0.3),x
# def find_next(im, x_start, x_end, y_start, y_end, y_c, x_c):
#     t = []
#     gap = 20#20
#     gap_ = 15 #15
#     t.append(int(im[y_start, x_start, 0]))
#     t.append(int(im[y_start, x_start, 1]))
#     t.append(int(im[y_start, x_start, 2]))
#     t = np.array(t)
#     c = []
#     x = -1
#     y = -1
#     for i in range(y_start, y_end):
#         for j in range(x_start, x_end):
#             if abs(x_c - j) < 40:
#                 continue
#             if  abs(int(im[i,j, 0]) - t[0]) > gap or abs(int(im[i,j, 1]) - t[1]) > gap or abs(int(im[i,j, 2]) - t[2]) > gap:
                
#                 c.append(int(im[i + 5,j + 5,0]))
#                 c.append(int(im[i + 5,j + 5,1]))
#                 c.append(int(im[i + 5,j + 5,2]))
#                 x = j + 5 # 5
#                 y = i + 5 #5
#                 break
#         if x > 0:
#             break
#     c = np.array(c)
#     x_ = x
#     y_ = y
#     print(x, y)
#     for i in range(y, y_end):
#         if abs(int(im[i,x_, 0]) - c[0]) > gap_ or abs(int(im[i,x_, 1]) - c[1]) > gap_ or abs(int(im[i,x_, 2]) - c[2]) > gap_:
#             y_ = i
#             break  
#         for j in range(x_, x_start, -1):
#             if abs(int(im[i,j, 0]) - c[0]) > gap_ or abs(int(im[i,j, 1]) - c[1]) > gap_ or abs(int(im[i,j, 2]) - c[2]) > gap_:
#                 x_ = j + 1
#                 break
    
#     return y_, x

def find_curr(im, x_start, x_end, y_start, y_end):
    x = -1
    y = -1
    gap = 10 #10
    im = im.astype(int)
    for i in range(y_end, y_start, -1):
        y = i
        for j in range(x_start, x_end):
            tmp = (im[i-1, j] + im[i - 2, j] + im[i-3, j] + im[i-4, j] + im[i-5, j] +  im[i-6, j] +  im[i-7, j]) / 7
            if abs(int(tmp[0]) - 55) < gap and abs(int(tmp[1]) - 55) < gap and abs(int(tmp[2]) - 96) < gap:
                # if abs(int(im[i - 1,j, 0]) - 55) < gap and abs(int(im[i - 1,j, 1]) - 55) < gap and abs(int(im[i - 1,j, 2]) - 96) < gap:
                x = j #5
                break
        if x > 0:
            break
    y -= 4
    # for j in range(x_start, x_end):
    #     for i in range(y_start, y_end):
    #         if abs(int(im[i,j, 0]) - 55) < gap and abs(int(im[i,j, 1]) - 55) < gap and abs(int(im[i,j, 2]) - 96) < gap:
    #             y = i
    #             break
    #     if y > 0:
    #         break
    return y, x + 4
        

            
k = 0
kk = 0
import time
while True:
    kk += 1
    im1 = pyautogui.screenshot() #x, y, w, h
    im1 = np.array(im1)
    im2 = im1
    
    im2 = cv2.GaussianBlur(im2,(5,5),0)  
    im2 = cv2.Canny(im2, 1, 10) 
    
    # template = cv2.imread('a.png', 0) 
    # im3 = im1[y_start:y_end, x_start:x_end]
    # # matchTemplate 函数：在模板和输入图像之间寻找匹配,获得匹配结果图像 
    # # minMaxLoc 函数：在给定的矩阵中寻找最大和最小值，并给出它们的位置
    # res = cv2.matchTemplate(im3,template,cv2.TM_CCOEFF_NORMED)
    # min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
    # print(min_val, max_val, min_loc, max_loc)
    # assert 0
    # assert 0
    y_1, x_1 = find_curr(im1,x_start, x_end, y_start, y_end)
    y_2, x_2 = find_next(im2,x_start, x_end, y_start, y_end, y_1, x_1)
    print("curr y: ", y_1,"curr x: ", x_1)
    print("next y: ", y_2,"next x: ", x_2)
    d = np.sqrt((y_1 - y_2) ** 2 + (x_1 - x_2) ** 2)
    print("distance: ", d)
    a = 1.17 * 1.045
    q = 1.03 - 0.23 * (1 - np.sqrt(d) / np.sqrt(145)) ** 2
    d *= q * 0.00279 * a
    t = d
    if d < 135:
        t *= 0.95
    if d > 250:
        t *= 1.05
    
    t1 = time.time()
    pyautogui.mouseDown(x_start, y_start, button='left')
    while(True):
        if abs(time.time() - t1) > t:
            break
    # if d < 90:
    #     time.sleep(d*0.00279 * 0.75 * a)
    # elif d < 105:
    #     time.sleep(d*0.00279 * 0.88 * a)
    # elif d < 135:
    #     time.sleep(d*0.00279 * 0.94 * a)
    # elif d > 190:
    #     time.sleep(d*0.00279 * 1.03 * a)
    # elif d <60:
    #     time.sleep(d*0.00279 * 0.65* a)
    # else:
    #     time.sleep(d*0.00277 * a)
    
    pyautogui.mouseUp(x_start, y_start, button='left')
    t1 = time.time()
    while(True):
        if time.time() - t1 > 2.4:
            break
    for i in range(5):
        for j in range(5):
            im1[y_1 - i,x_1 - j] = np.array([255,255,255])
            im1[y_1 + i,x_1 - j] = np.array([255,255,255])
            im1[y_1 + i,x_1 + j] = np.array([255,255,255])
            im1[y_1 - i,x_1 + j] = np.array([255,255,255])
            im2[y_1 - i,x_1 - j] = 255
            im2[y_1 + i,x_1 - j] = 255
            im2[y_1 + i,x_1 + j] = 255
            im2[y_1 - i,x_1 + j] = 255
    for i in range(5):
        for j in range(5):
            # im1[y_2 - i,x_2 - j] = np.array([255,255, 255])
            # im1[y_2 + i,x_2 - j] = np.array([255,255,255])
            # im1[y_2 + i,x_2 + j] = np.array([255,255,255])
            # im1[y_2 - i,x_2 + j] = np.array([255,255,255])
            im1[y_2 - i,x_2 - j] = np.array([0,0,0])
            im1[y_2 + i,x_2 - j] = np.array([0,0,0])
            im1[y_2 + i,x_2 + j] = np.array([0,0,0])
            im1[y_2 - i,x_2 + j] = np.array([0,0,0])
            im2[y_2 - i,x_2 - j] = 255
            im2[y_2 + i,x_2 - j] = 255
            im2[y_2 + i,x_2 + j] = 255
            im2[y_2 - i,x_2 + j] = 255
    im = Image.fromarray(im1[y_start:y_end, x_start:x_end])
    im.save(f"./fig/{k}.png", format='png')
    im = Image.fromarray(im2[y_start:y_end, x_start:x_end])
    im.save(f"./fig1/{k}.png", format='png')
    k += 1
    if k == 5:
        k = 0
    
    
    
    
    
