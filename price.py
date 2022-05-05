import time
from tracemalloc import stop
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.ubereats.com/tw/store/%E9%9D%92%E5%8E%9F%E6%8B%89%E9%BA%B5%E4%B8%BC%E9%A3%AF/O53QERsYS4yEFTPWn7ArNw?diningMode=DELIVERY")

# --- 輸入外送地址
driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div/div[2]/div[2]/button').click()

# a=driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div/div[4]/ul').text

