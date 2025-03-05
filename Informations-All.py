from pystyle import *
from pystyle import System
System.Clear()
# ـــــــــــــــــــــــــــــــــــــ
import sys
import os
import platform
import time
import stat
from pathlib import Path

# ==============================================================
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
    TaskProgressColumn,
    MofNCompleteColumn,
)
# ===============================================================
from rich.console import Console
from rich.console import Console
import datetime
import random
import pyfiglet
from colorama import Fore

medo = Console()



def START (Keys) :


    Keys = ('1G7HkuGudjuwe997J','10C1g1IGOP','LL9hFU8bnQ','LOMI2a91tq')
    checking = medo.input("\n[bold cyan][+] Enter Code For Start Tool : ").strip()
    while True :
        if checking in Keys :
            System.Clear()
            break 

        else :
            medo.print(f"[→][bold red] Error In The This Code..You Write A : [/bold red]{checking}")
            exit()
# START (Keys=[f'{KeyError}'])        
#=============================================================
tool_logo = ("S Y S T E M",'P A T H S','O  S  S Y S T E M','A L L I N F O','S Y S T O O L','H A K  E R S')
colors = (f"{Fore.CYAN}",f'{Fore.GREEN}',f'{Fore.LIGHTRED_EX}',f'{Fore.LIGHTGREEN_EX}',f'{Fore.MAGENTA}',f'{Fore.RED}',f'{Fore.BLUE}',f'{Fore.LIGHTRED_EX}',f"{Fore.BLACK}",f'{Fore.YELLOW}',f'{Fore.GREEN}')
print ("ـ"*45)
print (f"{random.choice(colors)}",pyfiglet.figlet_format(f'{random.choice(tool_logo)}',font='BIG',justify="left"),"\33[39;0m"+"ـ"*45+"\n© Mohammed Alaa Mohammed",datetime.datetime.now())
print (f"{random.choice(colors)} Tool Name : A.X.A+")
print (f"{random.choice(colors)} Tool Version : 2.1.1")
print (f"{random.choice(colors)} Developer Name : M.A.M")
print (f"{random.choice(colors)} Last Update Tool Is : V.2.1.1 \33[39;0m")

time.sleep(.2)
#=============================================================
def CLS () -> None :
        from pystyle import System
        time.sleep(1)
        System.Clear()
        


