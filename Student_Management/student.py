from date import date
from dshp import dshp

class student:
    def __init__(self,name,mssv,major,ngaysinh,dshp):
        self.name=name
        self.mssv=mssv
        self.major=major
        self.ngaysinh=ngaysinh
        self.dshp=dshp
        
    def show(self):
        f1='\x1b[6;37;41m'
        f2='\x1b[6;30;42m'
        last='\033[0m'#mauden
        print(f2+"Ten: "+self.name,last)
        print(f2+"MSSV: "+self.mssv,last)
        print(f2+"Chuyen nganh: "+self.major,last)
        self.ngaysinh.show()
        self.dshp.show()
        
    def getname(self):
        return self.name

    def tichluy(self):
        return self.dshp.tichluy()

