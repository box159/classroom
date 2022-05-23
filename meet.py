#pyinstaller -F .\classroom\class.py
import json
import threading
from selenium import webdriver
from datetime import datetime
import time
import schedule
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


day=datetime.today().isoweekday()
opt=Options()
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })
def get_data():
  with open('config.json','r',encoding='utf-8') as f :
    data = json.load(f)
    return data
def google(mail,password): 
  global chrome
  try:
    chrome=webdriver.Chrome(chrome_options=opt)
    chrome.get("https://accounts.google.com/signin")
    emailweb=chrome.find_element_by_id("identifierId")
    emailweb.send_keys(mail)
    login1=chrome.find_element_by_xpath("//*[@id='identifierNext']/div/button/span")
    login1.click()  

    passwordweb = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    chrome.implicitly_wait(1)
    passwordweb.send_keys(password)

    login2=chrome.find_element_by_xpath("//*[@id='passwordNext']/div/button")
    login2.click()
    time.sleep(5)
  except:
    return 0

def get_code():
  data = get_data()
  schedule = data[str(day)]
  scode = data['subject_code']
  mcode = data['meet_code']
  # rscode = {a:b for b,a in scode.items()}
  nowclass = get_nowclass()

  if(nowclass[0]!=-1):
    try:
      classjoin(mcode[schedule[nowclass[0]]])
    except:
      chrome.close()
      return schedule[nowclass[0]]
  else:
    chrome.close()
    return 0

def get_nowclass():
  data = get_data()
  onclass = data['ontime']
  offclass = data['offtime']
  now = str(datetime.now().time())
  classnow = 0
  class_status = False
  for i in offclass:
    if (now < i):
      if(now > onclass[classnow]):
        class_status = True      
      break
    classnow +=1
  else:
    classnow = -1
  return classnow,class_status

def classjoin(code):
  print(code)
  chrome.get("https://meet.google.com/"+code)
  try:
    WebDriverWait(chrome, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[2]/div/div")))
  except:
    camera=WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]")))
    camera.click()
    mic=WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div[1]")))
    mic.click()
    join=WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.VfPpkd-vQzf8d:nth-child(4)')))
    join.click()
    time.sleep(5)
    t = threading.Thread(target=check_onlinenum)
    t.start()

def check_onlinenum():
  while True:
    people=int(chrome.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/div/div").text)
    if (people<15 and get_nowclass()[1]):
      get_code()
      break
    print(people)
    time.sleep(15)
    
def classquit():
  get_code()
  # quit=chrome.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[10]/div[3]/div[10]/div[2]/div/div[6]/span/button")
  # quit.click()
  # try:
  #   quit1 = chrome.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div[2]/div/div[2]/button[1]/span")
  #   quit1.click()
  # except:
  #   pass

if(__name__=='__main__'):
  print("請使用gui.py啟動")
# schedule.every().day.at('08:05').do(job,1)
# schedule.every().day.at('09:10').do(job,2)
# schedule.every().day.at('10:10').do(job,3)
# schedule.every().day.at('11:10').do(job,4)
# schedule.every().day.at('13:00').do(job,5)
# schedule.every().day.at('14:00').do(job,6)
# schedule.every().day.at('15:00').do(job,7)

# schedule.every().day.at('08:55').do(classquit)
# schedule.every().day.at('10:00').do(classquit)
# schedule.every().day.at('11:00').do(classquit)
# schedule.every().day.at('12:00').do(classquit)
# schedule.every().day.at('13:50').do(classquit)
# schedule.every().day.at('14:50').do(classquit)
# schedule.every().day.at('15:50').do(classquit)

while False:
  x=1
  schedule.run_pending()
  time.sleep(1)
  os.system("cls")
  if peopleon:
    try:
      people=int(chrome.find_element_by_class_name("uGOf1d").text)
      if people<20:
        peopleon=False
        classquit()
    except:
      peopleon=False
  if inclass:
    print("*Produced by box159*\n*Used for 116 TYSH*\n當前時間:",time.strftime("%H:%M:%S", time.localtime()),"\n等待下一節下課(",x,")")
  if inclass==False:
    print("*Produced by box159*\n*Used for 116 TYSH*\n當前時間:",time.strftime("%H:%M:%S", time.localtime()),"\n等待下一節上課(",x,")")