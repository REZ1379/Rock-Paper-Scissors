from tkinter import *
from tkinter import messagebox as ms
import random
Win = Tk()
Win.title("Rock, Paper, Scissors")
Win.geometry("300x450")
Win.resizable(width=False, height=False)
Win.configure(bg="#afc5e0")

FirstFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
FirstFrame.pack(side="top")
SecondFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
SecondFrame.pack(side="top")
ThirdFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
ThirdFrame.pack(side="top")
FourthFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
FourthFrame.pack(side="top")
FifthFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
FifthFrame.pack(side="top")
SixthFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
SixthFrame.pack(side="top")
SeventhFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
SeventhFrame.pack(side="top")
EighthFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
EighthFrame.pack(side="top")
NinthFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
NinthFrame.pack(side="top")
TenthFrame = Frame(Win, width=300, height=50, bg="#afc5e0")
TenthFrame.pack(side="top")

Bt1 = Button(FirstFrame, text="Rock", width=15, bg="#636061", command=lambda: Rock())
Bt1.pack(padx=10, pady=10)
Bt2 = Button(SecondFrame, text="Paper", width=15, command=lambda: Paper())
Bt2.pack(padx=10, pady=1)
Bt3 = Button(ThirdFrame, text="Scissors", width=15, bg="#ff3503", command=lambda: Scissors())
Bt3.pack(padx=10, pady=10)
Bt4 = Button(SixthFrame, text="", width=20, bg="#0c0e24", fg="white")
Bt4.pack(padx=10, pady=10)
Bt5 = Button(NinthFrame, text="", width=20, bg="#0c0e24", fg="white")
Bt5.pack(padx=10, pady=10)
Bt6 = Button(TenthFrame, text="Clear", width=5, bg="#0c0e24", fg="white", command=lambda: Clear())
Bt6.pack(padx=5, pady=1)
Bt7 = Button(TenthFrame, text="info", width=5, bg="#0c0e24", fg="white", command=lambda: info())
Bt7.pack(padx=5, pady=1)

Lb1 = Label(FifthFrame, text="Computer Move :", bg="#7da3d1")
Lb1.pack()
Lb2 = Label(EighthFrame, text="Result :", bg="#7da3d1")
Lb2.pack()


def Rock():
    Num = random.randint(0, 2)
    if Num == 0:
        Bt4["text"] = "Rock"
        Bt5["text"] = "Draw!"
    elif Num == 1:
        Bt4["text"] = "Paper"
        Bt5["text"] = "You Lose!"
    elif Num == 2:
        Bt4["text"] = "Scissors"
        Bt5["text"] = "You Win!"


def Paper():
    Num = random.randint(0, 2)
    if Num == 0:
        Bt4["text"] = "Rock"
        Bt5["text"] = "You Win!"
    elif Num == 1:
        Bt4["text"] = "Paper"
        Bt5["text"] = "Draw!"
    elif Num == 2:
        Bt4["text"] = "Scissors"
        Bt5["text"] = "You Lose!"


def Scissors():
    Num = random.randint(0, 2)
    if Num == 0:
        Bt4["text"] = "Rock"
        Bt5["text"] = "You Lose!"
    elif Num == 1:
        Bt4["text"] = "Paper"
        Bt5["text"] = "You Win!"
    elif Num == 2:
        Bt4["text"] = "Scissors"
        Bt5["text"] = "Draw!"


def Clear():
    Bt4["text"] = ""
    Bt5["text"] = ""


def info():
    ms.showinfo("info", "Created by \"Reza Rafiee\".09-Mar-22")


Win.mainloop()
