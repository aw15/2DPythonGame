import xml.etree.ElementTree as ET
import urllib
from http.client import *
import datetime

# location = urllib.parse.quote(location)
dataFromAPI = None#dataFromApi - 인터넷으로 부터 받은 자료를 저장하는 변수
dataList = None#dataList - dataFromApi 에서 xml형태로 변환한 리스트를 저장하는 변수
def ConnectServer(): #현재 시간-> date
    global dataFromAPI, dataList
    now = datetime.datetime.now()
    date =  now.strftime('%Y-%m-%d')
    date = date.split("-")
    server = "openAPI.seoul.go.kr:8088"#메인 주소
    url = "/564975784c61777331313847614d4644/xml/TimeAverageAirQuality/1/100/"#주소 뒷부분
    conn =HTTPConnection(server)#서버에 연결
    conn.request("GET",url+str(date[0])+str(date[1])+str(date[2]+"0300"))#주소 뒷부분 더하기 현재 날짜
    req = conn.getresponse()#성공적인 연결이 됬다면 req에 데이터와 상태정보가 들어간다.
    #print(req)
    if(req.status==200):#req.status가 200이면 연결 완료!
        cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
        dataFromAPI=(req.read(cLen).decode('utf-8'))  # 데이터를 한글로 읽기
        #print(dataFromAPI)
        tree = ET.fromstring(dataFromAPI)#가져온 데이터는 string 형태기 때문에 elemetal Tree형태의 xml로 파싱
        dataList = tree.getiterator("row") #<row>.....</row>사이 값들을 리스트형태로 저장
        #print(dataList)
    return None



#현재 시간 받아오는 부분, 시간을 2017-05-05형태로 줘서 -을 기준으로 split

def Findlocation(tag):
    global dataList#dataList는 #<row>.....</row>사이 값들을 리스트형태로 저장#<row>.....</row>사이 값들을 리스트형태로 저장한 값
    returnList = []
    print("test")
    for data in dataList:#<row>밑에 값을 하나씩 꺼내서
        if(data.find("MSRSTE_NM").text == tag):#<MSRSTE_NM>부분이 지역이름 들어가 있는 곳이니까 거기에 있는 값과 tag를 비교해서 같으면
                returnList.append("지역: " + data.find("MSRSTE_NM").text)
                returnList.append("NO2: " + data.find("NO2").text)
                returnList.append("O3: " + data.find("O3").text)
                returnList.append("CO: " + data.find("CO").text)
                returnList.append("PM10: " + data.find("PM10").text)
                returnList.append("PM25: " + data.find("PM25").text)
                returnList.append("\n")
                if(int(data.find("PM10").text)>50 or int(data.find("PM25").text)>25):
                    returnList.append("외출을 삼가세요!")
                else:
                    returnList.append("안전합니다!")
                return returnList

