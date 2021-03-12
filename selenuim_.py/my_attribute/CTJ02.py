import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://172.16.101.147:9601/login')
driver.find_element_by_css_selector('#_easyui_textbox_input1').send_keys('cz001')
driver.find_element_by_css_selector('#_easyui_textbox_input2').send_keys('123456')
# driver.find_element_by_css_selector('a[class="textbox-icon combo-arrow"]').click()
# js = 'document.getElementsByClassName("textbox-value").value="430500"'
# driver.execute_script(js)
# driver.find_element_by_css_selector('input[class="textbox-value"]').click()
# 登陆
driver.find_element_by_css_selector('#submit').click()

elements = driver.find_elements("css selector", ".cate-li")
elements[13].click()
driver.find_element_by_css_selector("[index='/nontax/record/nostatuslist.html?list=ticketstoragemanage&ticketType=0&userCode=cz001&userName=%E8%B4%A2%E6%94%BF%E7%AE%A1%E7%90%86%E5%91%98&userId=80B7A4D7F7CF4812A4D08F3BFDF23201&regionCode=430000&regionName=%E6%B9%96%E5%8D%97%E7%9C%81&orgName=%E6%B9%96%E5%8D%97%E7%9C%81%E9%9D%9E%E7%A8%8E%E5%B1%80&orgCode=430000&orgId=BABC9618D0074924B0B9443EDEC1C21C&tokenId=undefined&menuName=%E7%BA%B8%E8%B4%A8%E7%A5%A8%E6%8D%AE%E6%96%B0%E5%A2%9E%E5%85%A5%E5%BA%93']").click()
time.sleep(3)
# driver.find_element_by_css_selector("[class='textbox-icon icon-dataset textbox-icon-disabled']").click()
driver.switch_to.frame("ssiframe")
ass = driver.find_elements("css selector", ".panel-toolbar panel-toolbar-top border-left border-right panel-body panel-body-noheader panel-body-noborder layout-body")
ass[1].click()
# driver.find_element_by_css_selector('span[class="l-btn-left l-btn-icon-left"]').click()
# driver.find_element_by_css_selector("[id='_easyui_tree_67'][class='tree-hit tree-collapsed']").click()


