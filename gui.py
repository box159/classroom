from datetime import datetime
from os import remove
from re import S
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
    subject = [i for i in data['subject_code']]

week = ['星期一','星期二','星期三','星期四','星期五']
day = datetime.today().isoweekday()
subject_temp = ['國']

# def get_data():
#     with open("config.json",'r',encoding='utf-8') as f:
#         data = json.load(f)
#     return data

def set_option(day=day):
    slist = data[str(day)]
    rsubdc = {a:b for b,a in data['subject_code'].items()}
    var = [tk.StringVar() for _ in range(7)]
    try:
        tnum = 0
        for i in var:
            if slist[tnum] == '':
                tnum += 1
                continue
            temp = i.set(rsubdc[slist[tnum]])
            i = temp
            tnum += 1
    except:
        pass
    return var

def set_optionmenu(var):
    group = tk.LabelFrame(window,text="今日課表")
    group.grid(column=3,row=0,rowspan=7)
    for i in range(7):
        t = tk.OptionMenu(group, var[i], *subject)
        t.pack()

def setdefault():
    global e1,e2,e3,box1,box2,o1
    
    code = tk.StringVar(value=subject[1])
    T = tk.Label(window,text=" 請輸入學生Google帳號",font=('Arial',20))
    e1 = tk.Entry(window,width=20)
    e2 = tk.Entry(window,width=20,show='*')
    e3 = tk.Entry(window,width=20)
    e3.var = tk.StringVar(value=data['meet_code']['國'])
    e3.config(textvariable=e3.var)
    t1 = tk.Label(window,text="帳號")
    t2 = tk.Label(window,text="密碼")
    o1 = tk.OptionMenu(window, code , *subject[1:],command=refresh_classcode)
    o1.var = code.get()
    # t4 = tk.Label(window,text="(e.g. 208)")
    box1 = tk.Checkbutton(window,text="顯示密碼",command=toggle_password,onvalue=True,offvalue=False)
    box2 = tk.Checkbutton(window,text="記住密碼",onvalue=True,offvalue=False)
    b1 = tk.Button(window,text="啟動程式",command=button_click,bg='green',fg='white',width=15)
    b2 = tk.Button(window,image=icon,relief="flat",command=setting)
    box1.var = tk.BooleanVar()
    box1.config(variable=box1.var)
    box2.var = tk.BooleanVar()
    box2.config(variable=box2.var)

    
    T.grid(column=0,row=0,columnspan=2)
    t1.grid(column=0,row=1)
    t2.grid(column=0,row=2)
    o1.grid(column=0,row=3)
    # t4.grid(column=0,row=4)
    e1.grid(column=1,row=1)
    e2.grid(column=1,row=2)
    e3.grid(column=1,row=3)
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

def setting():
    global setting_data,setting_window,listbox
    setting_window = tk.Toplevel()
    setting_window.title("設定") 
    setting_data = []
    tk.Label(setting_window,text="一周課表設定區",bg='green',fg='white',font=('Microsoft YaHei',20)).grid(column=0,row=0,columnspan=5)
    
    for i in range(5):
        setting_data.append(set_option(i+1))
        group = tk.LabelFrame(setting_window,text=week[i])
        group.grid(column=i,row=1,rowspan=7)
        for j in range(7):
            t = tk.OptionMenu(group, setting_data[i][j], *subject)
            t.pack()

    listbox = tk.Listbox(setting_window)
    for i in data['subject_code'].keys():
        listbox.insert(tk.END,i)
    listbox.grid(column=6,row=1,rowspan=5,columnspan=5)
    tk.Button(setting_window,image=plus_img,relief='flat',command=add_listbox).grid(column=6,row=7)
    tk.Button(setting_window,image=minus_img,relief='flat',command=remove_listbox).grid(column=7,row=7)
    tk.Button(setting_window,image=save_img,relief='flat',command=setting_save_click).grid(column=8,row=7)

def add_listbox():
    print(listbox.get(0,tk.END))
def remove_listbox():
    select = listbox.curselection()
    listbox.delete(select[0])
    
def setting_save_click():
    savedata(0)
    setting_window.destroy()
    popup('info',"儲存成功")

def refresh_classcode(subject):
    temp = e3.get()
    subject_temp.append(subject)
    pre_subject = subject_temp[0]
    try:
        code = data['meet_code'][subject]
        e3.var.set(code)
    except:
        e3.var.set('')
    try:
        data['meet_code'][pre_subject] = temp
    except:
        data['meet_code'].update({pre_subject:temp})
    subject_temp.pop(0)
    with open('config.json','w+',encoding='utf-8') as f :
        json.dump(data,f,indent=1)

def savedata(type):
    if(type == 1):
        data['meet_code'][o1.var] = e3.get()
    else:
        num = 1
        for i in setting_data:
            temp = [data['subject_code'][t.get()] for t in i]
            data[str(num)]=temp
            num+=1
        for i in listbox.get(0,tk.END):
            data['subjectcode']
        
    with open('config.json','w+',encoding='utf-8') as f :
        json.dump(data,f,indent=3)

def button_click():
    savedata(1)
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

window.mainloop()