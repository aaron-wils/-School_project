import tkinter as tk 
from tkinter import Text, font, messagebox, Label, Entry, Button, Label
from PIL import ImageTk, Image
import os
import pickle


p = os.path.realpath(__file__)
r = p.split("\\")
p = ''
for x in range((len(r) -1)):
    p += f'{r[x]}\\'

if os.path.isdir(f'{p}\data files'):
    pass

else:
    os.chdir(p)
    os.makedirs('data files')


os.chdir(f'{p}\data files')


def login_details():

    file=open("log.dat","rb")
    read=pickle.load(file)
    global usr 
    usr = user_name.get()
    pswrd = password.get()
    val = 0
    for i in read:
        if usr == i:
            if read[usr] == pswrd:
                print('Login Sucessfull')
                val +=2
                pics()
                break
            else:
                val += 1
                break
        else:
            val = 0
    if val == 1:
        tk.messagebox.showinfo(message="Wrong Password")
    elif val == 0:
        tk.messagebox.showinfo(message="Username or password not found")




def new_acc():
    file=open("log.dat","rb")
    read=pickle.load(file)
    usr = user_name.get()
    pswrd = password.get()
    file.close()
    if usr in read:
        a=True
    else:
        a=False
    if(a==True):
        tk.messagebox.showinfo(message="User already exist")
    else:
        if (user_name.get() or password.get()) == '':
            tk.messagebox.showinfo(message="Please Enter a Valid username or password")     
        else:
            file_write=open("log.dat","wb")
            read[f'{user_name.get()}'] = f'{password.get()}'
            pickle.dump(read, file_write)
            file_write.close()
            tk.messagebox.showinfo(message="New user created")                

items = []
number = []
total_price_list = []
price_list = []

price_1 = {'Soap':8,'Oil' :38,'Batteries' :7,'Cereal' :15,
  'Chocolate' :4, 'Cheese' :7, 'Salt' :4, 'Milk' :12, 'Tissues' :15,
   'Bread' :6, 'Egg' :18, 'Rice' :30, 'Apple' :4, 'Banana' :3, 'Orange' :5,
    'Strawberry' :6}

def item_add(item):
    if item in items:
        for x in range(len(items)):
            if item == items[x]:
                number[x] += 1
                total_price_list[x] += price_1[item]
            else:
                continue
    else:
        items.append(item)
        number.append(1)
        total_price_list.append(price_1[item])
        price_list.append(price_1[item])


def yes(event):
    print('hello hello')



def show_items():
    for widget in label_2.winfo_children():
        widget.destroy()

    label_top = tk.Label(label_2, text = 'Items', bg = '#413c69', fg = '#ffefa1', font = highlightFont)
    label_top.grid(row = 0, column = 0)

    label_2top = tk.Label(label_2, text = '  Qty.   ', bg = '#413c69', fg = '#ffefa1', font = highlightFont)
    label_2top.grid(row = 0, column = 1)

    label_3top = tk.Label(label_2, text = 'Item Price   ', bg = '#413c69', fg = '#ffefa1', font = highlightFont)
    label_3top.grid(row = 0, column = 2)

    label_3top = tk.Label(label_2, text = 'Total Price', bg = '#413c69', fg = '#ffefa1', font = highlightFont)
    label_3top.grid(row = 0, column = 3)
    x = 1
    y = 0
    for item in items:
        label = tk.Label(label_2, text = item, bg = '#413c69', fg = '#ffefa1', font = Font2)
        label.grid(row = x, column = y)
        x+=1

    show_number()
    item_price()
    total_item_price()


def show_number():
    x = 1
    y = 1
    for num in number:
        label = tk.Label(label_2, text = f'x{num}', bg = '#413c69', fg = '#ffefa1', font = Font2)
        label.grid(row = x, column = y)
        x+=1
    
def total_item_price():
    x = 1
    y = 3
    for price in total_price_list:
        label = tk.Label(label_2, text = f'{price} aed', bg = '#413c69', fg = '#e0c43a', font = Font3)
        label.grid(row = x, column = y)
        x+=1
def item_price():
    x = 1
    y = 2
    for price in price_list:
        label = tk.Label(label_2, text = price, bg = '#413c69', fg = '#ffefa1', font = Font2)
        label.grid(row = x, column = y)
        x+=1

#append item to list( items )
def soap_click():
    item_add('Soap')
    show_items()
def oil_click():
    item_add('Oil')
    show_items()
def batteries_click():
    item_add('Batteries')
    show_items()
def cereal_click():
    item_add('Cereal')
    show_items()
def chocolate_click():
    item_add('Chocolate')
    show_items()
def cheese_click():
    item_add('Cheese')
    show_items()