print ("="*45)
SHOW = medo.print("""[bold cyan]
[1-] Remove A File or Folder Set Path
[yellow][2-] Get All Informations From Files To Path
[3-][bold red] Advanced[/bold red] Get All The Path Information Entered Put The File
[bold green][4-] Createing A Files or A Folders To Set Name
[cyan][5-] Tool Update..!
[bold yellow][6-] Get all Pictim Device Paths
[bold cyan][7-] Eavesdropping on WhatsApp Conversations [bold red][+] ! (Advanced Account)
[bold green][8-] Crack ZIP - RAR File Password , More [bold red][+] ! (Advanced Account)
[yellow][9-] Put Username [E-mail] To Get Password !! [If you forget it - - the account will be exposed to email leakage] 📢 
[bold red][0-] Exit - Close
\b""")           
print ("="*45)
# cli = (Colors.black_to_blue,Colors.black_to_green,Colors.blue_to_cyan,Colors.red_to_yellow,Colors.blue_to_white,Colors.gray,Colors.light_red,Colors.black_to_red,Colors.)
list_choose = input(f"\n{random.choice(colors)}[+] Enter Your Choose Of The List From\33[39;0m\33[32;1m 1\33[39;0m{random.choice(colors)} TO End List [+] : \33[39;0m").strip()
# Write.I(list_choose,Colors.green_to_cyan,interval=.2)
while True :

    if list_choose == '1' :


        file_path_get_input_remove = medo.input("\n\f[bold yellow][!] Enter File Path To Remove File : ")

        if os.path.exists(file_path_get_input_remove) :        
            print("\n")

            with Progress(
                SpinnerColumn("dots", style="bold green"),  # أيقونة التحميل المتحركة
                TextColumn("[bold cyan]{task.description}"),  # وصف المهمة
                BarColumn(bar_width=40, style="bold yellow", finished_style="bold bright_blue"),  # شريط التقدم
                TaskProgressColumn(),  # نسبة التقدم بالمئة
                TransferSpeedColumn(),  # سرعة التحميل
                TimeElapsedColumn(),  # الوقت المنقضي
                TimeRemainingColumn(),  # الوقت المتبقي
                MofNCompleteColumn(),  # عدد الخطوات المكتملة من الإجمالي
                )as progress:
                    task = progress.add_task(f"[bold cyan][+][/bold cyan] wait To Check If Path is True Will Remove...:", total=100)
                            # التقدم في شريط التحميل
                    for step in range(100):
                            time.sleep(.05)
                            #         # تحديث شريط التحميل بشكل مستمر
                            progress.update(task, advance=1)


            file_remove = os.remove(f"{file_path_get_input_remove}")
            medo.print('\n[bold green][✓] All Files Path is Remove...\n')
            ask_1 = medo.input("[bold cyan][!] Do You Want Try Again..? [y/n] : ").lower()
            if ask_1 == 'y' :
                continue
            else : 
                break
        else :
            medo.print(f"\n[bold red][~] Error This Path Not Found..>:|[/bold red] {file_path_get_input_remove}\n")    

    elif list_choose == '2' :

            file_path_get_info = medo.input("\n\f[bold yellow][!] Enter File Path To Get Some Informations : ")
            medo.print(f"\n[bold red][✓][/bold red] Your File Path Is : [bold green]{file_path_get_info}\n[/bold green]")
            if os.path.isfile (file_path_get_info) :

                    size = os.path.getsize(filename=file_path_get_info)
                    last_acc = os.path.getatime(filename=file_path_get_info)
                    last_edit = os.path.getmtime(filename=file_path_get_info)
                    create_file = os.path.getctime(filename=file_path_get_info)
                    is_path = os.path.abspath(file_path_get_info)
                    dir_path = os.path.dirname(file_path_get_info)
                    system_id = os.getpid()
                    print ("-"*45)
                    size_all = os.path.getsize(file_path_get_info) / os.path.getatime(file_path_get_info)
                    medo.print("[red][1] File Path Size Is : {:}[/red] B/Bit\n".format(size))
                    medo.print("[bold yellow][2] File Path Last Access : {:}\n".format(size_all))
                    medo.print(f"[cyan][3] File Path Last Edit In : {last_edit}\n")
                    medo.print(f"[yellow][4] File Path Created In  : {create_file}\n")
                    medo.print(f"[magenta][5] The Full File Path Fact Is  : {is_path}\n")
                    medo.print("[red][6] This Path To Folder Path Is : {:}\n".format(dir_path))
                    medo.print("[yellow][7] The This Path As File Name Is : {}\n".format(os.path.basename(file_path_get_info)))
                    medo.print(f"[bold yellow][8]More Infromations For File Path Is A : {sys.exc_info()}\n")
                    medo.print(f"[bold cyan][-] This PC - Laptop Name Is ID : {system_id}\n")
                    
                    print ("-"*45)
                    
            elif not os.path.exists (file_path_get_info)  :
                medo.print(f"[bold red][✕ ] Error This Path Not Found..>:|[/bold red] {file_path_get_info}\n")        
            ask_2 = medo.input("\n[bold cyan][!] Do You Want Try Again..? [y/n] : ").lower()
            if ask_2 == 'y' :
                    continue
            else : 
                        break
    elif list_choose == '3' :
                # دالة للحصول على معلومات الملف
        def get_file_info(file_path):
            try:
                # استخدام مكتبة os للحصول على معلومات الملف
                file_stats = os.stat(file_path)
                
                # استخدام مكتبة pathlib للحصول على معلومات إضافية
                file_path_obj = Path(file_path)
                
                # الحصول على تاريخ الإنشاء
                if platform.system() == "Windows":
                    creation_time = time.ctime(file_stats.st_ctime)
                else:
                    creation_time = time.ctime(file_stats.st_birthtime)
                
                # الحصول على تاريخ آخر تعديل
                modification_time = time.ctime(file_stats.st_mtime)
                
                # الحصول على تاريخ آخر وصول
                access_time = time.ctime(file_stats.st_atime)
                
                # الحصول على حجم الملف
                file_size = file_stats.st_size
                
                # الحصول على نوع الملف
                file_type = "File" if file_path_obj.is_file() else "Folder" if file_path_obj.is_dir() else "File Not Found"
                
                # الحصول على صلاحيات الملف
                file_permissions = stat.filemode(file_stats.st_mode)
                
                # الحصول على المالك والمجموعة (في أنظمة Unix)
                if platform.system() != "Windows":
                    import pwd
                    import grp
                    owner = pwd.getpwuid(file_stats.st_uid).pw_name
                    group = grp.getgrgid(file_stats.st_gid).gr_name
                else:
                    owner = "Not available in Windows"
                    group = "Not available in Windows"
                
                # الحصول على رقم inode (في أنظمة Unix)
                inode = file_stats.st_ino if platform.system() != "Windows" else "Not Available Windows"
                
                # عرض المعلومات
                print("=" * 45)
                medo.print(f"\n[red bold][1] File Full Path: {file_path}")
                medo.print("=" * 45)
                medo.print(f"[cyan bold][2] File Type: {file_type}\n")
                medo.print(f"[yellow bold][3] Creation Date: {creation_time}\n")
                medo.print(f"[magenta bold][4] Last Modification date: {modification_time}\n")
                medo.print(f"[bold red][5] Last Access date: {access_time}\n")
                medo.print(f"[bold yellow][6] File Size: {file_size} Bytes\n")
                medo.print(f"[bold green][7] File Permissions: {file_permissions}\n")
                medo.print(f"[bold cyan][8] Owner: {owner}\n")
                medo.print(f"[yellow bold][9] Group: {group}\n")
                medo.print(f"[bold magenta][10] Inode Number: {inode}")
                print("=" * 45)
            
            except FileNotFoundError:
                print(f"The file '{file_path}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

        # استقبال مسار الملف من المستخدم
        file_path = medo.input("\n[bold red][-][bold cyan] Please Enter The File Path :")
        get_file_info(file_path)
        ask_4 = medo.input("\n[bold cyan][!] Do You Want Try Again..? [y/n] : ").lower()
        if ask_4 == 'y' :
            continue
        else : 
            break

        # الحصول على معلومات الملف وعرضها
        


    elif list_choose == '4' :
        
        Write.Print("\n[?] This Choose Is Not Found Now Try Again To Next Time...!\n\n\f",Colors.light_red,interval=.02)
        ask_3 = medo.input("[bold cyan][!] Do You Want Try Again..? [y/n] : ").lower()
        if ask_3 == 'y' :
            continue
        else : 
            break

    
    elif  list_choose == '0' :
        

        medo.print("\n[bold yellow][!] GoodBay....! 👋\n\a")
        break 
    
    elif list_choose == '5' :
        
            with Progress(
                SpinnerColumn("dots", style="bold green"),  # أيقونة التحميل المتحركة
                TextColumn("[bold cyan]{task.description}"),  # وصف المهمة
                BarColumn(bar_width=40, style="bold yellow", finished_style="bold bright_blue"),  # شريط التقدم
                TaskProgressColumn(),  # نسبة التقدم بالمئة
                TransferSpeedColumn(),  # سرعة التحميل
                TimeElapsedColumn(),  # الوقت المنقضي
                TimeRemainingColumn(),  # الوقت المتبقي
                MofNCompleteColumn(),  # عدد الخطوات المكتملة من الإجمالي
                )as progress:
                    print("\n")
                    task = progress.add_task(f"{random.choice(colors)}Wait To Check Update...:", total=100)
                            # التقدم في شريط التحميل
                    for step in range(100):
                            time.sleep(.05)
                            #         # تحديث شريط التحميل بشكل مستمر
                            progress.update(task, advance=1)
            print (f"\n{random.choice(colors)}This is Tool is Last Update\n\33[39;0m")
            break
    
    
    else:

        medo.print("\n\t[bold red]⟦ ✕ Invalid Choose...✕ ⟧\n")
        break

# Last Update...
