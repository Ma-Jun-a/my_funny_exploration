from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
driver.switch_to.frame("login_frame")
# diver.get('file:///C:/Users/xiaon/Documents/MuMu共享文件夹/html5/login.html')
login_list = ['787269969','asd1123']
driver.find_element_by_css_selector('#switcher_plogin').click()
driver.find_element_by_id("u").send_keys(login_list[0])
driver.find_element_by_css_selector('#p').send_keys(login_list[1])
driver.find_element_by_id("login_button").click()
# diver.cl_ose()