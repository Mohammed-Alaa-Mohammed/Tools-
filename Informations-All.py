from pystyle import *
from pystyle import System
System.Clear()
import time
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
import os
medo = Console()


def START (code) :

    code = code
    code = '20018739901DARK_WOH'
    
    checking = medo.input("\n[bold cyan][+] Enter Code For Start Tool : ").strip()
    while True :
        if checking == code :
            System.Clear()
            break 

        else :
            exit()
# START ('20018739901DARK_WOH')        
#=============================================================
tool_logo = ("S Y S T E M",'P A T H S','O S S Y S T E M','A L L I N F O','S Y S T O O L')
colors = (f"{Fore.CYAN}",f'{Fore.GREEN}',f'{Fore.LIGHTRED_EX}',f'{Fore.LIGHTGREEN_EX}',f'{Fore.MAGENTA}',f'{Fore.RED}',f'{Fore.BLUE}',f'{Fore.LIGHTRED_EX}')
print ("ـ"*70)
print (f"\n{random.choice(colors)}",pyfiglet.figlet_format(f'{random.choice(tool_logo)}',font='BIG',justify="left"),"\33[39;0m"+"ـ"*70+"\n\n© Mohammed Alaa Mohammed",datetime.datetime.now())
print (f"{random.choice(colors)} Tool Name : A.X.A+")
print (f"{random.choice(colors)} Tool Version : 2.1.1")
print (f"{random.choice(colors)} Developer Name : M.A.M")
print (f"{random.choice(colors)} Last Update Tool Is : V.2.1.1 \33[39;0m")

time.sleep(5)
#=============================================================
def CLS () -> None :
        from pystyle import System
        System.Clear()
# CLS()

print ("ـ"*70)
SHOW = medo.print("""[bold cyan]
[1-] Remove A File or Folder Set Path
[bold yellow][2-] Get All Informations From Files To Path
[bold green][3-] Createing A Files or A Folders To Set Name
[cyan][4-] Tool Update..!
[bold red][0-] Exit - Close
""")           
print ("ـ"*70)
list_choose = Write.Input("\n[+] Enter Your Choose Of The List From 1 TO 5 : ",Colors.red_to_yellow,interval=.07)
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
                    print ("-"*50)
                    medo.print("\n[red][1] File Path Size Is : {:2f}[/red] B / Bit\n".format(size))
                    medo.print(f"[red][2] File Path Last Access : {last_acc}\n")
                    medo.print(f"\n[cyan][3] File Path Last Edit In : {last_edit}\n")
                    medo.print(f"\n[yellow][4] File Path Created In  : {create_file}\n")
                    medo.print(f"\n[magenta][4] The Full File Path Fact Is  : {is_path}\n")
                    print ("-"*50)
    elif list_choose == '3' :
        
        medo.print("[bold magenta][$] This Choose Is Not Found Now Try Again To Next Time...!\n")
        break
    
    elif  list_choose == '0' :

        medo.print("\n[bold yellow][!] GoodBay....! 👋\n\a")
        break 
    
    elif list_choose == '4' :
        
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