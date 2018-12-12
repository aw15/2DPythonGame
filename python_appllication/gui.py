import tkinter as t1
from tkinter import *
from tkinter import ttk
from tkinter import font
import Mungi
import Weather
import Map
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



weatherResult=[]
bicycleResult=[]
dustResult=[]

win = t1.Tk()
win.geometry("1200x700") #600x400
win.title("자놀")
buttonFont = font.Font(win, size=10, weight='bold', family = '맑은 고딕')
textFont = font.Font(win, size=9, family = '맑은 고딕')
tabControl = ttk.Notebook(win)
#Map.ConnectServer()
#-------------------------------------------------------------------------------------  날씨
def WeatherProcess():
    global weatherResult
    weatherText.delete('1.0 ',END )
    select=weatherComboBox.get()
    returnList = []
    if select=="서울":
        returnList = Weather.ConnectServer("seoul")
    elif select =="인천":
        returnList = Weather.ConnectServer("Incheon")
    elif select =="강원도":
        returnList = Weather.ConnectServer("Gangwon")
    elif select =="충청도":
        returnList = Weather.ConnectServer("Daesun")
    elif select =="경상도":
        returnList = Weather.ConnectServer("busan")
    elif select =="전라도":
        returnList = Weather.ConnectServer("Junrado")
    for i in range(0,5,1):
        weatherText.insert(INSERT,returnList[i])
        weatherResult.append(returnList[i])
        weatherText.insert(INSERT, "\n")
    foreCastData = Weather.ForeCast()
    weatherText.insert(INSERT, "\n")
    weatherText.insert(INSERT, "\n")
    weatherText.insert(INSERT, "내일 : " + foreCastData[0])
    weatherResult.append("내일 : " + foreCastData[0])
    weatherText.insert(INSERT, "\n")
    weatherText.insert(INSERT, "내일 모래 : " + foreCastData[1])
    weatherResult.append("내일 모래 : " + foreCastData[1])
#----------------------------------------------------------------------------------------미세먼지
def DustProcess():
    global dustResult
    dustText.delete("1.0",END)
    tag = dustComboBox.get()
    Mungi.ConnectServer()
    returnData = Mungi.Findlocation(tag)
    print(returnData)
    for i in range(0,8,1):
        dustText.insert(INSERT,returnData[i])
        dustResult.append(returnData[i])
        dustText.insert(INSERT,"\n")

#----------------------------------------------------------------------------------------자전거
def bycicleProcess():
    tag = bicycleEntry.get()
    #Map.FindLocation(tag)
    coord=Map.GetCoordinate(tag)
    Map.GetMap(coord)
    photo = PhotoImage(file="SearchMap.gif")
    boganImage.configure(image = photo, width = 777, height = 397.5)
    boganImage.image = photo
#----------------------------------------------------------------------------------------메일
def SendMail():
    global weatherResult,dustResult
    # me == 보내는 사람의 이메일 주소
    # you == 받는 사람의 이메일 주소
    me = mailIDEntry.get()
    you=mailSendEntry.get()
    # me ="didxodbs0987@gmail.com"
    password = mailPasswordEntry.get()
    # you = "didxodbs0987@naver.com"
    # password = "x0yx251210"

    message = MIMEMultipart()
    message['Subject'] = 'Your Search Result!' # 이메일 제목
    message['From'] = me
    message['To'] = you

    # 로컬 SMTP 서버를 사용해서 메세지를 보낸다.
    # 이 예제에서는 Header 는 추가하지 않는다.
    msg = MIMEText('결과\n'+
                   "=================================\n" +
                   weatherResult[0]+'\n'+
                   weatherResult[1] + '\n'+
                   weatherResult[2] + '\n' +
                   weatherResult[3] + '\n' +
                   weatherResult[4] + '\n' +
                   weatherResult[5] + '\n' +
                   weatherResult[6] + '\n' +
                   "=================================\n"+
                   dustResult[0]+'\n'+
                   dustResult[1] + '\n' +
                   dustResult[2] + '\n' +
                   dustResult[3] + '\n' +
                   dustResult[4] + '\n' +
                   dustResult[5] + '\n')
    imageFD = open('SearchMap.gif', 'rb')
    ImagePart = MIMEImage(imageFD.read())
    imageFD.close()

    # 만들었던 mime를 MIMEBase에 첨부
    message.attach(msg)
    message.attach(ImagePart)


    # 헤더에 첨부 파일에 대한 정보 추가
    message.add_header('Content-Disposition', 'MapSearchResult', filename="map.gif")

    # 로컬 SMTP 서버가 없을 경우 계정이 있는 다른 서버를 사용하면 된다.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(me, password)
    s.sendmail(me, you, message.as_string())
    s.quit()
