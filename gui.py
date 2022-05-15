from datetime import datetime
from distutils.log import error
import json
import tkinter as tk
import tkinter.messagebox as tkm
import meet
var=[]
window = tk.Tk()
window.title("classroom輔助程式")
window.iconbitmap('icon.ico')
subject = ['國','英','數','化學','物理','歷史','公民','美術','虎崗']
day =datetime.today().isoweekday()

def set_option():
    with open("schedule.json",'r',encoding="utf-8") as f:
        data = json.load(f)
        slist = data[str(day)]
    var = [tk.StringVar() for _ in range(7)]
    try:
        tnum = 0
        for i in var:
            if slist[tnum] == '':
                tnum += 1
                continue
            temp = i.set(subject[slist[tnum]])
            i = temp
            tnum += 1
    except:
        pass
    return var

def set_optionmenu():
    group = tk.LabelFrame(window,text="今日課表")
    group.grid(column=3,row=0,rowspan=7)
    for i in range(7):
        t = tk.OptionMenu(group, var[i], *subject)
        t.pack()
    # M1 = tk.OptionMenu(group, var[0], *subject)
    # M2 = tk.OptionMenu(group, var[1], *subject)
    # M3 = tk.OptionMenu(group, var[2], *subject)
    # M4 = tk.OptionMenu(group, var[3], *subject)
    # M5 = tk.OptionMenu(group, var[4], *subject)
    # M6 = tk.OptionMenu(group, var[5], *subject)
    # M7 = tk.OptionMenu(group, var[6], *subject)
    # M1.grid(column=3,row=0)
    # M2.grid(column=3,row=1)
    # M3.grid(column=3,row=2)
    # M4.grid(column=3,row=3)
    # M5.grid(column=3,row=4)
    # M6.grid(column=3,row=5)
    # M7.grid(column=3,row=6)

def setdefault():
    global e1,e2,e3,box1,box2
    T = tk.Label(window,text=" 請輸入學生Google帳號",font=('Arial',20))
    e1 = tk.Entry(window,width=20)
    e2 = tk.Entry(window,width=20,show='*')
    e3 = tk.Entry(window,width=20)
    t1 = tk.Label(window,text="帳號")
    t2 = tk.Label(window,text="密碼")
    t3 = tk.Label(window,text="班級")
    # t4 = tk.Label(window,text="(e.g. 208)")
    box1 = tk.Checkbutton(window,text="顯示密碼",command=toggle_password,onvalue=True,offvalue=False)
    box2 = tk.Checkbutton(window,text="記住密碼",onvalue=True,offvalue=False)
    b1 = tk.Button(window,text="啟動程式",command=button_click,bg='green',fg='white',width=15)
    box1.var = tk.BooleanVar()
    box1.config(variable=box1.var)
    box2.var = tk.BooleanVar()
    box2.config(variable=box2.var)

    T.grid(column=0,row=0,columnspan=2)
    t1.grid(column=0,row=1)
    t2.grid(column=0,row=2)
    t3.grid(column=0,row=3)
    # t4.grid(column=0,row=4)
    e1.grid(column=1,row=1)
    e2.grid(column=1,row=2)
    e3.grid(column=1,row=3)
    box1.grid(column=0,row=4,columnspan=2)
    box2.grid(column=0,row=5,columnspan=2)
    b1.grid(column=0,row=6,columnspan=2)

    try:
        with open('temp') as f:
            check = f.readline().strip()
            classnum = f.readline().strip()
            account = f.readline().strip()
            password = f.readline()
    except:
        pass
    e1.insert(0,account)
    e3.insert(0,classnum)
    print(type(check))
    if check=="True":
        box2.var.set(True)
    if password!='\n':
        e2.insert(0,password)

def button_click():
    account = e1.get()
    password = e2.get()
    classnum = e3.get()
    print(account)
    if(account==''):
        popup('info','請輸入帳號')
    elif(password==''):
        popup('info','請輸入密碼')
    else:
        with open('temp','w') as f:
            f.write(str(box2.var.get())+'\n')
            f.write(classnum+'\n')
            f.write(account+'\n')
            if box2.var.get():
                f.write(password)
        if(meet.google(account,password,classnum)==0):
            popup('error','現在不是上課時間')

def popup(type,text):
    if(type=="error"):
        tkm.showerror('錯誤',text)
    elif(type=='info'):
        tkm.showinfo('提醒',text)
        
def toggle_password():
    if box1.var.get():
        e2.config(show='')
    else:
        e2.config(show='*')

setdefault()
var = set_option()
set_optionmenu()

window.mainloop()