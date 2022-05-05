# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:00:36 2022

@author: User
"""

from selenium import webdriver
import pandas as pd
import time

# 開啟Selenium
driver = webdriver.Edge(
    r'C:\\Users\\User\\OneDrive\\桌面\\北大\\研究助理\\Ubereats\\msedgedriver.exe'
)
driver.maximize_window()
driver.get("https://www.ubereats.com/tw")

# 爬蟲函數
def webcrawl(place,meal):
    # driver.get("https://www.ubereats.com/tw")
    getblock=driver.find_element_by_xpath('//*[@placeholder="輸入外送地址"]')
    getblock.send_keys(place)
    time.sleep(2)
    getblock.send_keys('\ue007')
    time.sleep(3)
    label=driver.find_element_by_xpath('//*[@placeholder="美食、生鮮雜貨、飲料等"]')
    label.send_keys(meal)
    time.sleep(1)
    label.send_keys('\ue007')

webcrawl("台灣大學","日式")

restaurant={
    'shopName':[],
    'Url':[],
    # 'address':[],
    # 'location':[],
    'shopCode':[],
    'shopTag':[],
    'rate':[],
    'comment':[],
    'discount':[],
    'pickup':[],
    # 'inShopPrice':[],
    'menu':[],
    'shippingFee':[],
    'shippingTime':[],
    # 'updateDate':[],
    # 'myLocation':[]
    }

location = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div['

# for i in range(1,80):
#     if "開始營業" not in driver.find_element_by_xpath(location + str(i) + ']/div/div/div/div[2]/div[2]/div[2]/span[2]/div').text:
#         restaurant['shippingFee'].append(driver.find_element_by_xpath(location + str(i) + ']/div/div/div/div[2]/div[2]/div[2]/span[2]/div').text)
#     else:
#         break
#     restaurant['shopName'].append(driver.find_element_by_xpath(location + str(i) + ']/div/a/h3').text)
#     restaurant['Url'].append(driver.find_element_by_xpath(location + str(i) + ']/div/a').get_attribute('href'))
#     restaurant['shippingTime'].append(driver.find_element_by_xpath(location + str(i) +']/div/div/div/div[2]/div[2]/div[3]').text)
#     try:
#         restaurant['rate'].append(driver.find_element_by_xpath(location + str(i) +']/div/div/div/div[2]/div[1]/div[3]').text)
#     except:
#         restaurant['rate'].append('Star')
#     try:
#         restaurant['comment'].append(driver.find_element_by_xpath(location + str(i) +']/div/div/div/div[2]/div[1]/span').text)
#     except:
#         restaurant['comment'].append('None')

from unittest import result
import urllib.request as req
import json

# 連線網址
url="https://www.ubereats.com/api/getFeedV1?localeCode=tw"

# 字典
requestData={"cacheKey":"JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFOCU4NyVCQSVFNyU4MSVBMyVFNSVBNCVBNyVFNSVBRCVCOCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpxUzR5X29tcFFqUVJabjhkN2dRRWRTRSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EyNS4wMTc0NjA2JTJDJTIybG9uZ2l0dWRlJTIyJTNBMTIxLjUzOTA2MiU3RA==/DELIVERY/日式//0/0//JTVCJTVE//////ALL/SEARCH_SUGGESTION/HOME//","feedSessionCount":{"announcementCount":0,"announcementLabel":""},"userQuery":"日式","date":"","startTime":0,"endTime":0,"carouselId":"","sortAndFilters":[],"marketingFeedType":"","billboardUuid":"","feedProvider":"","promotionUuid":"","targetingStoreTag":"","venueUuid":"","favorites":"","vertical":"ALL","searchSource":"SEARCH_SUGGESTION","recaptchaToken":"03AGdBq25A-rdkBIfYC-CCq_pQvww-y4zGfCENPiHojz9qjOUWiupfMSLCEhM7B8hTJ1gmRscJuuZ3oPN7BevNWG-WG0IQdFs1vhjVgnnkiXvQoK3khtgpKj-P70KjYN1D9fUBqImpS3asodsNON89e-SqNf8ICLzei1Z-ZHslvphkZPHHpn7s2KlQqGMbDl547UsPy8YOpWHtQqgYta7MLh5QkYwypeWjdD6rEigNU4ato_fw7xv7ypR_7qA1L0z902C_HNFFLXTc0HRX2nB71ppujn2WLx6L1iSi-FvcXeaZPIuIuQhKE7C2NliKbjq6THjuhXBOf-Sh6dOiTsIuqKl7iradZoapd1CAE_7YRuhjAdANW8qOOWlvm8F9JhSbEKntOZqScONFjOq87h-LSeqit6z28HUg_RJFCCfRkAcRoHHPc65GvCTrJQyAlYXjQwPxo3LMY66wwzjiECz_cXEqlBMOdHU_SWEZYmSOurn70HRafEw7f-Od2mZ82PYrVWULEEojooggUBhU08HE6zDHZaBVduKlCLRLkK4c0O9ClAj7LwWZY9PfdVzJ2Fyaq4FXAxwhERo59U54IOdn0S_Td1KkC6Ukm8lJgsfJ6jVCauW-glSYcYlkdBmLdBhx45L0lK61lXwAMqKfZS_1LBzIMDuWiVsLoryCYp-Nmju4l_WkBBB91EMnDasI00CL68x5tUM_jVGUvGTVbjUFlQhO3-Xs2_ZKTj7h7cMv7AYJV96C7fZoZduaZijNitiGzmBwfS3plowpj7d6WgSMFM6fdyrCXB-Y2kn9ZaEZfWgWtr4hXGjxqPXlh1jSZ4yJwpTCNz8OvcS03Ir3Y6ZI1CY9fOxBaRR-3gp-dmRxGjCf-4sfuZAJ_3stpk7Q0pit67Yw-XH8BfpTR2dot448QtiAyn109f68I_Y2bBXKnDjF-AmFhcxNVUmCPxqtHlQzCO-1k69eHJNIQWOULPGuQSmLk1rrSjhswxD1MHrNBDG0s4T5aZKVvVNdbUGmPdqqKPe22IdFROfZklOiOFwVIUrJia5hTiylGStChu2mepFbkPpAuEDDmWOQrgTcZ1kBIDtPaeA2zxO-cc_IzGFG4dcvlPnt_NrBZGwBBchtor2Ucl5zecTMg_F_tckpuneyrvnJ3kD15mDA-jkCJoI2VQWe9hbEEBi9Pb-Bmkoj2WYJrfc_udxPBD_dIUJKoZVxolfqOTr5QWeA3HcyICwrHYMqF5yFojLlGoyITPtDFe2gqHuBV1zHnn4ir5-ssdu6IdkyOzKS5rOWzGAC6wemfHhT4qzYb6xcoS7fw7F5T8gzuW8uHi5lU9ktRiWJfyG03RuxDJsvhVPwVPNv8r2UYDe67_sxNCVe2tHkDmo75Y-AKR4OFpctnSZXTYlKPhty_xOwma0x7dGRf5EDAbcS1fvBboQ8O2lxFG12wa9S-xfnBxal8MauBT4GiQ30UHcXBJyAuAs0CjKVX7hSINXxGCdmxY8roP2hBZKL7zKzThPwWaG2Xzio9JA"}
request=req.Request(url,headers={
    "Content-Type":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44",
    "cookie":"uev2.id.xp=d51cc830-dabe-44a0-a694-aa888a52b8c9; dId=410db17f-6bde-4ec1-8885-b3729306401d; uev2.id.session=9b684afb-9942-4485-8d75-76d9b01668f9; uev2.ts.session=1651561538454; marketing_vistor_id=cc78a443-cd7e-42c3-84a5-0a3bc50ca392; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTE1NjE1MzgsImV4cCI6MTY1MTY0NzkzOH0.3oJVFGMyST4lDlEYFkMUYZq1bmVajCz3-VoZaSmYxQU; uev2.gg=true; utm_medium=undefined; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1651561541396%7Cconsent:true; _scid=1116f395-31e8-4568-adff-8160454a396e; _gcl_au=1.1.726044677.1651561542; _rdt_uuid=1651561541932.29477f90-05d9-4e9c-a9ef-e222aa2125ad; _ts_yjad=1651561541955; _ga=GA1.2.1308292534.1651561542; _gid=GA1.2.1688515285.1651561542; _gac_UA-60706425-3=1.1651561542.EAIaIQobChMIm_3IleLC9wIVhiRgCh3unQc7EAAYASAAEgKxV_D_BwE; _fbp=fb.1.1651561542087.1419502252; _gat_tealium_0=1; _gcl_aw=GCL.1651561543.EAIaIQobChMIm_3IleLC9wIVhiRgCh3unQc7EAAYASAAEgKxV_D_BwE; _gcl_dc=GCL.1651561543.EAIaIQobChMIm_3IleLC9wIVhiRgCh3unQc7EAAYASAAEgKxV_D_BwE; _sctr=1|1651507200000; uev2.loc=%7B%22address%22%3A%7B%22address1%22%3A%22%E8%87%BA%E7%81%A3%E5%A4%A7%E5%AD%B8%22%2C%22address2%22%3A%22%E5%8F%B0%E5%8C%97%E5%B8%82%E5%A4%A7%E5%AE%89%E5%8D%80%E7%BE%85%E6%96%AF%E7%A6%8F%E8%B7%AF%E5%9B%9B%E6%AE%B51%E8%99%9F%22%2C%22aptOrSuite%22%3A%22%22%2C%22eaterFormattedAddress%22%3A%2210617%E5%8F%B0%E7%81%A3%E5%8F%B0%E5%8C%97%E5%B8%82%E5%A4%A7%E5%AE%89%E5%8D%80%E7%BE%85%E6%96%AF%E7%A6%8F%E8%B7%AF%E5%9B%9B%E6%AE%B51%E8%99%9F%22%2C%22subtitle%22%3A%22%E5%8F%B0%E5%8C%97%E5%B8%82%E5%A4%A7%E5%AE%89%E5%8D%80%E7%BE%85%E6%96%AF%E7%A6%8F%E8%B7%AF%E5%9B%9B%E6%AE%B51%E8%99%9F%22%2C%22title%22%3A%22%E8%87%BA%E7%81%A3%E5%A4%A7%E5%AD%B8%22%2C%22uuid%22%3A%22%22%7D%2C%22latitude%22%3A25.0174606%2C%22longitude%22%3A121.539062%2C%22reference%22%3A%22ChIJqS4y_ompQjQRZn8d7gQEdSE%22%2C%22referenceType%22%3A%22google_places%22%2C%22type%22%3A%22google_places%22%2C%22source%22%3A%22manual_auto_complete%22%2C%22addressComponents%22%3A%7B%22countryCode%22%3A%22TW%22%2C%22firstLevelSubdivisionCode%22%3A%22%E5%8F%B0%E5%8C%97%E5%B8%82%22%2C%22city%22%3A%22%E5%A4%A7%E5%AE%89%E5%8D%80%22%2C%22postalCode%22%3A%2210617%22%7D%2C%22originType%22%3A%22user_autocomplete%22%7D; _uetsid=71eec1d0caaf11ecaa2a95be64a49e7f; _uetvid=71f02620caaf11ec9de945ed3040ce73; uev2.diningMode=DELIVERY; utag_main=v_id:018088bd2ee70021d8fbc0a8ed3c0508501ba07d00978$_sn:1$_se:7$_ss:0$_st:1651563362643$ses_id:1651561541355%3Bexp-session$_pn:2%3Bexp-session; _userUuid=undefined",
    "x-csrf-token": "x"
},data=json.dumps(requestData).encode("utf-8"))

with req.urlopen(request) as response:
    result=response.read().decode("utf-8")

# 解析Json
result=json.loads(result)

store=result["data"]["feedItems"]

for i in range(0,79):
    
    if "開始營業" not in store[i]["store"]["meta"][1]["text"]:
       restaurant['shippingFee'].append(store[i]["store"]["meta"][1]["text"]) 
    else:
        break    
    restaurant['shippingTime'].append(store[i]["store"]["meta"][2]["text"])
    try:
        store[i]["store"]["meta"][0]['textFormat']
        restaurant['shopTag'].append("優饗方案")
    except:
        restaurant['shopTag'].append("None")
    restaurant['shopName'].append(store[i]["store"]["title"]["text"])
    restaurant['Url'].append(store[i]["store"]['actionUrl'])
    restaurant['shopCode'].append(store[i]["store"]['storeUuid'])
    try:
        restaurant['comment'].append(store[i]["store"]["rating"]["accessibilityText"])
    except:    
        restaurant['comment'].append("None")
    try:
        restaurant['rate'].append(store[i]["store"]["rating"]["text"])
    except:
        restaurant['rate'].append('Star')
    try:
        restaurant['discount'].append(store[i]["store"]['signposts'][0]["text"])
    except:
        restaurant['discount'].append('None')
    
def total_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

food = '//*[@id="main-content"]/div[5]/div/div[4]/ul[1]/li['
link = 'https://www.ubereats.com/tw'

for i in range(1,80):
    
    menu={
        'name':[],
        'price':[]
        }
   
    murl=link + restaurant['Url'][i-1]
    
    driver.get(murl)

    # 地址
    # restaurant['address'].append(driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div/div[2]/div[3]/button[1]/div/div[2]').text)

    # 外帶自取
    try:
        driver.find_element_by_xpath('//*[@id="main-content"]/div[4]/div/div[2]/div/div[2]/div/div/div')
        restaurant['pickup'].append(1)
    except:
        restaurant['pickup'].append(0)

    # 有幾個類別
  
    category = driver.find_elements_by_class_name("h7")
    num = total_elements(category) 

    # 餐點名稱
    try:        

        for x in range(1,num+2):
        # 類別中有幾個餐點
            try:
                section = driver.find_element_by_xpath(food + str(x) + ']').find_elements_by_tag_name("li") 
            except:
                next
            # 分成兩種排版方式
            if len(driver.find_element_by_xpath(food + str(x) + ']').find_elements_by_tag_name("ul")) == 2:
                try:
                    for z in range(1,3):
                        for y in range(1,len(section)+1):
                            menu['name'].append(driver.find_element_by_xpath(food + str(x) + ']/ul[' + str(z) +']/li[' + str(y) + ']/div/div/div[2]/div[1]').text)
                except:
                    for g in range(1,len(driver.find_element_by_xpath(food + str(x) +']/ul[2]').find_elements_by_tag_name("li")) + 1):
                        menu['name'].append(driver.find_element_by_xpath(food + str(x) + ']/ul[2]/li[' + str(g) + ']/div/div/div[1]/div[1]/div[1]').text)
            else :
                for y in range(1,len(section)+1):                   
                    menu['name'].append(driver.find_element_by_xpath(food + str(x) + ']/ul[1]/li[' + str(y) + ']/div/div/div[2]/div[1]').text)

    except:
          next
     
    # 餐點價格
    try:
        for x in range(1,num+2):
        # 類別中有幾個餐點價格
            try:
                section = driver.find_element_by_xpath(food + str(x) + ']').find_elements_by_tag_name("li") 
            except:
                next
            # 分成兩種排版方式
            if len(driver.find_element_by_xpath(food + str(x) + ']').find_elements_by_tag_name("ul")) == 2:
                try:
                    for z in range(1,3):
                        for y in range(1,len(section)+1):
                            menu['price'].append(driver.find_element_by_xpath(food + str(x) + ']/ul[' + str(z) +']/li[' + str(y) + ']/div/div/div[2]/div[2]').text)
                except:
                    for g in range(1,len(driver.find_element_by_xpath(food + str(x) +']/ul[2]').find_elements_by_tag_name("li")) + 1):
                        menu['price'].append(driver.find_element_by_xpath(food + str(x) + ']/ul[2]/li[' + str(g) + ']/div/div/div[1]/div[1]/div[2]').text)
            else :
                for y in range(1,len(section)+1):
                    menu['price'].append(driver.find_element_by_xpath(food + str(x) + ']/ul[1]/li[' + str(y) + ']/div/div/div[2]/div[2]').text)
    except:
          next
    
   
    restaurant['menu'].append(menu)

restarant2=pd.DataFrame(restaurant)


driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div/div[4]/ul/li[1]/div/div/div[2]/div/ul/div/li/div/div/div[2]/div[1]')
