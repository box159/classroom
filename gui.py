from datetime import datetime
import time
from tkinter import font

from click import command
from soupsieve import select
import meet
import json
import tkinter as tk
import tkinter.messagebox as tkm
import cryptocode

window = tk.Tk()
window.title("classroom輔助程式")
window.iconbitmap('icon.ico')

icon = tk.PhotoImage(file="setting.png")
plus_img = tk.PhotoImage(file='plus.png')
minus_img = tk.PhotoImage(file='minus.png')
save_img = tk.PhotoImage(file='save.png')

with open('config.json','r',encoding='utf-8') as f :
    data = json.load(f)
    
    

week = ['星期一','星期二','星期三','星期四','星期五']
day = datetime.today().isoweekday()
subject_temp = ['國']

# def get_data():
#     with open("config.json",'r',encoding='utf-8') as f:
#         data = json.load(f)
#     return data
\
def set_option(day=day):
    slist = data[str(day)]
    var = [tk.StringVar(value=slist[i]) for i in range(9)]
    return var

def set_optionmenu(var):
    subject = data['subject_code']
    group = tk.LabelFrame(window,text="今日課表")
    group.grid(column=3,row=0,rowspan=7)
    for i in range(7):
        t = tk.OptionMenu(group, var[i], *subject)
        t.pack()

def setdefault():
    global e1,e2,code_entry,box1,box2,clock
    
    T = tk.Label(window,text=" 請輸入學生Google帳號",font=('Arial',20))
    e1 = tk.Entry(window,width=20)
    e2 = tk.Entry(window,width=20,show='*')
    
    clock = tk.Label(window,text=datetime.now(),font=('Arial',15))
    clock.grid(column=0,row=3,columnspan=2)
    t1 = tk.Label(window,text="帳號")
    t2 = tk.Label(window,text="密碼")
    tk.Label(window,text="Copyright © 2020 box159. All rights reserved.").grid(column=0,row=8,columnspan=4)
    # o1 = tk.OptionMenu(window, code , '*subject[1:]',command=refresh_classcode)
    # o1.var = code.get()
    box1 = tk.Checkbutton(window,text="顯示密碼",command=toggle_password,onvalue=True,offvalue=False)
    box2 = tk.Checkbutton(window,text="記住密碼",onvalue=True,offvalue=False)
    b1 = tk.Button(window,text="啟動程式",command=button_click,bg='green',fg='white',width=15)
    b2 = tk.Button(window,image=icon,relief="flat",command=setting)
    tk.Button(window,text='refresh',relief='flat',command=setdefault).grid(column=0,row=5)
    box1.var = tk.BooleanVar()
    box1.config(variable=box1.var)
    box2.var = tk.BooleanVar()
    box2.config(variable=box2.var)

    T.grid(column=0,row=0,columnspan=2)
    t1.grid(column=0,row=1)
    t2.grid(column=0,row=2)
    # o1.grid(column=0,row=3)
    e1.grid(column=1,row=1)
    e2.grid(column=1,row=2)
    # code_entry.grid(column=1,row=3)
    box1.grid(column=0,row=4,columnspan=2)
    box2.grid(column=0,row=5,columnspan=2)
    b1.grid(column=0,row=6,columnspan=2)
    b2.grid(column=0,row=4)

    try:
        with open('temp') as f:
            check = f.readline().strip()
            account = decoded(f.readline().strip())
            password = decoded(f.readline())
        e1.insert(0,account)
        if check=="True":
            box2.var.set(True)
        if password!='\n':
            e2.insert(0,password)
    except:
        pass

def update_clock():
        now = time.strftime("%H:%M:%S")
        status = meet.get_nowclass()
        if(status[0]==-1):
            clock.configure(text=now+'  狀態：放學')
        else:
            if(status[1]):
                temp='上課'
            else:
                temp='下課'
            clock.configure(text=now+'  狀態： 第'+str(status[0]+1)+'節'+temp)
        window.after(1000, update_clock)

