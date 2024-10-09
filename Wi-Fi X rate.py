import subprocess


def create_virtual_wifi(ssid, password):
    try:
        # تحقق من دعم الشبكة الافتراضية
        result = subprocess.run('netsh wlan show drivers', check=True, shell=True, capture_output=True, text=True)

        if "Hosted network supported  : Yes" not in result.stdout:
            print("المحول الخاص بك لا يدعم الشبكة الافتراضية (Hosted Network).")
            return

        # 1. إعداد شبكة Wi-Fi الافتراضية باستخدام netsh
        subprocess.run(f'netsh wlan set hostednetwork mode=allow ssid={ssid} key={password}', check=True, shell=True)

        # 2. بدء تشغيل الشبكة
        subprocess.run('netsh wlan start hostednetwork', check=True, shell=True)

        print(f"تم إنشاء شبكة Wi-Fi باسم {ssid} ويمكن الاتصال بها باستخدام كلمة المرور {password}.")

    except subprocess.CalledProcessError as e:
        print(f"حدث خطأ: {e}")
        if "The hosted network couldn't be started" in e.stderr:
            print("قد يكون المحول غير مفعل أو غير متاح.")
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")


def stop_virtual_wifi():
    try:
        # إيقاف الشبكة الافتراضية
        subprocess.run('netsh wlan stop hostednetwork', check=True, shell=True)
        print("تم إيقاف شبكة Wi-Fi.")

    except subprocess.CalledProcessError as e:
        print(f"حدث خطأ أثناء محاولة إيقاف الشبكة: {e}")
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")


if __name__ == "__main__":
    action = input("أدخل 'start' لإنشاء شبكة أو 'stop' لإيقافها: ").strip().lower()

    if action == 'start':
        ssid = input("أدخل اسم شبكة Wi-Fi الافتراضية (SSID): ")
        password = input("أدخل كلمة مرور لشبكة Wi-Fi (8 أحرف على الأقل): ")

        if len(password) >= 8:
            create_virtual_wifi(ssid, password)
        else:
            print("كلمة المرور يجب أن تكون 8 أحرف أو أكثر.")
    elif action == 'stop':
        stop_virtual_wifi()
    else:
        print("أمر غير صحيح.")
