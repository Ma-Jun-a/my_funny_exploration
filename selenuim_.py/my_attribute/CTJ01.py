import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://172.16.101.147:9601/login')
driver.find_element_by_css_selector('#_easyui_textbox_input1').send_keys('cz001')
driver.find_element_by_css_selector('#_easyui_textbox_input2').send_keys('123456')
time.sleep(1)
# 登陆
driver.find_element_by_css_selector('#submit').click()
driver.implicitly_wait(5)
# 选择子菜单
elements = driver.find_elements("css selector", ".cate-li")
elements[13].click()
# 纸质票期初入库
driver.find_element_by_css_selector("[index='/nontax/record/nostatuslist.html?list=ticketstoragemanage&ticketType=0&userCode=cz001&userName=%E8%B4%A2%E6%94%BF%E7%AE%A1%E7%90%86%E5%91%98&userId=80B7A4D7F7CF4812A4D08F3BFDF23201&regionCode=430000&regionName=%E6%B9%96%E5%8D%97%E7%9C%81&orgName=%E6%B9%96%E5%8D%97%E7%9C%81%E9%9D%9E%E7%A8%8E%E5%B1%80&orgCode=430000&orgId=BABC9618D0074924B0B9443EDEC1C21C&tokenId=undefined&menuName=%E7%BA%B8%E8%B4%A8%E7%A5%A8%E6%8D%AE%E6%96%B0%E5%A2%9E%E5%85%A5%E5%BA%93']").click()
# driver.find_element_by_css_selector('a[classname=class="easyui-linkbutton recordbtn l-btn l-btn-small l-btn-plain"]').click()
# 电子票期初入库
time.sleep(2)
driver.find_element_by_css_selector("[index='/nontax/record/nostatuslist.html?list=eleticketstoragemanage&userCode=cz001&userName=%E8%B4%A2%E6%94%BF%E7%AE%A1%E7%90%86%E5%91%98&userId=80B7A4D7F7CF4812A4D08F3BFDF23201&regionCode=430000&regionName=%E6%B9%96%E5%8D%97%E7%9C%81&orgName=%E6%B9%96%E5%8D%97%E7%9C%81%E9%9D%9E%E7%A8%8E%E5%B1%80&orgCode=430000&orgId=BABC9618D0074924B0B9443EDEC1C21C&tokenId=undefined&menuName=%E7%94%B5%E5%AD%90%E7%A5%A8%E6%8D%AE%E6%96%B0%E5%A2%9E%E5%85%A5%E5%BA%93']").click()
time.sleep(2)
elements[5].click()
# 财政库存
time.sleep(2)
driver.find_element_by_css_selector("[index='/nontax/record/nostatuslist.html?list=financestorage&userCode=cz001&userName=%E8%B4%A2%E6%94%BF%E7%AE%A1%E7%90%86%E5%91%98&userId=80B7A4D7F7CF4812A4D08F3BFDF23201&regionCode=430000&regionName=%E6%B9%96%E5%8D%97%E7%9C%81&orgName=%E6%B9%96%E5%8D%97%E7%9C%81%E9%9D%9E%E7%A8%8E%E5%B1%80&orgCode=430000&orgId=BABC9618D0074924B0B9443EDEC1C21C&tokenId=undefined&menuName=%E8%B4%A2%E6%94%BF%E5%BA%93%E5%AD%98']").click()
# 单位库存
time.sleep(2)
driver.find_element_by_css_selector("[index='/nontax/record/nostatuslist.html?list=currentagencystorage&userCode=cz001&userName=%E8%B4%A2%E6%94%BF%E7%AE%A1%E7%90%86%E5%91%98&userId=80B7A4D7F7CF4812A4D08F3BFDF23201&regionCode=430000&regionName=%E6%B9%96%E5%8D%97%E7%9C%81&orgName=%E6%B9%96%E5%8D%97%E7%9C%81%E9%9D%9E%E7%A8%8E%E5%B1%80&orgCode=430000&orgId=BABC9618D0074924B0B9443EDEC1C21C&tokenId=undefined&menuName=%E5%8D%95%E4%BD%8D%E5%BA%93%E5%AD%98']").click()
# 财政票据发放
driver.implicitly_wait(1)
elements[4].click()
time.sleep(2)
driver.find_element_by_css_selector("[index='/nontax/record/statuslist.html?list=ticketreceive&inputType=0&reportCode=ticketdeliverynote&userCode=cz001&userName=%E8%B4%A2%E6%94%BF%E7%AE%A1%E7%90%86%E5%91%98&userId=80B7A4D7F7CF4812A4D08F3BFDF23201&regionCode=430000&regionName=%E6%B9%96%E5%8D%97%E7%9C%81&orgName=%E6%B9%96%E5%8D%97%E7%9C%81%E9%9D%9E%E7%A8%8E%E5%B1%80&orgCode=430000&orgId=BABC9618D0074924B0B9443EDEC1C21C&tokenId=undefined&menuName=%E8%B4%A2%E6%94%BF%E7%A5%A8%E6%8D%AE%E5%8F%91%E6%94%BE']").click()
time.sleep(2)
# 单位票据发放
driver.find_element_by_css_selector("[index='/nontax/finance/ticketissueagency.html?userCode=cz001&userName=%E8%B4%A2%E6%94%BF%E7%AE%A1%E7%90%86%E5%91%98&userId=80B7A4D7F7CF4812A4D08F3BFDF23201&regionCode=430000&regionName=%E6%B9%96%E5%8D%97%E7%9C%81&orgName=%E6%B9%96%E5%8D%97%E7%9C%81%E9%9D%9E%E7%A8%8E%E5%B1%80&orgCode=430000&orgId=BABC9618D0074924B0B9443EDEC1C21C&tokenId=undefined&menuName=%E5%8D%95%E4%BD%8D%E7%A5%A8%E6%8D%AE%E5%8F%91%E6%94%BE']").click()




