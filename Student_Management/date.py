class date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    def show(self):
        f1='\x1b[6;37;41m'
        f2='\x1b[6;30;42m'
        last='\033[0m'#mauden
        print(f2+"Ngay sinh:",self.day,self.month,self.year,last+"\n")