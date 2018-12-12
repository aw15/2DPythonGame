import os
import sys
import requests
import xml.etree.ElementTree as ET
import folium
import time
from selenium import webdriver
import exampIe

print(exampIe.my_mod("test"))

client_id = "R5BQZkZ9ytJLn2NoTIkg"
client_secret = "okRFeguF9J"
dataFromAPI = None  # dataFromApi - 인터넷으로 부터 받은 자료를 저장하는 변수
dataList = None  # dataList - dataFromApi 에서 xml형태로 변환한 리스트를 저장하는 변수

def ConnectServer():
    global dataFromAPI, dataList
    server = ""  # 메인 주소

    url = "http://api.data.go.kr/openapi/bcycl-dpstry-std?serviceKey=wfqQWmQJMk3FlhDQcutYkXmLMDIXN%2FUIrcwsdqIrzkBZfA5%2F6XVYfDObxhkZ6vhnL9O%2FWJq9DPpu49GCZaN08g%3D%3D&type=xml&s_list=100"  # 주소 뒷부분
    req = requests.get(url)
    if(req.status_code==200):
        tree = ET.fromstring(req.text)
        dataList = tree.getiterator("list")
    else:
        print("연결 오류")
def FindLocation(tag):
    returnList=[]
    for com in dataList:
            for entry in com:
                    for string in entry:
                            for data in string:
                                if (data.text == None):
                                    returnList.append("N")
                                else:
                                    returnList.append(data.text)
    count=0
    coord=[]
    index = (returnList.index(tag))
    finalList=[]

    for i in range(index-15,index+17,1):
        if(returnList[i]=="보관대수"):
            finalList.append(returnList[i]+" : "+returnList[i+1])
        elif (returnList[i] == "공기주입기비치여부"):
            finalList.append(returnList[i] + " : " + returnList[i + 1])
        elif (returnList[i] == "수리대설치여부"):
            finalList.append(returnList[i] + " : " + returnList[i + 1])
        elif (returnList[i] == "소재지지번주소"):
            finalList.append(returnList[i] + " : " + returnList[i + 1])
            coord=GetCoordinate(returnList[i+1])
            GetMap(coord)
        elif (returnList[i] == "관리기관전화번호"):
            finalList.append(returnList[i] + " : " + returnList[i + 1])
    GetMap(coord)
    return finalList

def GetCoordinate(address="광화문"):
    global client_id, client_secret
    url = "https://maps.googleapis.com/maps/api/geocode/xml?address="+address+"&key=AIzaSyBYOPieArSXEiwExB00FPNU6e-WMbIYyUg" # json 결과
    req = requests.get(url)
    tree = ET.fromstring(req.text)
    coord=[]
    for item in tree.getiterator("location"):
        coord.append(item.find("lat").text)
        coord.append(item.find("lng").text)
    return coord

def GetMap(coord=[35.213145, 129.1076011]):
    map_osm = folium.Map(location=[coord[0], coord[1]], zoom_start=15)
    # 마커 지정
    folium.Marker([coord[0], coord[1]], popup='Mt. Hood Meadows').add_to(map_osm)
    # html 파일로 저장\
    delay = 5
    fn = 'testmap.html'
    map_osm.save(fn)
    tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=fn)

    browser = webdriver.Chrome('C:/Users/didxo/Documents/GitHub/project/chromedriver.exe')
    browser.get(tmpurl)
    # Give the map tiles some time to load
    time.sleep(delay)
    browser.save_screenshot('SearchMap.gif')
    browser.quit()
#coord = GetCoordinate("인천광역시 서구 청마로 167번길")
# GetMap(coord)
#ConnectServer()
#why=FindLocation("부산광역시 금정구 금사동 110-10")
#print(why)