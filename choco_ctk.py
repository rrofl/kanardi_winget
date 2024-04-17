from tkinter import *
from customtkinter import *
import os
import wmi
import subprocess
import csv

deactivate_automatic_dpi_awareness()

width = 500
length = 550
current_path = os.getcwd()
aplikacje = []
zestawy = []
nazwy_winget = []
wybrane_oprogramowanie = []
c = wmi.WMI()

dict_oprogramowanie = {
    'Google Chrome' : 'Google.Chrome',
    'Mozilla Firefox' : '',
    'Opera' : 'Opera.Opera',
    '7 Zip' : '7zip.7zip',
    'WinRAR' : 'RARLab.WinRAR',
    'Adobe' : 'Adobe.Acrobat.Reader.64-bit',
    'VLC' : 'VideoLAN.VLC',
    'Slack' : 'SlackTechologies.Slack',
    'Zoom' : 'Zoom.Zoom',
    'Skype' : 'Microsoft.Skype',
    'Framework 3.5' : '',
    'WhatsApp' : 'WhatsApp.WhatsApp',
    'M365 BS' : 'Microsoft.Office',
}

dict_zestawy = {
    'Standard' : ''
}

#dodaje klucze(nazwy widoczne w aplikacji) i wartosci(nazwy winget) do list z dziennika dict_oprogramowanie
for key in dict_oprogramowanie.keys():
    aplikacje.append(key)
    nazwy_winget.append(dict_oprogramowanie[key])

#dodaje klucze(nazwy widoczne w aplikacji) i wartosci(nazwy winget) do list z dziennika dict_zestawy
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
    else:
        pass
    if mozilla.get() == 'on':
        mozilla.configure(window, fg_color = 'green')
    else:
        pass
    if opera.get() == 'on':
        opera.configure(window, fg_color = 'green')
    else:
        pass
    if sevenzip.get() == 'on':
        sevenzip.configure(window, fg_color = 'green')
    else:
        pass
    if winrar.get() == 'on':
        winrar.configure(window, fg_color = 'green')
    else:
        pass
    if skype.get() == 'on':
        skype.configure(window, fg_color = 'green')
    else:
        pass
    if vlc.get() == 'on':
        vlc.configure(window, fg_color = 'green')
    else:
        pass
    if slack.get() == 'on':
        slack.configure(window, fg_color = 'green')
    else:
        pass
    if zoom.get() == 'on':
        zoom.configure(window, fg_color = 'green')
    else:
        pass
    if adobe.get() == 'on':
        adobe.configure(window, fg_color = 'green')
    else:
        pass
    if whatsapp.get() == 'on':
        whatsapp.configure(window, fg_color = 'green')
    else:
        pass
    if m365_bs.get() == 'on':
        m365_bs.configure(window, fg_color = 'green')
    else:
        pass
    if framework_35.get() == 'on':
        framework_35.configure(window, fg_color = 'green')
    else:
        pass

def zmien_nazwe():
    input_tekst = input_zmien_nazwe.get(1.0, END+"-1c")
    if input_tekst == '':
        print('Puste pole nazwy PC, pomijam zmiane nazwy..')
    elif input_tekst != '':
        os.system(f'wmic computersystem where caption="%computername%" rename "{input_tekst}"')
        print(input_tekst)
    else:
        print('Blad!')

def instalacja_oprogramowania():
    #jesli checkbox jest zaznaczony dodaje nazwe z wingeta do listy wybrane_oprogramowanie, jesli nie - pass
    if var0.get() == 'on':
        if nazwy_winget[0] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[0])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[0])
        except:
            pass
    if var1.get() == 'on':
        os.system('start Mozilla.exe')
    else:
        pass
    if var2.get() == 'on':
        if nazwy_winget[2] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[2])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[2])
        except:
            pass
    if var3.get() == 'on':
        if nazwy_winget[3] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[3])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[3])
        except:
            pass
    if var4.get() == 'on':
        if nazwy_winget[4] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[4])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[4])
        except:
            pass
    if var5.get() == 'on':
        if nazwy_winget[5] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[5])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[5])
        except:
            pass
    if var6.get() == 'on':
        if nazwy_winget[6] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[6])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[6])
        except:
            pass
    if var7.get() == 'on':
        if nazwy_winget[7] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[7])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[7])
        except:
            pass
    if var8.get() == 'on':
        if nazwy_winget[8] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[8])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[8])
        except:
            pass
    if var9.get() == 'on':
        if nazwy_winget[9] in wybrane_oprogramowanie:
            pass
        else:
            wybrane_oprogramowanie.append(nazwy_winget[9])
    else:
        try:
            wybrane_oprogramowanie.remove(nazwy_winget[9])
        except:
            pass
    if var10.get() == 'on':
        os.system('DISM /Online /Enable-Feature /FeatureName:NetFx3 /All')
    else:
        pass
    #otwiera plik 'lista programow.txt', usuwa wczesniejsze nazwy, wprowadza nowe i instaluje programy z pliku
    open(f'{current_path}/lista_programow.txt', "w").close()
    # with open(f'{current_path}/lista_programow.txt', 'w') as f:
    #     f.truncate(16)
    #     for item in wybrane_oprogramowanie:
    #         f.write(f'{item}\n')
    #         print(item)
    with open(f'{current_path}/lista_programow.txt', 'w') as f:
        f.truncate(16)
        for item in wybrane_oprogramowanie:
            print(subprocess.run(f'winget install -e --id {item} --force --accept-package-agreements --accept-source-agreements --scope machine'))
    zmien_nazwe()