def RoadProcess():
    select=roadComboBox.get()
    # if(select=='금강 자전거길'):
    #     photo = PhotoImage(file=select)
    # elif(select== '낙동강 자전거길'):
    #
    # elif (select == '남한강 자전거길'):
    # elif (select == '동해안 자전거길'):
    # elif (select == '북한강 자전거길'):
    # elif (select == '새재 자전거길' ):
    # elif(select== '섬진강 자전거길'):
    # elif (select == '아라 자전거길'):
    # elif (select == '영산강 자전거길'):
    # elif (select == '오천 자전거길'):
    # elif (select == '한강종주 자전거길'):
    final = (select+".png")
    photo = PhotoImage(file=final)
    roadImage.configure(image=photo, width=1200, height=700)
    roadImage.image = photo
#-------------------------------------------------------------------------------------  탭을 추가부분
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='자전거 보관소 위치')
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='자전거 도로')
tabControl.pack(expand=1, fill="both")

#------------------------------------------------------------------------------------- 탭안에 뭐 넣을지 각각 정해주기
vBigTable = ttk.LabelFrame(tab1)
vBigTable.grid(column=0, row=0)
#
# titleTable = ttk.LabelFrame(vBigTable, text='타이틀프레임')
# titleTable.grid(column=0, row=0)

# mainTable = ttk.LabelFrame(vBigTable)
# mainTable.grid(column=0, row=1)

bicycleBigTable = ttk.LabelFrame(vBigTable)
bicycleBigTable.grid(column=0, row=0)

bicycleSemiTable = ttk.LabelFrame(bicycleBigTable,text='지도 검색창')
bicycleSemiTable.grid(column=0, row=0)
bicycleTable1 = ttk.LabelFrame(bicycleSemiTable)
bicycleTable1.grid(column=0, row=0)

bicycleEntry = Entry(bicycleTable1 )
bicycleEntry.grid(column=1, row=0)
bicycleButton = Button(bicycleTable1, font = buttonFont , text = "검색",command=bycicleProcess)
bicycleButton.grid(column=2, row=0)

bicycleTable2 = ttk.LabelFrame(bicycleSemiTable)
bicycleTable2.grid(column=0, row=1,sticky='W')

bicycleText = Text(bicycleTable2 , font = textFont, width = 40, height = 10)
bicycleText.grid(column=0, row=0, sticky='W')


weatherBigTable = ttk.LabelFrame(bicycleBigTable, text='날씨정보 검색창')
weatherBigTable.grid(column=1, row=0)
weatherTable1 = ttk.LabelFrame(weatherBigTable)
weatherTable1.grid(column=0, row=0)
weatherTableForImage = ttk.LabelFrame(weatherBigTable)
weatherTableForImage.grid(column=0, row=0)

#photo = PhotoImage(file="clean.gif")
#weatherImage =Label(weatherTable1,image=photo)
#weatherImage.grid(column=0,row=0)



