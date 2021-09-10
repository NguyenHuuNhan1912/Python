class dshp:
    def __init__(self,danhsachhocphan):
        self.danhsachhocphan=danhsachhocphan
    def show(self):
        f1='\x1b[6;37;41m'
        f2='\x1b[6;30;42m'
        last='\033[0m'#mauden
        k=len(self.danhsachhocphan)
        for i in range(k):
            print(f1+"Thong tin hoc phan thu",(i+1),last+"\n")
            print(f2,self.danhsachhocphan[i],last+"\n")   

    def doidiem(self,s):
        if s=="A" or s=="a":
            return 4.0
        elif s=="B+" or s=="b+":
            return 3.5
        elif s=="B" or s=="b":
            return 3.0      
        elif s=="C+" or s=="c+":
            return 2.5
        elif s=="C" or s=="c":
            return 2.0
        elif s=="D+" or s=="d+":
            return 1.5
        elif s=="D" or s=="d":
            return 1.0
        elif s=="F" or s=="f":
            return 0.0

    def tichluy(self):
       k = len(self.danhsachhocphan)
       total=0.0
       count=0
       for i in range(k):
           count+=self.danhsachhocphan[i][1]
           s = self.danhsachhocphan[i][2]
           total += ( self.danhsachhocphan[i][1] * self.doidiem(s))
       return total/count