def cleanup():
    os.system(f'{current_path}/cleanup.bat')

def raport_csv():       
    bios = c.Win32_BIOS()[0]
    #win32 = c.Win32_Process()[0]
    serial_number = 'wmic bios get serialnumber'
    nazwa_raportu = os.popen(serial_number).read().replace("\n", "").replace("  ", "").replace(" ", "").replace("SerialNumber", "")
    string = ','.join(wybrane_oprogramowanie)
    if nazwa_raportu == 'TobefilledbyO.E.M.':
        nazwa_raportu = os.environ['COMPUTERNAME']
    else:
        pass
    with open(f'{current_path}/raporty/{nazwa_raportu}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['Nazwa systemu', ','+nazwa_raportu])
        writer.writerow(['Wersja BIOS', ','+bios.Version])
        writer.writerow(['Data wydania BIOS', ','+bios.ReleaseDate])
        writer.writerow(['Zainstalowane programy', ','+string])
    print('Raport zostal wygenerowany')

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
var10 = StringVar(value='off')
var11 = StringVar(value='off')
var12 = StringVar(value='off')
var01 = StringVar(value='off')

#OPROGRAMOWANIE
chrome = CTkCheckBox(window, text=aplikacje[0], variable=var0, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50, fg_color = 'black')
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

framework_35 = CTkCheckBox(window, text=aplikacje[10], variable=var10, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
framework_35.place(x=width/13, y=300)

whatsapp = CTkCheckBox(window, text=aplikacje[11], variable=var11, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
whatsapp.place(x=width/2.4, y=250)

m365_bs = CTkCheckBox(window, text=aplikacje[12], variable=var12, command=check, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
m365_bs.place(x=width/1.35, y=250)

#ZESTAWY
standard = CTkCheckBox(window, text=zestawy[0], variable=var01, command=standard, onvalue='on', offvalue='off', font=('Calibri Bold', 14), corner_radius=50)
standard.place(x=width/13, y=390)

napis_programy = CTkLabel(window, 
                    text=f'Wybierz oprogramowanie \ndo instalacji: ', 
                    font=('Calibri Bold', 30))
napis_programy.place(x=width/5.5, y=length/100)

napis_zestawy = CTkLabel(window, 
                    text='Zestawy', 
                    font=('Calibri Bold', 30))
napis_zestawy.place(x=width/2.45, y=340)

napis_zmien_nazwe = CTkLabel(window, 
                        text='Zmien nazwę\nkomputera ↓',
                        text_color = 'yellow',
                        font=('Calibri Bold', 14))
napis_zmien_nazwe.place(x=width/10,y=440)

input_zmien_nazwe = CTkTextbox(window,
                        fg_color = 'yellow',
                        width = 150,
                        height = 20,
                        text_color = 'black',
                        border_spacing = 0,
                        activate_scrollbars = False,
                        wrap = 'none',
                        font=('Calibri Bold', 12))
input_zmien_nazwe.place(x=width/30,y=480)

napis_zostaw_nazwe = CTkLabel(window, 
                        text='(zostaw puste pole jesli\n nie chcesz zmieniac nazwy)',
                        text_color = 'grey',
                        font=('Calibri Bold', 10))
napis_zostaw_nazwe.place(x=width/14,y=513)

przycisk_zainstaluj = CTkButton(window, 
                     text='Zainstaluj', 
                     command=instalacja_oprogramowania, 
                     font=('Calibri Bold', 20))
przycisk_zainstaluj.place(x=width/2.75,y=450)

przycisk_cleanup = CTkButton(window, 
                     text='Cleanup', 
                     command=cleanup, 
                     font=('Calibri Bold', 20))
przycisk_cleanup.place(x=width/2.75,y=490)

przycisk_raport = CTkButton(window, 
                     text='Generuj \nraport!', 
                     command=raport_csv, 
                     font=('Calibri Bold', 20))
przycisk_raport.place(x=width/1.45,y=length-95)

ja = CTkLabel(window, text='by Artur Drab', font=('Calibri', 12)).place(x=width/1.18, y=length/1.05)

window.resizable(0,0)
window.mainloop()