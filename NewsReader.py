# NewsReader Application

from tkinter import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
import time
import pyttsx3
from threading import Thread

engine = pyttsx3.init()
engine.setProperty('rate',160)

root = Tk()
root.title("News Reader")
root.resizable(0,0)
root.geometry("700x600")

chooseNews = StringVar()
NewsType=StringVar()

imgs = Image.open("images/start.png")
imgs = imgs.resize((108, 55), Image.ANTIALIAS)
imgs=ImageTk.PhotoImage(imgs)
imgok = Image.open("images/okButton.png")
imgok= imgok.resize((108, 55), Image.ANTIALIAS)
imgok=ImageTk.PhotoImage(imgok)
image2 =Image.open('images/Best.jpg')
img2 = image2.resize((700, 600), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(img2)
back_img1 = Image.open("images/Back.jpg")
back_img2 = back_img1.resize((90, 45), Image.ANTIALIAS)
back_img3 = ImageTk.PhotoImage(back_img2)


def greet():
    tim = int(time.strftime("%H"))
    if 5 <= tim < 12:
        print("\n                 Good Morning, I'm your news reader assistant")
        engine.say("Good Morning, I'm your news reader assistant")
        engine.runAndWait()
    elif 12 <= tim< 17:
        print("\n                 Good Afternoon, I'm your news reader assistant")
        engine.say("Good Afternoon, I'm your news reader assistant")
        engine.runAndWait()
    elif 17 < tim < 19:
        print("\n                 Good Evening, I'm your news reader assistant")
        engine.say("Good Evening, I'm your news reader assistant")
        engine.runAndWait()
    elif 19 <= tim :
        print("\n         Hi, Its quite late but I'll tell you all important headlines ASAP")
        engine.say("Hi, Its quite late but I'll tell you all important headlines ASAP")
        engine.runAndWait()

news = ''
cano=0
var= IntVar()


def p4():
    engine.setProperty('rate',var.get())
    NewsSource = chooseNews.get()
    print('you selected newssource --> ', NewsSource)
    newsType=NewsType.get()
    print('you selected news-type --> ', newsType)
    news = ''
    fourthPage = Frame()
    fourthPage.place(x=0, y=0, width=700, height=600)
    fourthPage.configure(bg="Blue2")
    back_button = Button(fourthPage, text="<-", image=back_img3, borderwidth=0, bg="light cyan", command=p3,
                         width=50, height=20)
    back_button.place(x=0, y=0)
    Messagelable = Label(fourthPage, fg="light cyan", text=newsType.capitalize(), bg="Blue2",
                       justify="center", font=("comic sans MS", 20))
    Messagelable.pack(pady=50)
    T = Text(fourthPage, height=4, width=50, wrap=WORD)
    T.pack(ipadx=10, ipady=10, side="left", expand=True, fill="both")

    if NewsSource == 'NDTV':
        url = "https://www.ndtv.com"
        den = {'world': '/world-news', 'science': '/science', 'business': '/business/your-money', 'health': '/health', 'india': '/india', 'top-stories': '/top-stories'}
        content = requests.get(url + den[newsType])
        soup = BeautifulSoup(content.text, 'html.parser')
        data = soup.select('.lisingNews .news_Itm .newsHdng')
        count = 1
        for i in data:
            news = news  + i.text+ '\n'
            tell=str(count) + "> " + i.text+ '\n'
            T.insert(END, tell)
            count += 1
    elif NewsSource =='India today':
        url = "https://www.indiatoday.in"
        den = {1: '/world', 2: '/science', 3: '/business', 4: '/lifestyle/health', 5: '/india', 6: '/top-stories'}
        content = requests.get(url + den[6])
        soup = BeautifulSoup(content.text, 'html.parser')
        data = soup.find_all('h2', class_='')
        news = ''
        count = 1
        for i in range(len(data)):
            news = news  + data[i].text + '\n'
            tell = str(count) + "> " + data[i].text + '\n'
            T.insert(END, tell)
            count += 1
    elif NewsSource == 'easternherald':
        url = "https://www.easternherald.com/category"
        den = {1: '/gov-pol', 2: '/society', 3: '/entertainment', 4: '/climate', 5: '/economy', 6: '/health'}
        content = requests.get(url + den[3])
        soup = BeautifulSoup(content.text, 'html.parser')
        data = soup.select('.td-ss-main-content .entry-title ')
        news = ''
        for i in range(1, len(data)):
            news = news +  data[i].text + '\n'
            tell = str(i) + "> " + data[i].text + '\n'
            T.insert(END, tell)
    elif NewsSource == 'deccanchronicle':
        url = "https://www.deccanchronicle.com"
        den = {1: '/world', 2: '/nation', 3: '/business', 4: '/lifestyle', 5: 'sports', 6: '/entertainment'}
        content = requests.get(url + den[6])
        soup = BeautifulSoup(content.text, 'html.parser')
        data = soup.select('.stry-hd-sml-led2')
        news = ''
        count = 1
        for i in data:
            news = news + i.text + '\n'
            tell = str(count) + "> " + i.text + '\n'
            T.insert(END, tell)
            count += 1
    global newss
    newss = news
    k11 = Thread(target=readL)
    k11.start()


def readL():
    engine.say(newss)
    k=var.get()
    print(k)
    engine.setProperty('rate', k)
    print(newss)
    engine.runAndWait()


def p3():
    NewsSource=chooseNews.get()
    print('you clicked--> ', NewsSource)
    ThirdPage = Frame()
    ThirdPage.place(x=0, y=0, width=700, height=600)
    ThirdPage.configure(bg="Blue2")
    back_button = Button(ThirdPage, text="<-", image=back_img3, borderwidth=0, bg="light cyan",command=page,
                         width=50, height=20)
    back_button.place(x=0, y=0)
    Messagelable = Label(ThirdPage, fg="light cyan", text="Now \n Select type of news:", bg="Blue2",
                       justify="center", font=("comic sans MS", 20))
    Messagelable.pack(pady=50)
    speedVol = Scale(ThirdPage, from_=80, to=320, variable=var, orient=HORIZONTAL, label="speed")
    speedVol.place(x=593, y=0)
    var.set(160)
    choices=[]
    if NewsSource=='NDTV':
        choices=['world-news','science','business','health','india','top-stories']
        NewsType.set('top-stories')
    elif NewsSource=='India today':
        choices=['world','science','business','health','india','top-stories']
        NewsType.set('top-stories')
    elif NewsSource=='easternherald':
        choices=['economy','society','entertainment','health','climate','gov-pol']
        NewsType.set('economy')
    elif NewsSource=='deccanchronicle':
        choices = ['world', 'nation', 'business', 'lifestyle', 'sports', 'entertainment']
        NewsType.set('nation')
    newsMenu = OptionMenu(ThirdPage, NewsType, *choices)
    newsMenu.place(x=250, y=250, height=30, width=200)
    okButton = Button(ThirdPage, text="ok", borderwidth=0, image=imgok,bg="blue2", command=p4)
    okButton.place(x=300, y=400, width=100, height=50)

def page():
    k = Thread(target=greet)
    k.start()
    secondPage = Frame()
    secondPage.place(x=0, y=0, width=700, height=600)
    secondPage.configure(bg="Blue2")
    Messagelable = Label(secondPage, fg="light cyan", text="Welcome ! \n Select any source for news",bg='Blue2',
                            justify="center", font=("comic sans MS", 20))
    choices = ['NDTV', 'India today', 'easternherald', 'deccanchronicle']
    chooseNews.set(choices[0])  # set the default option
    newsMenu = OptionMenu(secondPage, chooseNews, *choices)
    newsMenu.place(x=250, y=250, height=30, width=200)
    Messagelable.pack(pady=100)
    okButton = Button(secondPage, text="ok", borderwidth=0, image=imgok,bg="blue2",command=p3)
    okButton.place(x=300, y=400, width=100, height=50)


home_frame = Frame()
home_frame.configure(bg="Blue2")
home_frame.place(x=0, y=0, width=700, height=600)
backgimg=Label(home_frame,image =image1)
backgimg.place(x=-2,y=0)
btnstart = Button(home_frame, text='Start', image=imgs,borderwidth=0, bg="blue2", command=page)
btnstart.place(x=305, y=430, height=50, width=100)
root.mainloop()