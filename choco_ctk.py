from tkinter import *
from customtkinter import *
import os

deactivate_automatic_dpi_awareness()

width = 500
length = 550
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
    standard.configure(window, fg_color = 'green')

def check():
    if chrome.get() == 'on':
        chrome.configure(window, fg_color = 'green')
    if mozilla.get() == 'on':
        mozilla.configure(window, fg_color = 'green')
    if opera.get() == 'on':
        opera.configure(window, fg_color = 'green')
    if sevenzip.get() == 'on':
        sevenzip.configure(window, fg_color = 'green')
    if winrar.get() == 'on':
        winrar.configure(window, fg_color = 'green')
    if adobe.get() == 'on':
        adobe.configure(window, fg_color = 'green')
    if vlc.get() == 'on':
        vlc.configure(window, fg_color = 'green')
    if slack.get() == 'on':
        slack.configure(window, fg_color = 'green')
    if zoom.get() == 'on':
        zoom.configure(window, fg_color = 'green')
    if skype.get() == 'on':
        skype.configure(window, fg_color = 'green')

def instalacja_oprogramowania():
    if var0.get() == 'on':
        if nazwy_winget[0] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[0])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[0])
        except:
            print('Program Google Chrome nie zostal wybrany')
    if var1.get() == 'on':
        if nazwy_winget[1] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[1])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[1])
        except:
            print('Program Mozilla Firefox nie zostal wybrany')
    if var2.get() == 'on':
        if nazwy_winget[2] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[2])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[2])
        except:
            print('Program Opera nie zostal wybrany')
    if var3.get() == 'on':
        if nazwy_winget[3] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[3])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[3])
        except:
            print('Program 7 Zip nie zostal wybrany')
    if var4.get() == 'on':
        if nazwy_winget[4] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[4])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[4])
        except:
            print('Program WinRAR nie zostal wybrany')
    if var5.get() == 'on':
        if nazwy_winget[5] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[5])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[5])
        except:
            print('Program Adobe nie zostal wybrany')
    if var6.get() == 'on':
        if nazwy_winget[6] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[6])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[6])
        except:
            print('Program VLC nie zostal wybrany')
    if var7.get() == 'on':
        if nazwy_winget[7] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[7])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[7])
        except:
            print('Program Slack nie zostal wybrany')
    if var8.get() == 'on':
        if nazwy_winget[8] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[8])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[8])
        except:
            print('Program Zoom nie zostal wybrany')
    if var9.get() == 'on':
        if nazwy_winget[9] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[9])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[9])
        except:
            print('Program Skype nie zostal wybrany')
    open(f'{current_path}/lista_programow.txt', "w").close()
    with open(f'{current_path}/lista_programow.txt', 'w') as f:
        f.truncate(16)
        for item in wybrane_oprogramowanie:
            f.write(f'{item}\n')
            print(item)
    # with open(f'{current_path}/lista_programow.txt', 'r') as f:
    #     for line in f:
    #         os.system(f'winget install -g {item} --accept-package-agreements --accept-source-agreements')

def cleanup():
    os.system(f'{current_path}/cleanup.bat')

def raport():
    nazwa_raportu = os.system('wmic bios get serialnumber')
    with open(f'{current_path}/{nazwa_raportu}.txt', 'w') as f:
        f.write('tworzenie raportu')

window = CTk()
set_appearance_mode("dark")
window.title('Kanardi')
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
chrome = CTkCheckBox(window, text=aplikacje[0], variable=var0, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
chrome.place(x=width/13, y=100)

mozilla = CTkCheckBox(window, text=aplikacje[1], variable=var1, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
mozilla.place(x=width/2.4, y=100)

opera = CTkCheckBox(window, text=aplikacje[2], variable=var2, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
opera.place(x=width/1.35, y=100)

sevenzip = CTkCheckBox(window, text=aplikacje[3], variable=var3, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
sevenzip.place(x=width/13, y=150)

winrar = CTkCheckBox(window, text=aplikacje[4], variable=var4, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
winrar.place(x=width/2.4, y=150)

adobe = CTkCheckBox(window, text=aplikacje[5], variable=var5, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
adobe.place(x=width/13, y=250)

vlc = CTkCheckBox(window, text=aplikacje[6], variable=var6, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
vlc.place(x=width/13, y=200)

slack = CTkCheckBox(window, text=aplikacje[7], variable=var7, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
slack.place(x=width/2.4, y=200)

zoom = CTkCheckBox(window, text=aplikacje[8], variable=var8, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
zoom.place(x=width/1.35, y=200)

skype = CTkCheckBox(window, text=aplikacje[9], variable=var9, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
skype.place(x=width/1.35, y=150)

#ZESTAWY
standard = CTkCheckBox(window, text=zestawy[0], variable=var01, command=standard, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
standard.place(x=width/13, y=350)

programy = CTkLabel(window, 
                    text=f'Wybierz oprogramowanie \ndo instalacji: ', 
                    font=('Calibri Bold', 30))
programy.place(x=width/5.5, y=length/100)

zestawy_napis = CTkLabel(window, 
                    text='Zestawy', 
                    font=('Calibri Bold', 30))
zestawy_napis.place(x=width/2.4, y=300)

przycisk_zainstaluj = CTkButton(window, 
                     text='Zainstaluj!', 
                     command=instalacja_oprogramowania, 
                     font=('Calibri Bold', 20))
przycisk_zainstaluj.place(x=width/6,y=length-140)

przycisk_cleanup = CTkButton(window, 
                     text='Cleanup!', 
                     command=cleanup, 
                     font=('Calibri Bold', 20))
przycisk_cleanup.place(x=width/6,y=length-80)

przycisk_raport = CTkButton(window, 
                     text='Generuj \nraport!', 
                     command=raport, 
                     font=('Calibri Bold', 20))
przycisk_raport.place(x=width/1.8,y=length-120)

ja = CTkLabel(window, text='by Artur Drab', font=('Calibri', 12)).place(x=width/1.18, y=length/1.06)

window.resizable(0,0)
window.mainloop()