from selenium import webdriver
import pandas as pd
import urllib.request as req
import json

# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver = webdriver.Edge(
    r'C:\\Users\\User\\OneDrive\\桌面\\北大\\研究助理\\Ubereats\\msedgedriver.exe'
)
 
url="https://www.ubereats.com/api/getFeedV1?localeCode=tw"
#字典
requestData={"cacheKey":"JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNSU5QyU4QiVFNyVBQiU4QiVFOCU4NyVCQSVFNSU4QyU5NyVFNSVBNCVBNyVFNSVBRCVCOCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpkY1Z5dF9BYmFEUVJERUFMbXhFdWxGbyUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EyNC45NDU0OTElMkMlMjJsb25naXR1ZGUlMjIlM0ExMjEuMzczMjQ4MyU3RA==/DELIVERY/拉麵//0/0//JTVCJTVE//////ALL/SEARCH_SUGGESTION/HOME//","feedSessionCount":{"announcementCount":0,"announcementLabel":""},"userQuery":"拉麵","date":"","startTime":0,"endTime":0,"carouselId":"","sortAndFilters":[],"marketingFeedType":"","billboardUuid":"","feedProvider":"","promotionUuid":"","targetingStoreTag":"","venueUuid":"","favorites":"","vertical":"ALL","searchSource":"SEARCH_SUGGESTION","recaptchaToken":"03AGdBq25XHHzziCAFmehY6rnIr4J5L7OxAOWodX6j-ZPg14yt34UxfeFUDV8Ip4sMSY0BkcA50M4HoDch2Cxps5S2VnC4JTeS62WXwFujhLn43Lkwy_1UV-5WISfM7LTQCrys-m4IPgHMfhPOI1QA6QHfvXGcXTUPOcr21qmIf-VyshunPRoTJbsbqDn28JMMcE8qv-1URQEclqoJrnSaSfAZqqDlkJof8Dz1maGL1ot3EA_TjaRzO8HfexrhI3XTmwZM60rJqQ6lkcn_uZPOSVLSHK0WRKytZ56qMdY7DefyIYekE4Ckg_TfZ_75VYnPiJkfnxfM5FQWVd9ekiE2QX-mPUifgAbAslTXH5L3edrkApk3GqO7IYq7Wf7Xo_BRU7A9GRcEg7XoJCnhWqnXD29_MNYJApas1ao9Gw1lCR9GYu4gZI6OHyCfWcEJtFlV2meZGE68JQTZvIMfYNUsXvR2qSVxueLtcajIMchmQOGV8w-Tuqc4I64OpglAcROBZMIXPrNGu17nFVKC18JmCaJEP3n5MOajv-BK7wqcQIdhBliPlLBTukPd_Tkv7apeWpQgV034HFU2tpHoDvdRypwuMdIjHWfXHHesY0f7BP5WES7R1mDoAXIHiHY8MsjW8P_R6ofuD1AdK8MMdumXiH9JDjjuN0jESNBAjy-BJ71vDaMl6ohyM_7oRDlm26SN3MRwwCzqyJMi9axfCtzhwmOh3k2xoD31c1AUWGGLJLUqm9Sh-fW45MH0LSAff1PI5KgZC6CHMLKUrmlnd-b2FTLB5IiXXj6WqNcLb_bbcJuIUUr1XMvd6OPYQqy-FV7DQ3_T8p4k3XPituvEiAxwMK-zLx6uxyV4WbZbNNr1Rezbb0_i6RPMi8wj3cX5EXkdoAY4FsCleDym2fUR_ibkt9XLZtJcT0681AM7bIm2Okgy79i0YOw33CNTx0G6UEySjAJo8B8DmvKzhs6xcIkxZoktTSh8EFquHCMfMfKSwk3dZpBqin8-FmIbCy72VD3LxTkMYZvwVXk30jcEgw9Fn_fUgkLjxAfPpgiAgFI7BsaL6bxMkDgEb3B8DdC5F0gt-jQeS_2XsjRmdVdKpyXLXIqpI0LcRWA8vaqFlNARm2gQcyylWSO0QA_cwzlp2XZFBkgSwk6SmME5MeSshZOQrc4wMRkvdyZCB6FG8pOZXElFd-Frd0lTZSxTmyOUKDpGh852cy2fY9kBSrFm0gkev7b8yVN4R76RqlxZu3QG94BTL3JiWl2UAf_SCbL6RduICcBx7GTGp0AqOvlJGv5GOxBsxjROEvfO7eiw9q9UvL1D0CvHHkcO9ksT5p0CfJAj1Fpw0mZ_70pRX97z42dXnObFkZ9q3w8RnWg6zXPfYg45YDJRs3KF7w0WPFgfh2DUXA2WV21tShTylNj0qoZPYKhOG5mNeH-oQYN-hD5G4Bda7hfHndk0xMKNmPngVjtD3yV63ziGebgMH8_gSUUJ7vwnoQi2E4y2ug"}
request=req.Request(url,headers={
    "Content-Type":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44",
    "cookie":"marketing_vistor_id=92842e8c-6f0f-43b9-9903-2f6b01f552c5; segmentCookie=b; utag_geo_code=TW; _ga=GA1.2.198613340.1650508528; _gcl_au=1.1.725313945.1650508528; _hjSessionUser_960703=eyJpZCI6IjNmYTEwNTE0LWRkZjUtNTZhNi1hYWM5LTUxODg3Y2NjYjY2ZCIsImNyZWF0ZWQiOjE2NTA1MDg1MjgxNjEsImV4aXN0aW5nIjp0cnVlfQ==; _scid=0110c2be-7dfa-4d04-a22d-e31b0b681b03; _sctr=1|1650470400000; dId=be9b657b-ade4-4214-b9f6-cae32dd843d8; uev2.gg=true; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1650509233085%7Cconsent:true; _rdt_uuid=1650509233869.d01fd790-e699-4850-88fc-7886dbb5cbe3; _ts_yjad=1650509233872; uev2.loc=%7B%22address%22%3A%7B%22address1%22%3A%22%E5%A4%A7%E5%AD%B8%E8%B7%AF200%E8%99%9F%22%2C%22address2%22%3A%22%E6%96%B0%E5%8C%97%E5%B8%82%E4%B8%89%E5%B3%BD%E5%8D%80%22%2C%22aptOrSuite%22%3A%22%22%2C%22eaterFormattedAddress%22%3A%22237%E5%8F%B0%E7%81%A3%E6%96%B0%E5%8C%97%E5%B8%82%E4%B8%89%E5%B3%BD%E5%8D%80%E5%A4%A7%E5%AD%B8%E8%B7%AF200%E8%99%9F%22%2C%22subtitle%22%3A%22%E6%96%B0%E5%8C%97%E5%B8%82%E4%B8%89%E5%B3%BD%E5%8D%80%22%2C%22title%22%3A%22%E5%A4%A7%E5%AD%B8%E8%B7%AF200%E8%99%9F%22%2C%22uuid%22%3A%22%22%7D%2C%22latitude%22%3A24.9467443%2C%22longitude%22%3A121.372428%2C%22reference%22%3A%22Ej9Oby4gMjAwLCBEYXh1ZSBSZCwgU2FueGlhIERpc3RyaWN0LCBOZXcgVGFpcGVpIENpdHksIFRhaXdhbiAyMzciURJPCjQKMgkPAJ81ChxoNBHCLKfDZID5rRoeCxDuwe6hARoUChIJYexZwYwaaDQRV7YfU46iRf4MEMgBKhQKEgmHn56bChxoNBG6E7O0d7kyxQ%22%2C%22referenceType%22%3A%22google_places%22%2C%22type%22%3A%22google_places%22%2C%22source%22%3A%22manual_auto_complete%22%2C%22addressComponents%22%3A%7B%22countryCode%22%3A%22TW%22%2C%22firstLevelSubdivisionCode%22%3A%22%E6%96%B0%E5%8C%97%E5%B8%82%22%2C%22city%22%3A%22%E4%B8%89%E5%B3%BD%E5%8D%80%22%2C%22postalCode%22%3A%22237%22%7D%2C%22originType%22%3A%22user_autocomplete%22%7D; uev2.diningMode=DELIVERY; uev2.id.xp=89440163-6259-46b0-a447-f6268b326639; uev2.id.session=856f153c-0a42-49a0-8d28-7d99b6ef4703; uev2.ts.session=1650695527033; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTA2OTU1MjcsImV4cCI6MTY1MDc4MTkyN30.pFvButtwS1dOZBdtpLq8XgFiEyGBDvofnDZwC_vITsA; utm_medium=undefined; _userUuid=; utag_main=v_id:018049f9760700121152ab9895b105086005607e00978$_sn:2$_ss:0$_st:1650697332546$segment:b$optimizely_segment:b$_se:5$ses_id:1650695528737%3Bexp-session$_pn:1%3Bexp-session; ext_pgvwcount=-0.1; trdipcktrffcext=1; _gid=GA1.2.1256158869.1650695535; _gat_tealium_0=1; _uetsid=1e137420c2cf11ec883975ee81689285; _uetvid=b4953960c11b11eca511fb36af225e74",
    "x-csrf-token": "x"
},data=json.dumps(requestData).encode("utf-8"))