def setting():
    global setting_data,setting_window,listbox,subject_entry,code_entry
    subject = data['subject_code']
    setting_window = tk.Toplevel()
    setting_window.title("設定") 
    setting_data = []
    tk.Label(setting_window,text="一周課表設定區",bg='green',fg='white',font=('Microsoft YaHei',20)).grid(column=3,row=0,columnspan=5,pady=10)
    tk.Label(setting_window,text="科目設定區",bg='green',fg='white',font=('Microsoft YaHei',20)).grid(column=0,row=0,columnspan=3,pady=10)
    
    for i in range(5):
        setting_data.append(set_option(i+1))
        group = tk.LabelFrame(setting_window,text=week[i])
        group.grid(column=i+3,row=1,rowspan=4,padx=5,sticky='ns')
        for j in range(9):
            t = tk.OptionMenu(group, setting_data[i][j], *subject)
            t.pack()

    scrollbar = tk.Scrollbar(setting_window)
    scrollbar.grid(column=2,row=1,sticky='wns')
    listbox = tk.Listbox(setting_window,yscrollcommand=scrollbar.set,height=12)
    listbox.bind('<<ListboxSelect>>', onselect)
    for i in data['subject_code']:
        try:
            code = " - "+data['meet_code'][i]
        except: 
            code = " - "
        listbox.insert(tk.END,i+code)   
    listbox.grid(column=0,row=1,columnspan=2,sticky='nwes')
    scrollbar.config(command=listbox.yview)
    Frame = tk.Frame(setting_window)
    tk.Button(Frame,image=plus_img,relief='flat',command=add_listbox).grid(column=0,row=7,padx=10)
    tk.Button(Frame,image=minus_img,relief='flat',command=remove_listbox).grid(column=1,row=7,padx=10)
    tk.Button(Frame,image=save_img,relief='flat',command=setting_save_click).grid(column=2,row=7,padx=10)
    Frame.grid(column=0,row=3,columnspan=2,sticky='n')

    tk.Label(setting_window,text='科目or網站').grid(column=0,row=4,sticky='',padx=20)
    tk.Label(setting_window,text='代碼').grid(column=0,row=5,pady=10)

    subject_entry = tk.Entry(setting_window,width=10)
    subject_entry.var = tk.StringVar()
    subject_entry.config(textvariable=subject_entry.var)
    subject_entry.grid(column=1,row=4,sticky='w') 

    code_entry = tk.Entry(setting_window,width=10)
    code_entry.var = tk.StringVar()
    code_entry.config(textvariable=code_entry.var)
    code_entry.grid(column=1,row=5,sticky="w")

def onselect(e):
    
    select = e.widget.curselection()[0]
    name = data['subject_code'][select]
    subject_entry.var.set(name)
    try:
        code_entry.var.set( data['meet_code'][name])
    except:
        code_entry.var.set("")

def add_listbox():
    code = code_entry.get()
    subject = subject_entry.get()
    if(subject in data['subject_code']):
        if(code[0:5]=="https"):
            code = code[24:36]
        num = data['subject_code'].index(subject)
        print(num)
        listbox.delete(num)
        listbox.insert(num,subject+' - '+code)
    # if(subject in data['subject_code']):
    #     popup('error','已有重複的科目')
    else:
        listbox.insert(tk.END,subject+' - '+code)
        subject_entry.delete(0,tk.END)
    savedata()

def remove_listbox():
    select = listbox.curselection()
    listbox.delete(select[0])
    
def setting_save_click():
    savedata()
    setting_window.destroy()
    popup('info',"儲存成功")

def savedata():
    num = 1
    for i in setting_data:
        temp = [t.get() for t in i]
        data[str(num)]=temp
        num+=1
    data['subject_code'] = [i.split(" - ")[0] for i in listbox.get(0,tk.END)]
    temp ={}
    for i in listbox.get(0,tk.END):
        a,b=i.split(" - ")
        temp.update({a:b})
    data['meet_code'] = temp 
    with open('config.json','w+',encoding='utf-8') as f :
        json.dump(data,f,indent=3)

def button_click():
    account = e1.get()
    password = e2.get()
    if(account==''):
        popup('info','請輸入帳號')
    elif(password==''):
        popup('info','請輸入密碼')
    else:
        with open('temp','w') as f:
            f.write(str(box2.var.get())+'\n')
            f.write(encoded(account)+'\n')
            if box2.var.get():
                f.write(encoded(password))

        if (meet.google(account,password)==0):
            popup('error','帳號密碼有誤')

        status = meet.get_code()
        if(status==0):
            popup('error','現在已經是晚上了\n不要在玩我了')
        elif(type(status)==str):
            popup('error','請輸入"'+status+'"的課程代碼')

def encoded(code):   
    return cryptocode.encrypt(code,"box159951")

def decoded(code):
    return cryptocode.decrypt(code,"box159951")

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
set_optionmenu(set_option())

if(day==6 or day==7):
    popup('info','今天不是上課日')

update_clock()
window.mainloop()