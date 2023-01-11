'''
    Nexo -- New Generation Internet Resourece Crawler

    Using the following Package:
        Tkinter -- GUI
        Urllib3 -- Web Core

'''

# Import Packages
from Core.Web import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#Functions
def about():
    QMessageBox.about(
        Window,
        'About',
        'Nexo Version 0.0.1_a'+
        '\nDeveloped by'+
        ' NLTech Corp\n'+
        'Copyright (C)2023 '+
        'NLTech Corporation'
    )

def fopen():
    FD = QFileDialog()
    File_Name = FD.getOpenFileName(
    Window,
    'Open'
    )
    print(File_Name)

def Get_URL():
    '''
    Get Target URL and analyze 
    Protocol & Domain Type
    '''
    Web.url = e0.text()
    Web.GetUA(c0.currentIndex())
    Web.GetProtocol()
    sts = Web.GetHandler()
    if sts == True:
        return
    Web.GetIP()
    Web.server = Web.handler.getheader('server')
    print(Web.__dict__)
    #DisplayGeneralInfo()
    print(Web.handler.read().decode('utf-8'))

def DisplayGeneralInfo():
    ld0 = QLabel(
        Web.url,
        Window)
    ld0.show()

def Get_Proxy_IP():
    global lei0,ci0
    ipproxy = lei0.text()
    protocol = ci0.currentText()
    Web.proxy = {protocol:ipproxy}
    # print(ipproxy)
    if ipproxy == '':
        Web.proxy = None
        l2_0.setText('Null')
        i.destroy(1,1)
        return
    # print(Web.proxy)
    l2_0.setText(ipproxy)
    Web.SetProxy()
    i.destroy(1,1)

def SetupProxy():
    global lei0,ci0,i
    i = QDialog(Window)
    i.setWindowTitle(
        'Setup Proxy'
        )
    i.setObjectName('i')
    i.setStyleSheet(
    '''
        #i{
    background-color:
        #585858;
    font-family:
        Times New Roman;
        }
    '''
    )
    li0 = QLabel(
    'Plaese Enter'+
    " Your Proxy's"+
    ' IP Address',i)
    li0.resize(220,20)
    li0.move(40,5)
    li0.setAlignment(Qt.AlignCenter)
    li0.setObjectName('li0')
    li0.setStyleSheet('''
        #li0{
    background-color:
        #CADBE8;
    border-radius:
        5px;
    color:
        #FF2E80;
    font-family:
        Times New Roman;
    font-weight:
        800;
        }
    ''')
    li1 = QLabel('Proxy Type:',i)
    li1.resize(70,20)
    li1.move(50,30)
    ci0 = QComboBox(i)
    ci0.resize(60,20)
    ci0.move(120,30)
    ci0.setWhatsThis('Proxy Type')
    ci0.addItems([
        'Http',
        'Https',
        'Socks4',
        'Socks5'
    ])
    lei0 = QLineEdit(i)
    lei0.resize(100,20)
    lei0.move(100,50)
    bi0 = QPushButton('Setup',i)
    bi0.setObjectName('bi0')
    bi0.setStyleSheet('''
        #bi0{
    background-color:
        #CADBE8;
    border-top-right-radius:
        5px;
    border-bottom-right-radius:
        5px;
    font-family:
        Times New Roman;
        }
    ''')
    bi0.clicked.connect(Get_Proxy_IP)
    bi0.resize(40,20)
    bi0.move(200,50)
    i.setGeometry(
    Root.desktop().width()/2-130,
    Root.desktop().height()/2-75,
    300,150)
    i.setFixedSize(300,150)
    i.show()

#Web Core Event Initialize
Web = Net_Obj()

#Create a Qt Window
#Root Object
Root = QApplication()
#Gui Window
Window = QMainWindow()
Window.setToolTip('Nexo')
Window.setGeometry(
    Root.desktop().width()/2-400,
    Root.desktop().height()/2-300,
    800,
    600
)
Window.setWindowIcon(QIcon('.\Icon.png'))
Window.setMinimumSize(800,600)
Window.setWindowTitle('Nexo')
Window.setToolTipDuration(1000)


#Widgets
#Labels
l0 = QLabel(
    'Nexo--The Internet Crawler',
    Window
)
l0.setObjectName('l0')
l0.setStyleSheet('''
    #l0{
background-color:
    #070925;
border-top-right-radius:
    15px;
color:
    #E2CAEF;
font-family:
    Times New Roman;
font-size:
    20px;
font-style:
    italic;
font-weight:
    800;
    }
''')
l0.setAlignment(Qt.AlignCenter)
l0.setToolTip('This is Nexo')
l0.resize(260,30)
l0.move(0,25)
# l1
l1 = QLabel(
    '''User-Agent:''',
    Window)