def salt_click():
    item_add('Salt')
    show_items()
def milk_click():
    item_add('Milk')
    show_items()
def tissues_click():
    item_add('Tissues')
    show_items()
def bread_click():
    item_add('Bread')
    show_items()
def eggs_click():
    item_add('Egg')
    show_items()
def rice_click():
    item_add('Rice')
    show_items()
def apple_click():
    item_add('Apple')
    show_items()
def banana_click():
    item_add('Banana')
    show_items()
def orange_click():
    item_add('Orange')
    show_items()
def strawberry_click():
    item_add('Strawberry')
    show_items()

                    
def pics():
    for widget in main.winfo_children():
        widget.destroy()
    global label_2
    label_2 = tk.Frame(main, bg = '#413c69')
    label_2.place(relwidth= 0.6, relheight= 1, relx= 0.7, rely = 0)

    global soap_pic
    global bat_pic
    global bread_pic
    global cereal_pic
    global cheese_pic
    global choco_pic
    global water_pic
    global milk_pic
    global oil_pic
    global salt_pic
    global tissues_pic
    global egg_pic
    global rice_pic
    global apple_pic
    global bannana_pic
    global orange_pic
    global straw_pic



    bat = Image.open(f'{p}\Pics\\batteries.jpg')
    bat = bat.resize((100, 100), Image.ANTIALIAS)
    bat_pic = ImageTk.PhotoImage(bat)


    bread = Image.open(f'{p}\Pics\\bread.jpg')
    bread = bread.resize((100, 100), Image.ANTIALIAS)
    bread_pic = ImageTk.PhotoImage(bread)


    cereal = Image.open(f'{p}\Pics\\cereal.jpg')
    cereal = cereal.resize((100, 100), Image.ANTIALIAS)
    cereal_pic = ImageTk.PhotoImage(cereal)


    cheese = Image.open(f'{p}\Pics\\cheese.jpg')
    cheese = cheese.resize((100, 100), Image.ANTIALIAS)
    cheese_pic = ImageTk.PhotoImage(cheese)


    choco = Image.open(f'{p}\Pics\\choco.jpg')
    choco = choco.resize((100, 100), Image.ANTIALIAS)
    choco_pic = ImageTk.PhotoImage(choco)


    water = Image.open(f'{p}\Pics\\water.jpg')
    water = water.resize((100, 100), Image.ANTIALIAS)
    water_pic = ImageTk.PhotoImage(water)


    milk = Image.open(f'{p}\Pics\\milk.jpg')
    milk = milk.resize((100, 100), Image.ANTIALIAS)
    milk_pic = ImageTk.PhotoImage(milk)

    
    oil = Image.open(f'{p}\Pics\\oil.jpg')
    oil = oil.resize((100, 100), Image.ANTIALIAS)
    oil_pic = ImageTk.PhotoImage(oil)


    salt = Image.open(f'{p}\Pics\\salt.jpg')
    salt = salt.resize((100, 100), Image.ANTIALIAS)
    salt_pic = ImageTk.PhotoImage(salt)


    soap = Image.open(f'{p}\Pics\\soap.jpg')
    soap = soap.resize((100, 100), Image.ANTIALIAS)
    soap_pic = ImageTk.PhotoImage(soap)


    tissues = Image.open(f'{p}\Pics\\tissues.jpg')
    tissues = tissues.resize((100, 100), Image.ANTIALIAS)
    tissues_pic = ImageTk.PhotoImage(tissues)

    egg = Image.open(f'{p}\Pics\\egg.jpg')
    egg = egg.resize((100, 100), Image.ANTIALIAS)
    egg_pic = ImageTk.PhotoImage(egg)

    rice = Image.open(f'{p}\Pics\\rice.jpg')
    rice = rice.resize((100, 100), Image.ANTIALIAS)
    rice_pic = ImageTk.PhotoImage(rice)

    
    apple = Image.open(f'{p}\Pics\\apple.jpg')
    apple = apple.resize((100, 100), Image.ANTIALIAS)
    apple_pic = ImageTk.PhotoImage(apple)

    bannana = Image.open(f'{p}\Pics\\banana.jpg')
    bannana = bannana.resize((100, 100), Image.ANTIALIAS)
    bannana_pic = ImageTk.PhotoImage(bannana)

    orange = Image.open(f'{p}\Pics\\orange.jpg')
    orange = orange.resize((100, 100), Image.ANTIALIAS)
    orange_pic = ImageTk.PhotoImage(orange)

    straw = Image.open(f'{p}\Pics\\strawberry.jpg')
    straw = straw.resize((100, 100), Image.ANTIALIAS)
    straw_pic = ImageTk.PhotoImage(straw)


    sop = tk.Button(main, image = soap_pic, command = soap_click)
    sop.place(relx= 0.02, rely = 0.02)

    oill = tk.Button(main, image = oil_pic,command = oil_click)
    oill.place(relx= 0.1, rely = 0.02)

    batt = tk.Button(main, image = bat_pic,command =batteries_click)
    batt.place(relx= 0.18, rely = 0.02)

    cer = tk.Button(main, image = cereal_pic,command = cereal_click)
    cer.place(relx= 0.26, rely = 0.02)

    choc = tk.Button(main, image = choco_pic,command = chocolate_click)
    choc.place(relx= 0.02, rely = 0.2)

    cheze = tk.Button(main, image = cheese_pic,command = cheese_click)
    cheze.place(relx= 0.1, rely = 0.2)

    sal = tk.Button(main, image = salt_pic,command = salt_click)
    sal.place(relx= 0.18, rely = 0.2)

    miluk = tk.Button(main, image = milk_pic,command = milk_click)
    miluk.place(relx= 0.26, rely = 0.2)

    tizzu = tk.Button(main, image = tissues_pic,command = tissues_click)
    tizzu.place(relx= 0.02, rely = 0.37)

    brud = tk.Button(main, image = bread_pic,command = bread_click)
    brud.place(relx= 0.1, rely = 0.37)

    eug = tk.Button(main, image = egg_pic,command = eggs_click)
    eug.place(relx= 0.18, rely = 0.37)

    rize = tk.Button(main, image = rice_pic,command = rice_click)
    rize.place(relx= 0.26, rely = 0.37)

    appul = tk.Button(main, image = apple_pic,command = apple_click)
    appul.place(relx= 0.02, rely = 0.53)

    bana = tk.Button(main, image = bannana_pic,command = banana_click)
    bana.place(relx= 0.1, rely = 0.53)

    oran = tk.Button(main, image = orange_pic,command = orange_click)
    oran.place(relx= 0.18, rely = 0.53)

    berry = tk.Button(main, image = straw_pic,command = strawberry_click)
    berry.place(relx= 0.26, rely = 0.53)



