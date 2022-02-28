from tkinter.constants import LEFT, SE, SW, X
from tkinter.font import names
from typing import Sized, Text
import numpy as np
import cv2 as cv
import tkinter.ttk
import os
import tkinter
from PIL import Image,ImageTk,ImageGrab
from tkinter import Label, filedialog
from pathlib import Path
import win32com.client



# 변수 선언

cap = cv.VideoCapture(0,cv.CAP_DSHOW)
# c_width=cap.get(cv.CAP_PROP_FRAME_WIDTH)
# c_height=cap.get(cv.CAP_PROP_FRAME_HEIGHT)
cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)
# print(c_width,c_height)
wid = 1
color = "black"
now_color = "검은색"
lastx1, lasty1 = 0, 0
lastx1, lasty1 = 0, 0

tts = win32com.client.Dispatch("SAPI.SpVoice")
# 카메라 출력
def show_frames():
   global h,w
   # Get the latest frame and convert into Image
   _, frame = cap.read()

   cv.rectangle(frame, (400, 210), (880, 510), (0, 0, 255), 3)
   cv2image= cv.cvtColor(frame,cv.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label3.imgtk = imgtk
   label3.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label3.after(20, show_frames)

# 카메라 저장
def snapshot():
    ret, frame = cap.read()
    img_frame = frame.copy()
    img_size = img_frame[210:510, 400:880]
    cv.imwrite('image.png', img_size)
    img_color = cv.imread('image.png', cv.IMREAD_COLOR)
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    ret,img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

    img2 = Image.fromarray(img_binary)
    img2 = img2.convert("RGBA")
    pixdata = img2.load()
    width, height = img2.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    img2.save('result.png', "PNG")
    os.remove('image.png') #여기서 image.png 파일을 제거함으로써 조건이 성립되도록 맞춤
    tts.Speak("저장되었습니다.")

# 파일 열기
def f_open():
    global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    global rot
    for label in frame1.winfo_children():
        if type(label) == Label : # just Label since you used a wildcard import to import tkinter
            label.destroy()
    rot =frame1.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
    my_image = ImageTk.PhotoImage(Image.open(frame1.filename),size=(1070,700))
    tkinter.Label(frame1,image=my_image).pack() #사진 view

# 파일 저장
def f_save():
    img_color = cv.imread(f"{rot}", cv.IMREAD_COLOR)
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    ret,img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
    img_r = Image.fromarray(img_binary)
    img_r = img_r.convert("RGBA")
    pixdata = img_r.load()
    width, height = img_r.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    img_r.save('result.png', "PNG")
    tts.Speak("저장되었습니다.")

# 페인트샵
def paint_shop():
    def paint_line(event):
        global lastx1, lasty1
        lastx1, lasty1 = event.x, event.y
        canvas.create_line(event.x, event.y, event.x + 0.5, event.y + 0.5, fill = "black", width = wid)

    def lining(event):
        global lastx1, lasty1
        canvas.create_line(lastx1, lasty1, event.x, event.y, fill = "black", width = wid)
        lastx1, lasty1 = event.x, event.y

    def scroll(event):
        global wid
        if wid < 5:
            if event.delta == 120:
                wid += 1
        if wid > 1:
            if event.delta == -120:
                wid -= 1

    canvas.bind("<B1-Motion>",lining)
    canvas.bind("<Button-1>",paint_line)
    canvas.bind("<MouseWheel>", scroll)
    canvas.pack()

# 캔버스 지우개
def all_clear():
        canvas.delete("all")

# 캔버스 저장
def save():
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    h = canvas.winfo_height() + y
    w = canvas.winfo_width() + x
    
    box = (x, y, w, h)
    img=ImageGrab.grab(box) #창의 크기만큼만 이미지저장
    saveas='capture.png'
    img.save(saveas)

    can_color = cv.imread(saveas, cv.IMREAD_COLOR)
    can_gray = cv.cvtColor(can_color, cv.COLOR_BGR2GRAY)
    _,can_binary = cv.threshold(can_gray, 127, 255, cv.THRESH_BINARY)
    can_r = Image.fromarray(can_binary)
    can_r = can_r.convert("RGBA")
    pixdata = can_r.load()
    width, height = can_r.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    can_r.save('result.png', "PNG")
    tts.Speak("저장되었습니다.")


window=tkinter.Tk()
window.title("digital signature")
window.geometry("1400x800")
window.resizable(False, False)

notebook=tkinter.ttk.Notebook(window, width=1340, height=700)
notebook.pack()

# 첫번째 탭(img)
frame1=tkinter.Frame(window)
notebook.add(frame1, text="image")
label1=tkinter.Label(frame1,width=1290,height=730)
b_open = tkinter.Button(frame1,text="open",command=f_open)
b_save = tkinter.Button(frame1,text="save",command=f_save)
b_save.pack(side="right",anchor="se",padx=10,pady=10)
b_open.pack(side="left",anchor="sw",padx=10,pady=10)

label1.pack()


# 두번째 탭(mouse)
frame2=tkinter.Frame(window)
notebook.add(frame2, text="mouse")
label2=tkinter.Label(frame2)
canvas=tkinter.Canvas(frame2,width=1200,height=650,bg="white",cursor="pencil")
paint_shop()
tkinter.Button(frame2, text = "clear", command = all_clear).pack(side="left", anchor="sw",padx=10,pady=10)
tkinter.Button(frame2,text="save",command = save).pack(side="right",anchor="se",padx=10,pady=10)
label2.pack()

# 3번째 탭(camera)
frame3=tkinter.Frame(window)
notebook.add(frame3, text="camera")
label3=tkinter.Label(frame3,width=1290,height=730)
b_snap=tkinter.Button(frame3,text="snapshot",command=snapshot).pack(side="bottom",anchor="s",fill=X,padx=10,pady=10)
show_frames()
label3.pack()


window.mainloop()