from copy import Error
from selenium import webdriver as wd
from selenium import webdriver
from time import sleep
import time 
import os
import uuid
from urllib import request
import random
from selenium.webdriver.chrome.options import Options 

path_ = os.path.dirname(str(os.path.realpath(__file__)))
dirpath = f'{path_}/img4/'
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')


#target_url = 'https://www.instagram.com/accounts/login/?next=%2Fexplore%2Ftags%2F%EC%A6%9D%EB%AA%85%EC%82%AC%EC%A7%84%EC%9E%98%EC%B0%8D%EB%8A%94%EA%B3%B3%2F&source=desktop_nav'
target_url = 'https://www.instagram.com/accounts/login/?next=%2Fexplore%2Ftags%2F%EC%A6%9D%EB%AA%85%EC%82%AC%EC%A7%84%2F&source=desktop_nav'
driver = wd.Chrome(executable_path=f"{path_}/driver/chromedriver",options=options)
driver.get(target_url)

time.sleep(3)


login_id = ''
login_pw = ''
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login_id)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(login_pw)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/section/div/button").click()
time.sleep(4)
#driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(4)
driver.get(target_url)
time.sleep(4)

# 스크롤 높이 가져옴
list_ = []

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # 끝까지 스크롤 다
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight-3000);")
    list_=[]
    try:
        info_ = []
        time.sleep(3)
        A = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div")
        B = A.find_elements_by_class_name("Nnq7C.weEfm")
        for i in B:
            B_list = i.find_elements_by_class_name("v1Nh3.kIKUG._bz0w")
            
            for t in B_list:
                info_ = t.find_element_by_xpath("a/div/div[1]/img").get_attribute('src')
                if not info_ in list_:
                    request.urlretrieve(str(info_),f"/Users/lionrocket/Desktop/Insta_tag_Crawling/img4/{uuid.uuid4()}.png")
                    list_.append(info_) 
                    
    except:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print("error")
    print(len(os.listdir(dirpath)))
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        info_ = []
        time.sleep(3)
        A = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div")
        B = A.find_elements_by_class_name("Nnq7C.weEfm")
        for i in B:
            B_list = i.find_elements_by_class_name("v1Nh3.kIKUG._bz0w")
            for t in B_list:
                info_ = t.find_element_by_xpath("a/div/div[1]/img").get_attribute('src')
                if not info_ in list_:
                    request.urlretrieve(str(info_),f"/Users/lionrocket/Desktop/Insta_tag_Crawling/img4/{uuid.uuid4()}.png")
                    list_.append(info_) 
                    
    except:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print("error")
    print(len(os.listdir(dirpath)))