l1.setObjectName('l1')
l1.setStyleSheet('''
    #l1{
background-color:
    #070925;
color:
    #E2CAEF;
font-family:
    Times New Roman;
font-weight:
    800;
    }
''')
l1.setAlignment(Qt.AlignCenter)
l1.setToolTip(
'Select Your Own User-Agent'
    )
l1.resize(80,20)
l1.move(0,75)
# l2
l2 = QLabel('IP Proxy:',Window)
l2.setObjectName('l2')
l2.setStyleSheet('''
    #l2{
background-color:
    #3C325F;
color:
    #E2CAEF;
font-family:
    Times New Roman;
font-weight:
    800;
    }
''')
l2.setAlignment(Qt.AlignCenter)
l2.resize(80,20)
l2.move(0,95)
l2_0 = QLabel('Null',Window)
l2_0.setObjectName('l2_0')
l2_0.setStyleSheet('''
    #l2_0{
background-color:
    #6973AC;
color:
    #E2CAEF;
font-family:
    Times New Roman;
font-weight:
    800;
    }
''')
l2_0.setAlignment(Qt.AlignCenter)
l2_0.resize(180,20)
l2_0.move(80,95)

#Line Edit
e0 = QLineEdit(Window)
e0.setObjectName('e0')
e0.setStyleSheet('''
    #e0{
background-color:
    #CECAEF;
border:
    1px solid;
border-color:
    #1AA1D6;
color:
    #FFFFFF;
}
    #e0:focus{
border-color:
    #5D6FD5;
color:
    #CE2CCC;
font-family:
    Times New Roman;
font-weight:
    800;
}''')
e0.setToolTip(
'Input Target URL'
)
e0.resize(220,20)
e0.move(0,55)

#Button
b0 = QPushButton(
    'Go',
    Window)
b0.setToolTip('Confirm')
b0.resize(40,20)
b0.move(220,55)
b0.clicked.connect(Get_URL)

#Combobox
c0 = QComboBox(Window)
c0.setObjectName('c0')
c0.setStyleSheet('''
    #c0{
background-color:
    #7922BC;
color:
    #DDDDDF;
font-family:
    Times New Roman;
font-weight:
    800;
    }
''')
c0.setToolTip('Selection')
c0.addItems(
    ['Firefox -- Windows 10(x64)',
    'Firefox -- Windows 10(x86)',
    'Firefox -- Windows 8.1(x64)',
    'Firefox -- Windows 8.1(x86)',
    'Firefox -- Windows 8(x64)',
    'Firefox -- Windows 8(x86)',
    'Firefox -- Windows 7(x64)',
    'Firefox -- Windows 7(x86)',
    'Firefox -- Windows Vista(x64)',
    'Firefox -- Windows Vista(x86)',
    'Firefox -- Windows XP(x64)',
    'Firefox -- Windows XP(x86)',
    'Firefox -- Windows 2000',
    'Firefox -- Windows ME',
    'Firefox -- Windows 98',
    'Firefox -- Windows 95',
    'Firefox -- Mac OS X',
    'Firefox -- Ubuntu',
    'Firefox -- Open BSD',
    'Firefox -- Arch Linux',
    'Firefox -- iPhone',
    'Firefox -- iPad',
    'Firefox -- iPod',
    'Firefox -- Android (40+)',
    'Firefox -- Android (40-)'
    ])
c0.resize(180,20)
c0.move(80,75)

#Menu
menu = Window.menuBar()
filemenu = menu.addMenu('&File')
proxymenu = menu.addMenu('&Proxy')
pluginmenu = menu.addMenu('P&lugin')
aboutmenu = menu.addMenu('&About')

#Sub Menu of File Menu
fAct0 = QAction('&Open')
fAct0.setShortcut('Ctrl+O')
fAct1 = QAction('E&xit\tCtrl+x')
fAct1.setShortcut('Ctrl+X')
filemenu.addAction(fAct0)
filemenu.addSeparator()
filemenu.addAction(fAct1)
fAct0.triggered.connect(fopen)
fAct1.triggered.connect(exit)

#Sub Menu of Proxy Menu
qAct0 = QAction('&Setup')
qAct1 = QAction('&Test')
proxymenu.addAction(qAct0)
proxymenu.addAction(qAct1)
qAct0.triggered.connect(SetupProxy)
#qAct1.triggered.connect(TestProxy)

#Sub Menu of About Menu
aAct0 = QAction('&About Nexo')
aAct1 = QAction('About &Qt')
aboutmenu.addAction(aAct0)
aboutmenu.addAction(aAct1)
aAct0.triggered.connect(about)
aAct1.triggered.connect(Root.aboutQt)

Window.show()

Root.exec_()