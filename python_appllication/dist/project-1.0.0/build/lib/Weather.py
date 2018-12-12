import xml.etree.ElementTree as ET
import urllib
from http.client import *

# location = urllib.parse.quote(location)
dataFromAPI = None#dataFromApi - 인터넷으로 부터 받은 자료를 저장하는 변수
dataList = None#dataList - dataFromApi 에서 xml형태로 변환한 리스트를 저장하는 변수

def ConnectServer(location):
    global dataFromAPI, dataList
    server = "www.kma.go.kr"#메인 주소
    if(location=="seoul"):
        url = "/wid/queryDFSRSS.jsp?zone=1159068000"#주소 뒷부분
    elif(location=="busan"):
        url="/wid/queryDFSRSS.jsp?zone=2635061000"
    elif(location=="Gangwon"):
        url="/wid/queryDFSRSS.jsp?zone=4215061500"
    elif(location=="Daesun"):
        url="/wid/queryDFSRSS.jsp?zone=3023052000"
    elif(location=="Junrado"):
        url="/wid/queryDFSRSS.jsp?zone=2920054000"
    elif(location=="Incheon"):
        url="/wid/queryDFSRSS.jsp?zone=2823764100"
    conn =HTTPConnection(server)#서버에 연결
    conn.request("GET",url)#주소 뒷부분 더하기
    req = conn.getresponse()#성공적인 연결이 됬다면 req에 데이터와 상태정보가 들어간다.


    if(req.status==200):#req.status가 200이면 연결 완료!
        #cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
        dataFromAPI=(req.read().decode('utf-8'))  # 데이터를 한글로 읽기
        #print(dataFromAPI)
        tree = ET.fromstring(dataFromAPI)#가져온 데이터는 string 형태기 때문에 elemetal Tree형태의 xml로 파싱
        dataList = tree.getiterator("body") #<row>.....</row>사이 값들을 리스트형태로 저장
        count=0
        returnList=[]
        for item in dataList:
            for data in item:
                count += 1
                if(count%5==0):
                    count=0
                    returnList.append("최고온도: "+ data.find("tmx").text)
                    returnList.append("최저온도: "+data.find("tmn").text)
                    returnList.append("날씨: " + data.find("wfKor").text)
                    temp =data.find("ws").text
                    temp = float(temp)
                    temp = round(temp,4)
                    returnList.append("풍속: "+str(temp))
                    returnList.append("강수확률: " + data.find("pop").text)
                    return returnList
    return None
def ForeCast():
    server = "www.kma.go.kr"
    url ="/weather/forecast/mid-term-rss3.jsp?stnId=108"
    conn = HTTPConnection(server)  # 서버에 연결
    conn.request("GET", url)  # 주소 뒷부분 더하기
    req = conn.getresponse()  # 성공적인 연결이 됬다면 req에 데이터와 상태정보가 들어간다.

    if (req.status == 200):  # req.status가 200이면 연결 완료!
        # cLen = req.getheader("Content-Length")  # 가져온 데이터 길이
        dataFromAPI = (req.read().decode('utf-8'))  # 데이터를 한글로 읽기

        tree = ET.fromstring(dataFromAPI)  # 가져온 데이터는 string 형태기 때문에 elemetal Tree형태의 xml로 파싱
        dataList = tree.getiterator("data")  # <row>.....</row>사이 값들을 리스트형태로 저장
        count = 0
        returnList = []
        for element in dataList:
            for data in element:
                count=count+1
                if (count<3):
                    returnList.append(element[2].text)
                else:
                    return returnList

