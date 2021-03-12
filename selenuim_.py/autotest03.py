import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.baidu.com/?tn=21002492_13_hao_pg"
driver = webdriver.Chrome()
driver.get(url)
# driver.close()
driver.find_element_by_id('kw').send_keys('meinv')
driver.find_element_by_id('su').click()
# 隐式等待
# element = WebDriverWait(driver,5).until(expected_conditions.presence_of_element_located((By.ID,'2')))
# element.find_element_by_class_name('c-img6').click()

# 显示等待
driver.implicitly_wait(5)
# element = driver.find_element_by_class_name('c-img6')
element = driver.find_element_by_id('1')
element.click()
# driver.back()
# handle = driver.current_window_handle

driver.implicitly_wait(3)
element = driver.find_element_by_css_selector('a')
element.click()
time.sleep(10)
# driver.quit()