r = tk.Tk()
r.title('Taxify')
r.state('zoomed')
r.iconbitmap(f'{p}\\Pics\\money.ico')

highlightFont = font.Font(family='Helvetica CY', size=17)
Font2 = font.Font(family = 'Century Gothic', size = 17)
Font3 = font.Font(family = 'Century Gothic', size = 17, weight = 'bold')
Font4 = font.Font(family = 'Century Gothic', size = 25)

canvas = tk.Canvas(r, height = 1920, width = 1080, bg = '#bfebff')
canvas.pack(fill = tk.BOTH)

img = Image.open(f'{p}\\poly.png')
img = img.resize((1920, 1080), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(img)
main = Label(canvas, image = bg)
main.place(x= 0, y = 0, relwidth = 1, relheight = 1)




ta = Image.open(f'{p}\\Pics\\taxx.jpg')
ta = ta.resize((200, 200), Image.ANTIALIAS)
ta_pic = ImageTk.PhotoImage(ta)

ta_label = tk.Label(main, image = ta_pic, bg = '#55adea')
ta_label.place(relx= 0.42, rely = 0.1)


def on_click1(event):
    l = len(user_name.get())
    user_name.delete(0, l)
    user_name.configure(fg = 'black')

def on_click2(event):
    l = len(password.get())
    password.delete(0, l)
    password.configure(fg = 'black', show="*")

user_name = Entry(main, width = 40, bg= "#FFFFFF", fg = 'grey', font = highlightFont)
user_name.insert(0, 'Username')
user_name.bind('<Button-1>', on_click1)
user_name.place(relwidth= 0.3, relheight= 0.05, relx= 0.335, rely = 0.35)

password = Entry(main, width = 40, bg= "#FFFFFF", fg = 'grey',font = highlightFont )
password.insert(0, 'Password')
password.bind('<Button-1>', on_click2)
password.place(relwidth= 0.3, relheight= 0.05, relx= 0.335, rely = 0.43)


login = tk.Button(main,text = 'Login', bg = '#bfebff',
                            activebackground= '#413c69',activeforeground = '#ffefa1', font = highlightFont, command = login_details)
login.place(relwidth= 0.2, relheight= 0.08, relx= 0.39, rely = 0.5)                  


signup = tk.Button(main,text = 'Sign Up', padx = 10, pady = 5, bg = '#bfebff',
                            activebackground= '#413c69',activeforeground = '#ffefa1',font = highlightFont,  command = new_acc)
signup.place(relwidth= 0.2, relheight= 0.08, relx= 0.39, rely = 0.6)                    


r.minsize(1920, 1080)
r.maxsize(1920, 1080)
r.mainloop()
