from selenium import webdriver


diver = webdriver.Chrome()
diver.get('https://mail.qq.com/cgi-bin/loginpage')
# diver.get('file:///C:/Users/xiaon/Documents/MuMu共享文件夹/html5/login.html')
login_list = ['787269969','asd1123']
diver.switch_to.frame('loginform')
diver.find_element_by_css_selector('#u').send_keys(login_list[0])
diver.find_element_by_css_selector('#exampleInputPassword1').send_keys(login_list[1])

# diver.cl_ose()