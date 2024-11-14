from playsound import playsound   
from tkinter import *
from time import *
import time
import math

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

root = Tk()
root.geometry('1000x800')
root.register(0,0)
bg = PhotoImage(file="background.png")
root.title('Đồng Hồ Kĩ Thuật Số')


cv = Canvas (root, width=1000,height=562)
cv.pack(fill= "both", expand=True)

cv.create_image(0, 0, image = bg, anchor = "nw")

Label(root,text='TIMER',font=("JetBrains Mono Medium",40),bg='lightgray',fg='darkviolet').place(x=440,y=30)
clock_label = Label(root, font=("Digital-7",50), text='',fg='green',bg='black')
clock_label.place(x=380,y=155)

day_label = Label(root, font=("Ink Free",30), text='',fg='green',bg='black')
day_label.place(x=260,y=220)

def makecenter(root):
  root.update_idletasks()
  width = root.winfo_width()
  height =  root.winfo_height()
  x = (root.winfo_screenwidth() // 2) - (width // 2)
  y = (root.winfo_screenheight() // 2) - (height // 2)
  root.geometry('{}x{}+{}+{}'.format(width,height, x, y))
makecenter(root)

def clock():
    clock_string = strftime('%H:%M:%S %p')   
    clock_label.config(text= clock_string)
    clock_label.after(1000,clock)
clock()

def datetime():
  day_string = strftime('%A, %B %d, %Y')
  day_label.config(text = day_string)
  
datetime()

sec = StringVar()
Entry(root, textvariable= sec, width=2, font=("Digital-7",30), bg="cadetblue",fg="aqua").place(x=675,y=440)
sec.set('00')

mins = StringVar()
Entry(root, textvariable= mins, width=2, font=("Digital-7",30), bg="cadetblue",fg="aqua").place(x=594,y=440)
mins.set('00')

hrs = StringVar()
Entry(root, textvariable= hrs, width=2, font=("Digital-7",30), bg="cadetblue",fg="aqua").place(x=500,y=440)
hrs.set('00')


def countdown():
  times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
  while times > -1:
    minute,second = (times // 60 , times % 60)

    hour = 0
    if minute > 60:
      hour , minute = (minute // 60 , minute % 60)

    sec.set(second)
    mins.set(minute)
    hrs.set(hour)

    root.update()
    time.sleep(1)

    if(times==0):
      playsound('Loud_Alarm_Clock_Buzzer.mp3')
      sec.set('00')
      mins.set('00')
      hrs.set('00')
    
    times -= 1

def brush():
  hrs.set("00")
  mins.set("02")
  sec.set("00")

def eggs():
  hrs.set("00")
  mins.set("10")
  sec.set("00")

def face():
  hrs.set("00")
  mins.set("15")
  sec.set("00")


Label(root,text="hours",font="Arial 12", bg="cadetblue",fg="aqua").place(x=546,y=460)
Label(root,text="min",font="Arial 12", bg="cadetblue",fg="aqua").place(x=640,y=460)
Label(root,text="sec",font="Arial 12", bg="cadetblue",fg="aqua").place(x=721,y=460)

image1 = PhotoImage(file="brush.png")
Button(root, image= image1, bd=0, command=brush,bg="black").place(x= 575, y= 530)

image2 = PhotoImage(file="eggs.png")
Button(root, image= image2, bd=0, command=eggs,bg="black").place(x= 450, y= 530)

image3 = PhotoImage(file="face.png")
Button(root, image= image3, bd=0, command=face,bg="black").place(x= 325, y= 530)


Label(root, font=("JetBrains Mono Medium",18), text = 'Đặt Thời Gian:',bg='cyan',fg='deeppink').place(x=265,y=445)
Label(root, font=("JetBrains Mono Medium",22), text = 'Đếm Ngược',bg='black',fg="red" ).place(x=440,y=350)
Button(root, text='Bắt Đầu', bd='12', command=countdown, font=("JetBrains Mono Medium", 12 ),bg='deepskyblue',fg='crimson').place(x=470, y=680)


root.mainloop()