from aiogram.fsm.state import State,StatesGroup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from bs4 import BeautifulSoup as X
import requests

class logs(StatesGroup):
    start1=State()
    start2=State()


def obhavo(data1,vil):
    g=0
    if data1=='KUNLIK':
        g=1
    if data1=='HAFTALIK':
        g=7
    if vil=='TOSHKENT':
        data='ташкент'
    elif vil=='ANDIJON':
        data='андижан'
    elif vil=='NAMANGAN':
        data='наманган'
    elif vil=='BUXORO':
        data='бухара'
    elif vil=='SAMARQAND':
        data='самарканд'
    elif vil=="FARG'ONA":
        data='фергана'
    elif vil=='XORAZM':
        data='ургенч'
    elif vil=='QASHQADARYO':
        data='карші'
    elif vil=='SURXANDARYO':
        data='термез'
    elif vil=='JIZZAX':
        data='джизак'
    elif vil=='NAVOI':
        data='навої'
    elif vil=="SIRDARYO":
        data='гулістан'
        
    url = requests.get(f"https://sinoptik.ua/погода-{data}")

    html_t = X(url.content, "html.parser")
    a = html_t.select("#content")

    kunlik=''
    for i in a:
        for j in range(g):
            z=i.select('.date')[j].text
            x=i.select('.month')[j].text
            c=(i.select(".max")[j].text).split()[1]
            v=(i.select('.min')[j].text).split()[1]
            kunlik+=f"Oy: {x}\nKun: {z}\nHarorat max: {c}\nHarorat min: {v}\n\n"
    return kunlik

tur=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="KUNLIK"),KeyboardButton(text='HAFTALIK')],[KeyboardButton(text="ORTGA")]],resize_keyboard=True)

def viloyat():
    a=[]
    a.append([KeyboardButton(text="TOSHKENT"),KeyboardButton(text="XORAZM")])
    a.append([KeyboardButton(text="ANDIJON"),KeyboardButton(text="QASHQADARYO")])
    a.append([KeyboardButton(text="NAMANGAN"),KeyboardButton(text="SURXANDARYO")])
    a.append([KeyboardButton(text="BUXORO"),KeyboardButton(text="JIZZAX")])
    a.append([KeyboardButton(text="SAMARQAND"),KeyboardButton(text="NAVOIY")])
    a.append([KeyboardButton(text="FARG'ONA"),KeyboardButton(text="SIRDARYO")])
    a.append([KeyboardButton(text="Youtube")])
    return ReplyKeyboardMarkup(keyboard=a)


yyy=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="XONKILLER",url="https://www.youtube.com/@XONKILLER100K")]])



