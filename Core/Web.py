'''
    Core of Net Module
'''

from urllib.error import *
from urllib.parse import *
from urllib.request import *
from urllib.response import *
from urllib.robotparser import *


class Net_Obj():
    '''
    Create a Net Model Object
    '''
    def __init__(self) -> None:
        super().__init__()
        self.ip = None
        self.url = None
        self.port = None
        self.proxy = None
        self.opener = None
        self.server = None
        self.handler = None
        self.request = None
        self.protocol = None
        self.UserAgent = None

    def GetProtocol(self):
        for i in range(0,len(self.url)):
            if self.url[i:i+3] == '://':
                self.protocol=self.url[0:i]
                return
    
    def GetHandler(self):
        self.request = Request(
        self.url,
        headers={'User-Agent':self.UserAgent})
        try:
            self.handler = urlopen(
                self.request,
                timeout=5.0
                )
        except Exception as e:
            print(e)
            return 1
    
    def GetIP(self):
        ip = self.handler.fp.raw._sock.getpeername()
        self.ip = ip[0]
        self.port = ip[1]

    def GetUA(self,Choice):
        try:
            UAPool = open(r'.\\Data\\UAPools.txt',encoding='utf-8')
        except:
            print('File Missing:UAPools.txt')
        for i in range(0,Choice+1):
            self.UserAgent = UAPool.readline().rstrip('\n')

    def SetProxy(self):
        # build_opener()
        proxy_handler = ProxyHandler(self.proxy)
        self.opener = build_opener(proxy_handler)
        install_opener(self.opener)