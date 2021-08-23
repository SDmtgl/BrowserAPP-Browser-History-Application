# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:26:06 2021

@author: ~DMTGL~
"""

import os
import sys
import json
import platform
from browser_history import browsers
import browser_history as bh
import csv
from datetime import datetime, timedelta
import tkinter as tkn
from tkinter import *
from pkg_resources import *
import pkg_resources
#import pkg_resources.py2_warn



def csv_yaz(dosya_adi,histo):
    with open(dosya_adi,'w',newline="") as dosya:
        yaz = csv.writer(dosya,delimiter=";")
        yaz.writerows(histo)
        
    dosya.close()

def html_yaz(dosya_adi,histo):
   with open (dosya_adi,'w') as dosya:
       html_con =f"<html> <head><title>Web Browser History</title> </head><body><p>{histo}</p></body> </html>" 
       dosya.write("%s"% line for line in html_con)
       
   dosya.close()

def text_yaz(dosya_adi,histo):
    with open (dosya_adi,'w') as dosya:
        dosya.write("%s"% line for line in histo)
    
    dosya.close()

def json_yaz(dosya_adi,histo):
    with open(dosya_adi,'w') as dosya:
        json.dump(histo,dosya)
    dosya.close()

def createNewTkinter(history):
    " new window"
    try:
        if nw.state() == "normal": nw.focus()
    except NameError as e:
        print(e)
        nw = tkn.Toplevel()
        nw.geometry("585x370")
        text = Text(nw, height = 155, width = 100)
        text.pack()
        text.insert(tkn.END, history)

root = tkn.Tk()
root.geometry("585x370")
root.iconbitmap("browser.ico")
root.title("Web History")


history = bh.get_history()
his = history.histories #otomotik tüm tarayıcıların geçmişini alır

# Web History Çekme
chrome = browsers.Chrome()
firefox = browsers.Firefox()
edge = browsers.Edge()
opera = browsers.Opera()
chromium = browsers.Chromium()

#Edge 

edge_cikti = edge.fetch_history() 
his_edge = edge_cikti.histories #text
edge_files = edge.fetch_history().to_csv()
edge_files_json = edge.fetch_history().to_json()

#Chrome

chrome_cikti = chrome.fetch_history()
his_chrome = chrome_cikti.histories #text
chrome_files =chrome.fetch_history().to_csv()
chrome_files_json = chrome.fetch_history().to_json()

#Opera

opera_cikti = opera.fetch_history()
his_opera = opera_cikti.histories
opera_files = opera.fetch_history().to_csv()
opera_file_json = opera.fetch_history().to_json()

#Firefox

firefox_cikti = firefox.fetch_history()
his_firefox = firefox_cikti.histories
firefox_files = firefox.fetch_history().to_csv()
firefox_files_json = firefox.fetch_history().to_json()

#Chromium
chromium_cikti = chromium.fetch_history()
his_chromium = chromium_cikti.histories
chromium_files = chromium.fetch_history().to_csv()
chromium_files_json = chromium.fetch_history().to_json()

###

arka_fon = tkn.PhotoImage(file='Ekran.PNG')
arka_fon_label = tkn.Label(root, image= arka_fon)
arka_fon_label.place(x=0,y=0)

frame = tkn.Frame(root,bg='#354365',highlightbackground='gray',highlightthickness=3,width=200, height=200) #anchor='s'
frame.pack(expand=True,side="top")

#frame2 = tkn.Frame(root,bg='#354365',highlightbackground='gray',highlightthickness=3,width=200, height=200) #anchor='s'
#frame2.pack(anchor="se",side='top')


label = tkn.Label(frame, bg='#354365', fg='yellow',font=('Arial','25'), text="Web Browsers")
label.pack(expand=True)

# Edge History 

mb_edge= Menubutton(frame,bg='#B8BDC6', fg='#2B5545',font=('Arial','20'),text="Edge Browser History", relief = RIDGE)
mb_edge.pack(expand=True,side="top")
mb_menu = Menu(mb_edge, tearoff = 0)
mb_edge["menu"] = mb_menu
var_e1= IntVar()
var_e2= IntVar()
var_e3= IntVar()
var_e4= IntVar()
var_e5= IntVar()
mb_menu.add_checkbutton ( label="Edge Histroy View",variable=var_e5,command=lambda:createNewTkinter(edge_files))
mb_menu.add_checkbutton ( label="Edge Histroy TEXT File Format",variable=var_e1,command=lambda:text_yaz('History_Edge.txt', edge_files))
mb_menu.add_checkbutton ( label="Edge Histroy CSV File Format",variable=var_e2 ,command=lambda:csv_yaz('History_Edge.csv',his_edge))
mb_menu.add_checkbutton ( label="Edge Histroy HTML File Format",variable=var_e3 ,command=lambda:html_yaz('History_Edge.html', edge_files))
mb_menu.add_checkbutton ( label="Chromium History JSON File Format",variable=var_e4 ,command=lambda:json_yaz('History_Edge.json', edge_files_json))
mb_edge.pack(expand=True,side="top")

# Chrome History

mb_chrome= Menubutton(frame,bg='#B8BDC6', fg='#2B5545',font=('Arial','20'), text="Chrome Browser History", relief = RIDGE)
mb_chrome.pack(expand=True,side="top")
mb_menu2 = Menu(mb_chrome, tearoff = 0)
mb_chrome["menu"] = mb_menu2
var_c1= IntVar()
var_c2= IntVar()
var_c3= IntVar()
var_c4= IntVar()
var_c5= IntVar()
mb_menu2.add_checkbutton ( label="Chrome Histroy View",variable=var_c5,command=lambda:createNewTkinter(chrome_files))
mb_menu2.add_checkbutton ( label="Chrome Histroy TEXT File Format",variable=var_c1,command=lambda:text_yaz('History_Chrome.txt', chrome_files) )
mb_menu2.add_checkbutton ( label="Chrome Histroy CSV File Format",variable=var_c2 ,command=lambda:csv_yaz('History_Chrome.csv',his_chrome))
mb_menu2.add_checkbutton ( label="Chrome Histroy HTML File Format",variable=var_c3 ,command=lambda:html_yaz('History_Chrome.html', chrome_files))
mb_menu2.add_checkbutton ( label="Chrome History JSON File Format",variable=var_c4 ,command=lambda:json_yaz('History_Chrome.json', chrome_files_json))
mb_chrome.pack(expand=True,side="top")

# Firefox History

mb_firefox= Menubutton(frame,bg='#B8BDC6', fg='#2B5545',font=('Arial','20'), text="Firefox Browser History", relief = RIDGE)
mb_firefox.pack(expand=True,side="top")
mb_menu3 = Menu(mb_chrome, tearoff = 0)
mb_firefox["menu"] = mb_menu3
var_f1= IntVar()
var_f2= IntVar()
var_f3= IntVar()
var_f4= IntVar()
var_f5= IntVar()
mb_menu3.add_checkbutton ( label="Firefox Histroy View",variable=var_f5,command=lambda:createNewTkinter(firefox_files))
mb_menu3.add_checkbutton ( label="Firefox History TEXT File Format",variable=var_f1,command=lambda:text_yaz('History_Firefox.txt', firefox_files) )
mb_menu3.add_checkbutton ( label="Firefox History CSV File Format",variable=var_f2 ,command=lambda:csv_yaz('History_Firefox.csv',his_firefox))
mb_menu3.add_checkbutton ( label="Firefox History HTML FileFormat",variable=var_f3 ,command=lambda:html_yaz('History_Firefox.html', firefox_files))
mb_menu3.add_checkbutton ( label="Firefox History JSON File Format",variable=var_f4 ,command=lambda:json_yaz('History_Firefox.json', firefox_files_json))
mb_firefox.pack(expand=True,side="top")

# Opera History

mb_opera= Menubutton(frame,bg='#B8BDC6', fg='#2B5545',font=('Arial','20'), text="Opera Browser History ", relief = RIDGE)
mb_opera.pack(expand=True,side="top")
mb_menu4 = Menu(mb_opera, tearoff = 0)
mb_opera["menu"] = mb_menu4
var_o1= IntVar()
var_o2= IntVar()
var_o3= IntVar()
var_o4= IntVar()
var_o5= IntVar()
mb_menu4.add_checkbutton ( label="Opera History View ",variable=var_o5,command=lambda:createNewTkinter(opera_files))
mb_menu4.add_checkbutton ( label="Opera History TEXT File Format",variable=var_o1,command=lambda:text_yaz('History_Opera.txt', opera_files) )
mb_menu4.add_checkbutton ( label="Opera History CSV File Format",variable=var_o2 ,command=lambda:csv_yaz('History_Opera.csv',his_opera))
mb_menu4.add_checkbutton ( label="Opera History HTML File Format",variable=var_o3 ,command=lambda:html_yaz('History_Opera.html', opera_files))
mb_menu4.add_checkbutton ( label="Opera History JSON File Format",variable=var_o4 ,command=lambda:json_yaz('History_Opera.json', opera_files_json))
mb_opera.pack(expand=True,side="top")

# Chromium History

mb_chromium= Menubutton(frame,bg='#B8BDC6', fg='#2B5545',font=('Arial','20'), text="Chromium Browser History", relief = RIDGE)
mb_chromium.pack(expand=True,side="top")
mb_menu5 = Menu(mb_chromium, tearoff = 0)
mb_chromium["menu"] = mb_menu5
var_ch1= IntVar()
var_ch2= IntVar()
var_ch3= IntVar()
var_ch4= IntVar()
var_ch5= IntVar()
mb_menu5.add_checkbutton ( label="Chromium History View ",variable=var_ch5,command=lambda:createNewTkinter(chromium_files))
mb_menu5.add_checkbutton ( label="Chromium History TEXT File Format",variable=var_ch1,command=lambda:text_yaz('History_Chromium.txt', chromium_files_files) )
mb_menu5.add_checkbutton ( label="Chromium History CSV File Format",variable=var_ch2 ,command=lambda:csv_yaz('History_Chromium.csv',his_chromium))
mb_menu5.add_checkbutton ( label="Chromium History HTML File Format",variable=var_ch3 ,command=lambda:html_yaz('History_Chromium.html', chromium_files))
mb_menu5.add_checkbutton ( label="Chromium History JSON File Format",variable=var_ch4 ,command=lambda:json_yaz('History_Chromium.json', chromium_files_json))
mb_chromium.pack(expand=True,side="top")




root.mainloop()

















