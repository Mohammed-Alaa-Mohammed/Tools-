import time
import requests
import psutil
import platform
import socket
from pystyle import *
from tqdm import *

# رسالة الترحيب
print("""
\33[34;2m
\t\t ██  ██████  
\t\t ██  ██  ██ 
\t\t ██  ██████  
\t\t ██  ██      
\t\t ██  ██      
\33[39;0m""")


print ("\n\33[36;1m[\33[39;0m-\33[36;1m]\33[39;0m\33[35;2m Press Enter To Show your device Info about IP \33[39;0m\n")
print ("\33[36;1m[\33[39;0m-\33[36;1m]\33[39;0m\33[33;2m Developer By :::| Mohammed Alaa Mohammed \33[39;0m\n")
print ("\33[36;1m[\33[39;0m-\33[36;1m]\33[39;0m\33[94;2m GitHub :::| https://www.github.com/DARKGITHUBPRO/\n\33[39;0m")
print ("\33[36;1m[\33[39;0m-\33[36;1m]\33[39;0m Create Tool By \33[31;2mPython Language\33[39;0m\n")
print ("\33[36;1m[\33[39;0m-\33[36;1m]\33[39;0m\33[31;2m Version Number \33[39;0m Of V1.4.5\33[39;0m\n")
def get_detailed_ip_info(ip_address):
    # الاتصال بـ API لجلب معلومات IP الخارجية
    response = requests.get(f"http://ipinfo.io/{ip_address}/json")
    data = response.json() if response.status_code == 200 else {}
    return {
        "[-] City": data.get("city", "Unknown"),
        "[-] Region": data.get("region", "Unknown"),
        "[-] Country": data.get("country", "Unknown"),
        "[-] Organization": data.get("org", "Unknown"),
        "[-] Timezone": data.get("timezone", "Unknown"),
        "[-]\33[32;1m Location\33[39;0m": data.get("loc", "Unknown")
    }


def get_device_info():
    # معلومات الجهاز الكاملة
    device_info = {
        "[-] Platform": platform.system(),
        "[-] Platform Version": platform.version(),
        "[-] Platform Release": platform.release(),
        "[-] Architecture": platform.architecture()[0],
        "[-] Hostname": socket.gethostname(),
        "[-] Username": platform.node(),
        "[-] Processor": platform.processor(),
        "[-] Processor Cores": psutil.cpu_count(logical=False),
        "[-] Processor Logical Cores": psutil.cpu_count(logical=True),
        "[-] Processor Speed (MHz)": psutil.cpu_freq().max if psutil.cpu_freq() else "Unknown",
        "[-] Total RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "[-] Available RAM (GB)": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "[-] CPU Usage (%)": psutil.cpu_percent(interval=1),
        "[-] Memory Usage (%)": psutil.virtual_memory().percent,
    }
    return device_info


def get_network_info():
    # معلومات الشبكة المحلية
    local_ip = socket.gethostbyname(socket.gethostname())

    # الحصول على MAC Address لأي واجهة متاحة
    mac_address = "Unknown"
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                mac_address = addr.address
                break
        if mac_address != "Unknown":
            break

    network_info = {
        "[-] Local IP Address": local_ip,
        "[-] MAC Address": mac_address,
        "[-] External IP Address": requests.get("https://api64.ipify.org").text,
        "[-] Active Connections": [conn for conn in psutil.net_connections() if conn.status == 'ESTABLISHED'],
    }
    return network_info


def display_info():

    # عرض المعلومات بشكل منسق
    ip_address = input(
        "\33[36;1m[\33[39;0m-\33[36;1m]\33[39;0m\33[32;1m Enter IP address to fetch info,or press Enter to use your IP: \33[39;0m") or requests.get(
        "https://api64.ipify.org").text
    print ("\n ")
    for done in tqdm(range(150), "\33[29;1mGetting...\33[39;0m", unit="\33[31;1m Processing\33[39;0m"):
        time.sleep(0.061)  # وقت قصير للتحميل

    ip_info = get_detailed_ip_info(ip_address)
    device_info = get_device_info()
    network_info = get_network_info()

    print("\33[36;1m\n--- Device Information ---\33[39;0m")
    for key, value in device_info.items():
        print(f"{key}: {value}")

    print("\33[35;1m\n--- Network Information ---\33[39;0m")
    for key, value in network_info.items():
        print(f"{key}: {value}")

    print("\33[31;1m\n--- IP Information ---\33[39;0m")
    for key, value in ip_info.items():
        print(f"{key}: {value}")


display_info()

#  V.5.TB