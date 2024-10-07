import os
import sys
import time
import tqdm
from PyQt6 import QtCore , QtGui , QtWidgets
from PyQt6.QtGui import  QPixmap , QAction
from click import progressbar

# جزء عمل الناقذه
# from PyQt6 import *

app = QtWidgets.QApplication(sys.argv) # امر التعامل من Terminal

Screen = QtWidgets.QTreeWidget() # امر عمل النافذة

Screen.show() # امر اظهار النافذه
# Screen.resize(600,500) # امر التحكم في حجم النافذه

# Screen.move(500,150) # امر التحكم في مكان النافذه

Screen.setGeometry(450,200,800,520)

Screen.setWindowTitle("DISCOR v.1.0") # set Title of App

# Set App icon
Screen.setWindowIcon(QtGui.QIcon(r"Icon APP.png"))

# use css to set a background color of App , windowname.setStyleSheet('css code')
Screen.setStyleSheet('background-color:#fff;')#
# Screen.setStyleSheet('background-color:#212225;')#212225

#====================================================================================================
# # جزء Buttons

# Set A Button with Value
button_download = QtWidgets.QPushButton('Download Video',Screen)
button_download.show()
button_download.resize(150,40)
button_download.move(350,230)

button_download.setStyleSheet("""
    QPushButton {
        background-color: #25a1ff;
        color: #fff;
        font-size: 14px;
        border-radius: 20px;
        font-family: bold;
    }
    QPushButton:hover {
        background-color: #0099cc;  /* لون الخلفية عند الوقوف على الزر */
        border: 2px solid #0000001;  /* حدود متوهجة */
        box-shadow: 0px 0px 10px #00ffcc;  /* تأثير التوهج */
    }
""")

# button_message.clicked.connect(input)





button_exit = QtWidgets.QPushButton("Exit",Screen)
button_exit.show()
button_exit.resize(150,40)
button_exit.move(350,280)

button_exit.setStyleSheet("""
  QPushButton {
        background-color: #ED4C67;
        color: #fff;
        font-size: 14px;
        border-radius: 20px;
        font-family: bold;
    }
    QPushButton:hover {
        background-color: #FF6B81;  /* لون الخلفية عند الوقوف على الزر */
        border: 2px solid #FFCCCC;  /* حدود متوهجة */
        box-shadow: 0px 0px 10px #FFCCCC;  /* تأثير التوهج */
    }
""")
# button_exit.setToolTip("Close App") # اظهار رساله عن الوقوف علي الزر
# الدرس 13 هو وضع ايقونه في الزر
button_exit.clicked.connect(exit)

#====================================================================================================
# جزء Entry , Label
label_message = QtWidgets.QLabel('<b>Welcome To APP</b>',Screen)
label_message.show()
label_message.move(370,15)
# label_message.setStyleSheet(""
#                             "color:red;"
#                             "font-size:16px;"
#
#                             "")

entry_username = QtWidgets.QLineEdit(Screen)
entry_username.show()
entry_username.move(300,120)
entry_username.resize(250,25)
#====================================================================================================
# Style of entry_username

entry_username.setStyleSheet(""
                             "color:#B53471;"
                             "background-color:#0000010;"
                             "font-size:15px;")


entry_password = QtWidgets.QLineEdit(Screen)
entry_password.show()
entry_password.move(300,150)
entry_password.resize(250,25)

# Style of entry_password

entry_password.setStyleSheet(""
                             "color:#009432;"
                             "background-color:#0000010;"
                             "font-size:15px;")

# جزء checkBox
check_box = QtWidgets.QCheckBox('Show Password',Screen)
check_box.show()
check_box.move(305,190)
check_box.setStyleSheet(""
                        "color:#cc112c;")
#====================================================================================================
# التعامل مع الصور عن طريق Labels
photo_1 = QtWidgets.QLabel(Screen)
photo = QPixmap("Icon APP.png").scaled(70,70) # العرض و الارتفاع
photo_1.setPixmap(photo)
# photo.show()
photo_1.show()
# photo_1.resize(50,50)
photo_1.move(380,45)
#====================================================================================================
# التعامل مع الرسائل messagebox
# Q = QtWidgets.QMessageBox.question(Screen,'login','متابعة الدخول')
#
# Q_Error = QtWidgets.QErrorMessage(Screen)
# Q_Error.showMessage("قد يكون هناك تحديث للبرنامج راجع اخر نسخة!")

#====================================================================================================
# التعامل مع الرسائل و الدوال للأزرار اي عند الضغط علي زر تظهر رساله MessageBox

# def MessageBox_Show ():
#     Q_1 = QtWidgets.QMessageBox.question(Screen,'CLOSE','are You Close Program!')
# def MessageBox_Show ():
#     Q_1 = QtWidgets.QMessageBox.question(Screen,'CLOSE','are You Close Program!')
#     if Q_1 == QtWidgets.QMessageBox.Yes:
#         exit(app)
#     else:
#         print('Error...')
# لم يتم الإكمال كان في  الدرس 23 يكمل في 24 مع الاحداث و الشروط
# الدرس 24 الشروط مع الرسائل
#====================================================================================================
# Create Menubar
#
# menubar = Screen.menuBar()
# man_1 = menubar.addMenu('Save')
# man_2 = menubar.addMenu('Save as')
# man_3 = menubar.addMenu('Upload Files')
# man_4 = menubar.addMenu('Delete File')
# man_5 = menubar.addMenu('Create New فاتوره')
# man_6 = menubar.addMenu('Edit فاتوره')
# #################################################################
# add_to_1 = QAction('استرداد الفواتير',Screen)
# add_to_2 = QAction('تعديل الفواتير',Screen)
# add_to_3 = QAction('انشاء الفواتير',Screen)
# add_to_4 = QAction('حذف الفواتير',Screen)
# add_to_5 = QAction('حفظ الفواتير',Screen)
# add_to_6 = QAction('حفظ الفواتير بإسمها',Screen)
# # add_to = QtWidgets.QAction('Upload Files')
# # add_to = QtWidgets.QAction('Upload Files')
# # add_to = QtWidgets.QAction('Upload Files')
# man_1.addAction(add_to_5)# حفظ بإسم
# man_3.addAction(add_to_1)# استرداد الفواتير
# man_4.addAction(add_to_4)# حذف الفواتير
# man_5.addAction(add_to_3)# انشاء فاتوره
# man_6.addAction(add_to_2)# تعديل فاتوره
# man_2.addAction(add_to_6)

# man_1.addAction(add_to)

#====================================================================================================
lb_prog = QtWidgets.QLabel('<b>متابة التحميل </b>', Screen)
lb_prog.move(370, 350)
lb_prog.show()

# إنشاء شريط التقدم
progressbar_set = QtWidgets.QProgressBar(Screen)
progressbar_set.setGeometry(250, 380, 400, 30)
progressbar_set.setValue(100)  # تعيين القيمة الابتدائية
progressbar_set.show()

# وظيفة لزيادة قيمة شريط التقدم بشكل تدريجي
def update_progress_bar():
    for i in range(101):  # 101 خطوة من 0 إلى 100
        time.sleep(0.02)  # تأخير لتوضيح حركة شريط التقدم
        progressbar_set.setValue(i)  # تعيين القيمة الجديدة
        QtWidgets.QApplication.processEvents()  # تحديث واجهة المستخدم

# استدعاء الدالة لتحديث شريط التقدم
update_progress_bar()

#====================================================================================================
# برمجة جزء التاريخ واظهاره
Cal = QtWidgets.QCalendarWidget(Screen)
Cal.show()
app.exec() # امر تشغيل البرنامج