from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome('/home/ra/chromedriver')

while(True):
driver.get('https://translate.google.com/#tr/tr') 

dinle  = driver.find_element_by_id('gt-speech')
dinle.click()

time.sleep(2)
dinlew  = driver.find_element_by_id('gt-speech')
dinlew.click()

time.sleep(3)

getir=driver.find_element_by_id_('result_box').text

print(getir)
if getir =='M�zik dinlemek istiyorum.' or 'Bana m�zik a�ar m�s�n?.' or 'Youtube.'
driver.get('https://www.youtube.com/') 
else :
print('i�lem tan�ml� de�il')

if getir =='Merhaba.' or 'Hello.' or 'Orada m�s�n?.' or 'Selam.':
time.sleep(1)
temizle = driver.find_element_by_id('gt-clear')
temizle.click()
print('alan temizlendi')

yaz=driver.find_elements_by_class_name('goog-textarea')
yaz.send_keys('sanada merhaba nas�l yard�m edebilirim?')

time.sleep(4)

ses = driver.find_element_by_id('gt-res-listen')
ses.click()
time.sleep(4)
print('islem tamam')
temizle.click()
else :
print('i�lem tan�ml� de�il')
 
print('system okey')