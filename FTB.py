from pystyle import System
System.Clear()
import instaloader
import time
import datetime
import random
import os
import sys
import re
import pyfiglet
import webbrowser
import matplotlib.pyplot as plt
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from colorama import Fore, Style, init
import json

# تهيئة مكتبة Colorama لجعل الألوان تعمل على جميع الأنظمة
init(autoreset=True)
console = Console()

# تحديد اللغة الافتراضية
language = "en"  # يمكن تغييرها إلى "ar" (عربي) حسب اختيار المستخدم

# رسائل اللغة الإنجليزية والعربية
lmlk = ("FB Security Pro" , "FB P  ro C 2" , "DIC MOJO" , "X X C 0 2 M","B L A C K   P A T H",'S M A G N T A R','P C C H E','P R O F X - X','B A N A A R','F O X I N G','F O C U S T O O L','L P P','I N S T A G O','B L A C K I N S T A')
messages = {
    "en": {
        "banner": f"{random.choice(lmlk)}",
        "privacy_check": "Account Privacy Check",
        "password_check": "Password Strength Test",
        "phishing_check": "Phishing Awareness Test",
        "security_center": "Open Facebook Security Center",
        "exit": "Exit",
        "enter_username": "Enter username for privacy check:",
        "enter_password": "Enter password to test strength:",
        "wrong_option": "Invalid option, try again.",
        "notification": "Notification sound triggered",
        "password_strength": "Password strength: ",
        "private": "Private 🔒",
        "public": "Public 🔓",
        "warning": "Warning! The account is exposed to the public!",
        "phishing_warning": "Potential Phishing Link Detected",
        "safe_link": "Safe link",
        "loading": "Loading...",
        "goodbye": "Goodbye from the tool.",
        "choose_language": "Choose your language (en/ar):"
    },
    "ar": {
        "banner": "FB أداة الأمان",
        "privacy_check": "فحص خصوصية الحساب",
        "password_check": "اختبار قوة كلمة المرور",
        "phishing_check": "اختبار الوعي بالتصيد الاحتيالي",
        "security_center": "فتح مركز الأمان في فيسبوك",
        "exit": "خروج",
        "enter_username": "أدخل اسم المستخدم لفحص الخصوصية:",
        "enter_password": "أدخل كلمة المرور لاختبار القوة:",
        "wrong_option": "خيار غير صحيح، حاول مرة أخرى.",
        "notification": "تم تشغيل صوت الإشعار",
        "password_strength": "قوة كلمة المرور: ",
        "private": "خاص 🔒",
        "public": "عام 🔓",
        "warning": "تنبيه! الحساب مكشوف للعامة!",
        "phishing_warning": "الرابط قد يكون تصيدًا احتياليًا!",
        "safe_link": "رابط آمن",
        "loading": "جاري التحميل...",
        "goodbye": "تم الخروج من الأداة.",
        "choose_language": "اختر لغتك (en/ar):"
    }
}

# تهيئة ملف JSON لتخزين الأحداث والعمليات
log_file = "user_info_log.json"

