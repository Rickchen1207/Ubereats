# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:40:09 2022

@author: User
"""

category = driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div[3]/div[4]/ul').find_elements_by_class_name("gl")

for x in range(1,len(category)+1):
    section = driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div/div[4]/ul/li[' + str(x) + ']/ul').find_elements_by_tag_name("li")
    
    for y in range(1,len(section)+1):
        try:
            menu['name'].append(driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div[3]/div[4]/ul/li[' + str(x) + ']/ul[1]/li[' + str(y) + ']/div/div/div[2]/div[1]').text)
        except:
            menu['name'].append(driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div[3]/div[4]/ul/li['+ str(x) +']/ul/li[' + str(y) + ']/div/div/div[2]/div[1]').text)
print(menu)