with req.urlopen(request) as response:
    result=response.read().decode("utf-8")
# 解析Json
result=json.loads(result)
# print(result["data"]["feedItems"][0]["store"]["title"]["text"])


        
menu={
    'store':[],
    # 'id':[],
    'name':[],
    'price':[]
    }

for i in range(2):
    action=result["data"]["feedItems"][i]["store"]["actionUrl"]
    
    murl="https://www.ubereats.com/tw" + str(action)
    
    driver.get(murl)
        
        # --- 輸入外送地址
        
    # dishes
    
    menu['store']=driver.find_elements_by_tag_name('h1')[1].text
    
    # menu['id']=range(1,38)
    
    
    for x in driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div/div[4]/ul').find_elements_by_class_name("c0"):
        if  x.text != "查看全部" :
            menu['name'].append(x.text)
        else:
            next
    
    
    for x in driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div/div[4]/ul').find_elements_by_class_name("dk"):
        
        if '$' in x.text:
            menu['price'].append(x.text)
        else:
            next


print(pd.DataFrame(menu))
    


# print(prices)

# prices=pd.DataFrame(prices).dropna()

# id=[]
# for i in range(len(prices)):
#     no={}
#     no["id"]=i+1
#     id.append(no)

# id=pd.DataFrame(id)
# store=pd.concat([id,name,prices],axis=1)


# print(store)





# product=[]
# for i in range(1,10) :
#     try:
#         data={}
#         a=driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div/div[4]/ul/li[1]/ul[2]/li[' + str(i) + ']/div/div/div/div/div[1]').text
#         data["Meal"]=a
#         product.append(data)
#     except:
#         stop
# print(product)

# for i in driver.find_elements_by_class_name("c0"):
#     print(i.text + '\n')