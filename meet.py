#pyinstaller -F .\classroom\class.py
import code
import pandas as pd
from selenium import webdriver
from datetime import datetime
import time
import schedule
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



opt=Options()
on=inclass=peopleon=False
w=datetime.today().isoweekday()

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

def google(mail,password,classnum): 
  global chrome
  chrome=webdriver.Chrome(chrome_options=opt)
  # chrome.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dzh-TW&followup=https%3A%2F%2Faccounts.google.com%2F%3Fhl%3Dzh-TW&hl=zh-TW&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

  # emailweb=chrome.find_element_by_id("identifierId")
  # emailweb.send_keys(mail)
  # login1=chrome.find_element_by_xpath("//*[@id='identifierNext']/div/button/span")
  # login1.click()  

  # passwordweb = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.NAME, "password")))
  # chrome.implicitly_wait(1)
  # passwordweb.send_keys(password)

  # login2=chrome.find_element_by_xpath("//*[@id='passwordNext']/div/button")
  # login2.click()
  # time.sleep(5)

  code=get_meetcode(classnum,8)#get_nowclass())
  print(code)
  if(code!=-1):
    classjoin("ss:"+code)
  else:
    chrome.close()
    return 0
  
  # if on:
  #   classjoin(gmeet)

def get_meetcode(classnum,classnow):
  print(classnow)
  if(classnow==-1):
    code = False
  else:
    code = pd.read_excel('meet_code.xlsx',sheet_name=classnum[0])
  return code[int(classnum)][int(classnow)]

def get_nowclass():
  onclass = ['08:05','09:10','10:10','11:10','13:00','14:00','15:00']
  offclass = ['08:55','10:00','11:00','12:00','13:50','14:50','15:50']
  now = str(datetime.now().time())
  classnow = 0
  for i in onclass:
    classnow +=1
    if (now < i):
      break
  else:
    classnow = -1
  return classnow

def classjoin(s):
  global on,inclass,peopleon
  on=True
  try:
    chrome.get(meet[s])
  except:
    return
  try:
    WebDriverWait(chrome, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[2]/div/div")))
  except:
    camera=WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")))
    camera.click()
    mic=WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")))
    mic.click()
    join=WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt')))
    join.click()
    inclass=True
    time.sleep(5)
    #classquit()
    peopleon=True
    return
  google(s)

def classquit():
  global inclass
  try:
    quit=chrome.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[6]/span/button")
  except:
    inclass=False
    return
  quit.click()
  inclass=False

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

# google(1)
#job(1)
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