def log_event(event_data):
    try:
        if os.path.exists(log_file):
            with open(log_file, "r", encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []

        data.append(event_data)

        with open(log_file, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        console.print(f"[red]Error logging event: {e}[/red]")
def show_banner():
    os.system("cls" if os.name == "nt" else "clear")  # تنظيف الشاشة قبل عرض البانر
    banner = pyfiglet.figlet_format(messages[language]["banner"], font="STANDARD", justify="left")
    
    # الحصول على التاريخ والوقت الحالي
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # تنسيق البانر ليشمل اسم صاحب الأداة والتاريخ
    banner_with_details = f"{banner}\n© Mohammed Alaa Mohammed < > {current_time}\n"
    
    # طباعة البانر
    console.print(f"[bold cyan]{banner_with_details}[/bold cyan]")

# شريط تحميل وهمي لإضافة تأثير احترافي
def loading_bar(task_name):
    with Progress(
        SpinnerColumn(), TextColumn("[bold cyan]{task.description}"), BarColumn()
    ) as progress:
        task = progress.add_task(f"{task_name}", total=100)
        for _ in range(25):
            time.sleep(random.uniform(0.1, 0.2))
            progress.update(task, advance=4)

# فحص خصوصية الحساب
def check_privacy(username):
    console.print(Panel(f"🔍 [bold yellow]{messages[language]['privacy_check']}: {username}[/bold yellow]"))
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        loading_bar(messages[language]["loading"])

        table = Table(title="Privacy Check Results", show_header=True, header_style="bold magenta")
        table.add_column("Feature", style="cyan")
        table.add_column("Status", style="green")

        privacy_status = messages[language]["private"] if profile.is_private else messages[language]["public"]
        table.add_row("Privacy", privacy_status)
        table.add_row("Followers", str(profile.followers))
        table.add_row("Following", str(profile.followees))
        table.add_row("Posts", str(profile.mediacount))

        # إضافة تفاصيل أخرى مع التحقق من وجود السمات
        birthday = "Not Available"
        if hasattr(profile, 'birthday'):
            birthday = profile.birthday
        
        biography = profile.biography if hasattr(profile, 'biography') else "Not Available"
        location = profile.location if hasattr(profile, 'location') else "Not Available"
        
        table.add_row("Birthday", birthday)
        table.add_row("Biography", biography)
        table.add_row("Location", location)
        
        if not profile.is_private:
            table.add_row("⚠️ [bold red]" +  messages [language] ["warning"] + "[/bold red]")

        console.print(table)

        # حفظ جميع البيانات في ملف JSON
        user_data = {
            "username": username,
            "privacy_status": privacy_status,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "birthday": birthday,
            "biography": biography,
            "location": location,
            "is_private": profile.is_private
        }
        
        log_event(user_data)

        # جمع بيانات المنشورات الأخيرة
        posts_data = []
        for post in profile.get_posts():
            posts_data.append({
                "caption": post.caption,
                "likes": post.likes,
                "comments": post.comments
            })

        # رسم بياني لعدد الإعجابات والتعليقات
        post_titles = [f"Post {i+1}" for i in range(len(posts_data))]
        likes = [post["likes"] for post in posts_data]
        comments = [post["comments"] for post in posts_data]
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(post_titles, likes, color='blue', label='Likes')
        ax.bar(post_titles, comments, color='green', label='Comments', alpha=0.7)
        ax.set_xlabel('Posts')
        ax.set_ylabel('Count')
        ax.set_title(f"Likes & Comments on {username}'s Posts")
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        console.print(f"[red]❌ Error during privacy check: {e}[/red]")
        log_event({
            "event": "privacy_check_failed",
            "username": username,
            "error_message": str(e)
        })

# باقي الكود كما هو ولكن مع تسجيل العمليات في ملف JSON لجميع الخيارات
# إضافة استخدام اللغات مع تخصيص الرسائل بناءً على لغة المستخدم، مثل:

# عند استدعاء الدالة في `main()`:
# لاختيار اللغة:
def choose_language():
    global language
    language_choice = console.input(f"[bold green]{messages[language]['choose_language']} [/bold green]")
    if language_choice == "ar":
        language = "ar"
    elif language_choice ==   '0' :    
        exit ()
    else:
        language = "en"

# القائمة الرئيسية التي تعرض خيارات الأداة
def main():
    show_banner()
    choose_language()
    
    while True:
        console.print(Panel(f"[bold cyan]1️⃣  {messages[language]['privacy_check']}[/bold cyan]\n"
                            f"[bold cyan]2️⃣  {messages[language]['password_check']}[/bold cyan]\n"
                            f"[bold cyan]3️⃣  {messages[language]['phishing_check']}[/bold cyan]\n"
                            f"[bold cyan]4️⃣  {messages[language]['security_center']}[/bold cyan]\n"
                            f"[bold cyan]5️⃣  {messages[language]['exit']}[/bold cyan]", title="🔍 [bold yellow]Main Menu[/bold yellow]"))

        choice = console.input("[bold green]Choose option: [/bold green]")

        if choice == "1":
            username = console.input(f"[bold cyan]{messages[language]['enter_username']} [/bold cyan]")
            check_privacy(username)
        elif choice == "2":
            password = console.input(f"[bold cyan]{messages[language]['enter_password']} [/bold cyan]")
            password_strength_test(password)
        elif choice == "3":
            phishing_test()
        elif choice == "4":
            console.print("[bold blue]🌍 Opening Facebook Security Center in the browser...[/bold blue]")
            open_security_center()
        elif choice == "5":
            console.print(f"[bold red]{messages[language]['goodbye']}[/bold red]")
            sys.exit()
        else:
            console.print(f"[bold red]{messages[language]['wrong_option']}[/bold red]")

if __name__ == "__main__":
    main()
