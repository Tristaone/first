from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com.cn")

# 切入iframe
driver.switch_to.frame("login_frame_qq")
driver.find_element_by_id("u")

# 先找到元素，再把元素拖动到滚动区域
ele = driver.find_element_by_id("xxxx")
driver.execute_script("arguments[0].scrollIntoView();", ele)
ele.send_keys("selenium")

# 重新回到主页面
driver.switch_to.default_content()
driver.close()
driver.quit()

