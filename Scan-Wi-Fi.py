import subprocess
import qrcode

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split(
    '\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8',
                                                                                                       errors="backslashreplace").split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))


def QRCODE():
    from tqdm import tqdm
    from time import sleep
    print('\n')
    ask = input("\nFor Got QRCODE Of This Write Done : ").lower()
    discrip = (f"{data}"  , "\n" , f" {profiles}")
    if ask == "done":
        for _ in tqdm(range(0, 100), unit="%", desc="Wait..."):
            sleep(.1)
            User_Input = qrcode.make(discrip)
            User_Input.save("Scan Network Wi-Fi.png")
        print("\33[32;1mQRCODE Image Saved and Success\33[39;8m")
    else:
        print("\nOK..the Code is End.\n\f")


QRCODE()

