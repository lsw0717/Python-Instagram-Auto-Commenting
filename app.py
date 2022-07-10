from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')

#페이지 이동
driver.get('http://instagram.com')

#(팁)페이지 이동시 로딩 자주 해주자.
time.sleep(4)

#원하는 키 입력시키기 
#-어디에 입력할지 찾기
e = driver.find_elements_by_class_name('_2hvTZ')[0] #아이디 입력 란
#-입력시키기
e.send_keys('nicemg2@naver.com')

#-어디에 입력할지 찾기
e = driver.find_elements_by_class_name('_2hvTZ')[1] #비번 입력 란
#-입력시키기
e.send_keys('430910Dick@')
#엔터키 입력하는 법
e.send_keys(Keys.ENTER)

#(팁)페이지 이동시 로딩 자주 해주자.
time.sleep(4)

#어떤 요소를 클릭하는 법
#-아까처럼 원하는 요소 찾고 - e.click()
e = driver.find_elements_by_class_name('sqdOP')[1] #'로그인 정보를 저장하시겠습니까?' 나중에 하기 클릭
e.click()

#(팁)페이지 이동시 로딩 자주 해주자.
time.sleep(4)

e = driver.find_elements_by_class_name('_a9--')[1] #'로그인 정보를 저장하시겠습니까?' 나중에 하기 클릭
e.click()




#(팁) 클래스 명이 없으면 아이디로 찾자.  find_elements_by_css_selector('#id명')


#(팁)페이지 이동시 로딩 자주 해주자.
time.sleep(4)


#페이지 이동(주호민)
driver.get('https://www.instagram.com/explore/tags/%ED%9B%88%EB%85%80/')
#-어디에 입력할지 찾기
e = driver.find_elements_by_class_name('_aagw')[1]  #두 번째 게시물 
e.click()



for i in range(10):
    time.sleep(4)
    
    #(팁)페이지 이동시 로딩 자주 해주자.
    time.sleep(4)
    e = driver.find_elements_by_class_name('PUqUI')[0]  #댓글창 클릭
    e.click()
    e = driver.find_elements_by_class_name('PUqUI')[0]  #댓글창 클릭
    e.click()
    e.send_keys('SNS 홍보 문구')
    e.send_keys(Keys.ENTER)

    time.sleep(4)
    e = driver.find_elements_by_class_name('wpO6b')[4]  #다음 게시물로 넘어가는 버튼 클릭
    e.click()
    #e = driver.find_elements_by_class_name('wpO6b')[4]  #다음 게시물로 넘어가는 버튼 클릭
    #e.click()