weatherComboBox = ttk.Combobox(weatherTable1)
weatherComboBox['values'] = ('서울', '인천', '강원도', '충청도', '전라도','경상도')
weatherComboBox.grid(column=2, row=0)
weatherButton = Button(weatherTable1, font = buttonFont, text = "검색",command=WeatherProcess)
weatherButton.grid(column=3, row=0, sticky='W')

weatherTable2 = ttk.LabelFrame(weatherBigTable)
weatherTable2.grid(column=0, row=1)

weatherText = Text(weatherTable2, font = textFont, width = 40, height = 10)
weatherText.grid(column=0, row=1, sticky='W')


dustBigTable = ttk.LabelFrame(bicycleBigTable, text='미세먼지정보 검색창')
dustBigTable.grid(column=2, row=0)
dustTable1 = ttk.LabelFrame(dustBigTable)
dustTable1.grid(column=0, row=0)

dustComboBox = ttk.Combobox(dustTable1)
dustComboBox['values'] = ('강동구', '강서구', '강동구', '강북구')
dustComboBox.grid(column=1, row=0)
dustButton = Button(dustTable1, font = buttonFont, text = "검색",command=DustProcess)
dustButton.grid(column=2, row=0, sticky='W')

dustTable2 = ttk.LabelFrame(dustBigTable)
dustTable2.grid(column=0, row=1)

dustText = Text(dustTable2, font = textFont, width = 40, height = 10)
dustText.grid(column=0, row=1, sticky='W')


EmailTable = ttk.LabelFrame(bicycleBigTable, text='메일', width = 20)
EmailTable.grid(column=3, row=0)



mailIDLabel = Label(EmailTable, text = "ID")
mailIDLabel.grid(column=0, row=1, pady = 2)
mailIDEntry = Entry(EmailTable, width = 30)
mailIDEntry.grid(column=0, row=2)

mailPasswordLabel = Label(EmailTable, text = "PASSWORD")
mailPasswordLabel.grid(column=0, row=3, pady = 3)
mailPasswordEntry = Entry(EmailTable, width = 30)
mailPasswordEntry.grid(column=0, row=4)

LabelSpace2 = Label(EmailTable, text = " ")
LabelSpace2.grid(column=0, row=5, pady = 10)

mailLabel = Label(EmailTable, text = "보내는 주소")
mailLabel.grid(column=0, row=8)
mailSendEntry = Entry(EmailTable,bg="yellow", fg="black", width = 30)
mailSendEntry.grid(column=0, row=9)
mailButton = Button(EmailTable, font = buttonFont, text = "전송!",command=SendMail)
mailButton.grid(column=0, row=10)

BottomTable = ttk.LabelFrame(vBigTable, text='지도 이미지')
BottomTable.grid(column=0, row=2)

photo = PhotoImage(file="SearchMap.gif")
boganImage =Label(BottomTable)
boganImage.grid(column=0,row=0)


#-------------------------------------------------------------------------------------
RoadTable = ttk.LabelFrame(tab2, width = 20)
RoadTable.grid(column=0, row=0)
RoadTo = ttk.LabelFrame(RoadTable, width = 20)
RoadTo.grid(column=0, row=0)
roadComboBox = ttk.Combobox(RoadTo)
roadComboBox['values'] = ('금강 자전거길', '낙동강 자전거길', '남한강 자전거길', '동해안 자전거길', '북한강 자전거길','새재 자전거길','섬진강 자전거길','아라 자전거길','영산강 자전거길', '오천 자전거길','한강종주 자전거길')
roadComboBox.grid(column=0, row=0)
roadButton = Button(RoadTo, font = buttonFont , text = "검색",command=RoadProcess)
roadButton.grid(column=1, row=0)
RoadPic = ttk.LabelFrame(RoadTable, width = 20)
RoadPic.grid(column=0, row=1)

roadImage =Label(RoadPic,width = 171)
roadImage.grid(column=0,row=1)
#-------------------------------------------------------------------------------------
win.mainloop()