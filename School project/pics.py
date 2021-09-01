import tkinter as tk 
from tkinter import Text, font, messagebox, Label, Entry, Button, Label
from PIL import ImageTk, Image
import os
import pickle

bat = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/batteries.jpg')
bat = bat.resize((100, 100), Image.ANTIALIAS)
bat_pic = ImageTk.PhotoImage(bat)


bread = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/bread.jpg')
bread = bread.resize((100, 100), Image.ANTIALIAS)
bread_pic = ImageTk.PhotoImage(bread)


cereal = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/cereal.jpg')
cereal = cereal.resize((100, 100), Image.ANTIALIAS)
cereal_pic = ImageTk.PhotoImage(cereal)


cheese = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/cheese.jpg')
cheese = cheese.resize((100, 100), Image.ANTIALIAS)
cheese_pic = ImageTk.PhotoImage(cheese)


choco = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/choco.jpg')
choco = choco.resize((100, 100), Image.ANTIALIAS)
choco_pic = ImageTk.PhotoImage(choco)


water = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/water.jpg')
water = water.resize((100, 100), Image.ANTIALIAS)
water_pic = ImageTk.PhotoImage(water)


milk = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/milk.jpg')
milk = milk.resize((100, 100), Image.ANTIALIAS)
milk_pic = ImageTk.PhotoImage(milk)


oil = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/oil.jpg')
oil = oil.resize((100, 100), Image.ANTIALIAS)
oil_pic = ImageTk.PhotoImage(oil)


salt = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/salt.jpg')
salt = salt.resize((100, 100), Image.ANTIALIAS)
salt_pic = ImageTk.PhotoImage(salt)


soap = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/soap.jpg')
soap = soap.resize((100, 100), Image.ANTIALIAS)
soap_pic = ImageTk.PhotoImage(soap)


tissues = Image.open(f'C:/Users/{os.getlogin()}/Downloads/School project/Pics/tissues.jpg')
tissues = tissues.resize((100, 100), Image.ANTIALIAS)
tissues_pic = ImageTk.PhotoImage(tissues)