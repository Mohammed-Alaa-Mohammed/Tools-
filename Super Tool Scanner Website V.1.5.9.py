import requests
from bs4 import BeautifulSoup
from pystyle import *
import datetime
from tqdm import tqdm
import time

# Tool information and logging setup
dt = datetime.datetime.now()
log_file = "scan_log.txt"

# Start the logging file
with open(log_file, "a") as f:
    f.write(f"\n--- Scan started on {dt} ---\n")

print ("              \n\t\t\t[↓↓ Notes For Help You.. ↓↓:] ")
print("﹌" * 20)
print ("""\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Don't Use https ,\33[39;0m Use http://www.link.com
\n\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Developer By : \33[39;0m Mohammed Alaa Mohammed
\n\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Tools Name and Versoin Website Scanner for Vulnerabilities\33[39;0m , V.4
\n\33[36;1m[\33[39;0m-\33[96;1m]\33[39;0m\33[35;2m Last Versoin V.5 Of at \33[39;0m"""+f"{dt}")
print ("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
print("﹌" * 20)

def scan_website(url):
    # Log the website being scanned
    with open(log_file, "a") as f:
        f.write(f"\nScanning website: {url}\n")

    # Loading animation
    for _ in tqdm(range(100), "\33[32;1mLoading……\33[39m", unit=' Wait... '):
        time.sleep(.40)

    try:
        # Send GET request to website
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for links in the website
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href:
                print(f"Found link: {href}")
                with open(log_file, "a") as f:
                    f.write(f"Found link: {href}\n")
                # Perform vulnerability tests on each link
                test_sql_injection(href)
                test_xss(href)
                test_csrf(href)
                test_lfi(href)
                test_ssrf(href)
                test_rce(href, "Possible RCE vulnerability in")
                test_open_redirect(href)
    except requests.exceptions.RequestException as e:
        print(f"\nError accessing {url}: {e}")
        with open(log_file, "a") as f:
            f.write(f"Error accessing {url}: {e}\n")

# Vulnerability Tests
def test_sql_injection(url):
    # SQL Injection Test
    payload = "' OR '1'='1"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url)
        if "syntax error" in response.text.lower():
            print(f"Possible SQL Injection vulnerability in: {url}")
            with open(log_file, "a") as f:
                f.write(f"SQL Injection vulnerability in: {url}\n")
    except requests.exceptions.RequestException as e:
        log_error("SQL Injection", url, e)

def test_xss(url):
    # XSS Vulnerability Test
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url)
        if payload in response.text:
            print(f"Possible XSS vulnerability in: {url}")
            with open(log_file, "a") as f:
                f.write(f"XSS vulnerability in: {url}\n")
    except requests.exceptions.RequestException as e:
        log_error("XSS", url, e)

def test_csrf(url):
    # CSRF Vulnerability Test
    try:
        response = requests.get(url)
        if "csrf" in response.text.lower():
            print(f"Possible CSRF vulnerability in: {url}")
            with open(log_file, "a") as f:
                f.write(f"CSRF vulnerability in: {url}\n")
    except requests.exceptions.RequestException as e:
        log_error("CSRF", url, e)

def test_lfi(url):
    # LFI Vulnerability Test
    payload = "../../../../etc/passwd"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url)
        if "root:x" in response.text:
            print(f"Possible LFI vulnerability in: {url}")
            with open(log_file, "a") as f:
                f.write(f"LFI vulnerability in: {url}\n")
    except requests.exceptions.RequestException as e:
        log_error("LFI", url, e)

def test_ssrf(url):
    # SSRF Vulnerability Test
    test_url = f"{url}?url=http://127.0.0.1"
    try:
        response = requests.get(test_url)
        if "Internal" in response.text:
            print(f"Possible SSRF vulnerability in: {url}")
            with open(log_file, "a") as f:
                f.write(f"SSRF vulnerability in: {url}\n")
    except requests.exceptions.RequestException as e:
        log_error("SSRF", url, e)

def test_rce(url, vuln_name):
    # RCE Vulnerability Test
    payload = "; echo RCE"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url)
        if "RCE" in response.text:
            print(f"{vuln_name}: {url}")
            with open(log_file, "a") as f:
                f.write(f"{vuln_name}: {url}\n")
    except requests.exceptions.RequestException as e:
        log_error("RCE", url, e)

def test_open_redirect(url):
    # Open Redirect Vulnerability Test
    payload = "/redirect?url=http://malicious.com"
    test_url = f"{url}{payload}"
    try:
        response = requests.get(test_url, allow_redirects=True)
        if response.url == "http://malicious.com":
            print(f"Possible Open Redirect vulnerability in: {url}")
            with open(log_file, "a") as f:
                f.write(f"Open Redirect vulnerability in: {url}\n")
    except requests.exceptions.RequestException as e:
        log_error("Open Redirect", url, e)

def log_error(vuln_type, url, error):
    # Log errors encountered during vulnerability testing
    print(f"Error testing {vuln_type} on {url}: {error}")
    with open(log_file, "a") as f:
        f.write(f"Error testing {vuln_type} on {url}: {error}\n")

# Tool Usage
Write.Print("[🚨❗🚨] Don't Use >| https , Use example: (http://www.google.com)", Colors.yellow, interval=.0)
print("\n" + "﹌" * 20)
website_url = input("[🌐]\33[92;1m URL \33[39;0m: ⋙⋙⋙⋙┆ ")
if website_url == '':
    print ("\n\33[91;1mTry...again return Run Code...")
    exit()
print ("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
print("﹌" * 20)
scan_website(website_url)

# End of program
def end_program():
    # End log and print exit message
    print("﹌" * 20)
    print("\n\33[31;1mProcess finished with exit\t\33[39;0m")
    with open(log_file, "a") as f:
        f.write("--- Scan completed ---\n")

end_program()
# ........................................................
# Developer : Mohammed Alaa
# Under Developing...
# run code > python 'filename.py'
# .........................................................
