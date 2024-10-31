

import requests
from bs4 import BeautifulSoup
from pystyle import *
import datetime

dt = datetime.datetime.now()
print ("              \n\t\t\t[↓↓ Notes For Help You.. ↓↓:] ")
print ("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
print ("""\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Don't Use https ,\33[39;0m Use http://www.link.com
\n\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Developer By : \33[39;0m Mohammed Alaa Mohammed
\n\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Tools Name and Versoin Website Scanner for Vulnerabilities\33[39;0m , V.4
\n\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Last Versoin V.5 Of at \33[39;0m"""+f"{dt}")
print ("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
import datetime


def فحص_الموقع(url):
    from tqdm import tqdm
    import time
    print("\n")
    for i in tqdm(range(100),"\33[32;1mLoading……\33[39m",unit=' Wait... '):
        "\n"
        time.sleep(.20)
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print ("\n\n")

        # البحث عن الروابط
        الروابط = soup.find_all('a')
        for رابط in الروابط:
            href = رابط.get('href')
            if href:
                print(f"تم العثور على رابط: {href}")
                اختبار_حقن_SQL(href)
                اختبار_XSS(href)
                اختبار_CSRF(href)
                اختبار_LFI(href)
    except requests.exceptions.RequestException as e:
        print(f"\nخطأ في الوصول إلى\n {url}: {e}")

def اختبار_حقن_SQL(url):
    payload = "' OR '1'='1"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url)
        if "syntax error" in response.text.lower():
            print(f"تم العثور على ثغرة حقن SQL محتملة في: {url}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في اختبار حقن SQL على {url}: {e}")

def اختبار_XSS(url):
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url)
        if payload in response.text:
            print(f"تم العثور على ثغرة XSS محتملة في: {url}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في اختبار XSS على {url}: {e}")

def اختبار_CSRF(url):
    try:
        response = requests.get(url)
        if "csrf" in response.text.lower():
            print(f"تم العثور على ثغرة CSRF محتملة في: {url}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في اختبار CSRF على {url}: {e}")

def اختبار_LFI(url):
    payload = "../../../../etc/passwd"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url)
        if "root:x" in response.text:
            print(f"تم العثور على ثغرة LFI محتملة في: {url}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في اختبار LFI على {url}: {e}")

# استخدام الأداة

Write.Print("[🚨❗🚨] Don't Use >| https , Useing ex : (http://www.google.com) ", Colors.yellow, interval=.0)
# تشغيل
print ("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
website_url = input("[🌐]\33[92;1m URL \33[39;0m: ⋙⋙⋙⋙┆ ")
if website_url == '':
    print ("\n\33[91;1mTry...again return Run Code...")
    exit()
print ("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
فحص_الموقع(website_url)


def نهاية_البرنامج():
    print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    print("\n\33[31;1mProcess finished with exit\t\33[39;0m")

نهاية_البرنامج()
