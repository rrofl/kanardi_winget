from tkinter import *
from customtkinter import *
import os

deactivate_automatic_dpi_awareness()

width = 500
length = 450
x = 0
current_path = os.getcwd()
aplikacje = []
zestawy = []
nazwy_winget = []
wybrane_oprogramowanie = []

dict_oprogramowanie = {
    'Google Chrome' : 'Google.Chrome',
    'Mozilla Firefox' : 'Mozilla.Firefox',
    'Opera' : 'Opera.Opera',
    '7 Zip' : '7zip.7zip',
    'WinRAR' : 'RARLab.WinRAR',
    'Adobe' : 'Adobe.Acrobat.Reader.64-bit',
    'VLC' : 'VideoLAN.VLC',
    'Slack' : 'SlackTechologies.Slack',
    'Zoom' : 'Zoom.Zoom',
    'Skype' : 'Microsoft.Skype',
}

dict_zestawy = {
    'Standard' : ''
}

for key in dict_oprogramowanie.keys():
    aplikacje.append(key)
    nazwy_winget.append(dict_oprogramowanie[key])

for key in dict_zestawy.keys():
    zestawy.append(key)
    nazwy_winget.append(dict_zestawy[key])

def standard():
    chrome.toggle()
    adobe.toggle()
    sevenzip.toggle()
    vlc.toggle()

def instalacja_oprogramowania():
    if var0.get() == 'on':
        wybrane_oprogramowanie.append(nazwy_winget[0])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[0])
        except:
            print('Program Google Chrome nie zostal wybrany')
    if var1.get() == 'on':
        wybrane_oprogramowanie.append(nazwy_winget[1])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[1])
        except:
            print('Program Mozilla Firefox nie zostal wybrany')
    if var2.get() == 'on':
        wybrane_oprogramowanie.append(nazwy_winget[2])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[2])
        except:
            print('Program 7 Zip nie zostal wybrany')
    if var3.get() == 'on':
        wybrane_oprogramowanie.append(nazwy_winget[3])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[3])
        except:
            print('Program WinRAR nie zostal wybrany')
    if var4.get() == 'on':
        wybrane_oprogramowanie.append(nazwy_winget[4])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[4])
        except:
            print('Program Adobe nie zostal wybrany')
    if var5.get() == 'on':
        wybrane_oprogramowanie.append(nazwy_winget[5])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[5])
        except:
            print('Program VLC nie zostal wybrany')
    if var6.get() == 'on':
        wybrane_oprogramowanie.append(nazwy_winget[6])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[6])
        except:
            print('Program Slack nie zostal wybrany')
    if var01.get() == 'on':
        print(wybrane_oprogramowanie)
    with open(f'{current_path}/lista_programow.txt', 'w') as f:
        for item in wybrane_oprogramowanie:
            f.write(f'{item}\n')
        print('Done')
    # with open(f'{current_path}/lista_programow.txt', 'r') as f:
    #     for line in f:
    #         os.system(f'winget install -g {item} --accept-package-agreements --accept-source-agreements')

# for i in range(1, len(dict_oprogramowanie)):
#     exec(f'var_{i} = i')

window = CTk()
window.title('Oprogramowanie')
window.geometry(f'{width}x{length}')
window.wm_iconbitmap(f'{current_path}/kanardi.ico')

var0 = StringVar(value='off')
var1 = StringVar(value='off')
var2 = StringVar(value='off')
var3 = StringVar(value='off')
var4 = StringVar(value='off')
var5 = StringVar(value='off')
var6 = StringVar(value='off')
var7 = StringVar(value='off')
var8 = StringVar(value='off')
var9 = StringVar(value='off')

var01 = StringVar(value='off')

#OPROGRAMOWANIE
chrome = CTkCheckBox(window, text=aplikacje[0], variable=var0, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
chrome.place(x=width/15, y=100)

mozilla = CTkCheckBox(window, text=aplikacje[1], variable=var1, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
mozilla.place(x=width/2.6, y=100)

opera = CTkCheckBox(window, text=aplikacje[2], variable=var2, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
opera.place(x=width/1.4, y=100)

sevenzip = CTkCheckBox(window, text=aplikacje[3], variable=var3, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
sevenzip.place(x=width/15, y=150)

winrar = CTkCheckBox(window, text=aplikacje[4], variable=var4, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
winrar.place(x=width/2.6, y=150)

adobe = CTkCheckBox(window, text=aplikacje[5], variable=var5, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
adobe.place(x=width/15, y=250)

vlc = CTkCheckBox(window, text=aplikacje[6], variable=var6, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
vlc.place(x=width/15, y=200)

slack = CTkCheckBox(window, text=aplikacje[7], variable=var7, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
slack.place(x=width/2.6, y=200)

zoom = CTkCheckBox(window, text=aplikacje[8], variable=var8, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
zoom.place(x=width/1.4, y=200)

skype = CTkCheckBox(window, text=aplikacje[9], variable=var9, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
skype.place(x=width/1.4, y=150)

#ZESTAWY
standard = CTkCheckBox(window, text=zestawy[0], variable=var01, command=standard, onvalue='on', offvalue='off', font=('Calibri Bold', 14))
standard.place(x=width/15, y=350)

programy = CTkLabel(window, 
                    text=f'Wybierz oprogramowanie \ndo instalacji: ', 
                    font=('Calibri Bold', 30), bg_color='grey')
programy.place(x=width/5.5, y=length/100)

zestawy_napis = CTkLabel(window, 
                    text='Zestawy', 
                    font=('Calibri Bold', 24))
zestawy_napis.place(x=width/2.4, y=300)

przycisk = CTkButton(window, 
                     text='Zainstaluj!', 
                     command=instalacja_oprogramowania, 
                     font=('Calibri Bold', 19))
przycisk.place(x=width/2.8,y=length-60)

ja = CTkLabel(window, text='by Artur Drab', font=('Calibri', 12)).place(x=width/1.25, y=length/1.06)

window.resizable(0,0)
window.mainloop()