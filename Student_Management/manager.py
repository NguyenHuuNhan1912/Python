from student import student
from date import date
from dshp import dshp
import os
def read_Information(ds):
    listHP_1SV = []
    name=input("Nhap ten: ")
    mssv=input("Nhap mssv: ")
    major=input("Nhap chuyen nganh: ")
    print("Nhap ngay thang nam sinh")
    day=int(input("Nhap ngay: "))
    month=int(input("Nhap thang: "))
    year=int(input("Nhap nam: "))
    ngaysinh = date(day,month,year)
    soluong=int(input("Nhap so luong hoc phan: "))
    for i in range(soluong):
        tenhp=input("Nhap ten hoc phan thu "+str(i+1)+": ")
        stc=int(input("Nhap so tin chi hoc phan thu "+str(i+1)+": "))
        diemhp=input("Nhap diem chu cua hoc phan thu "+str(i+1)+": ")
        monhoc = [tenhp,stc,diemhp]
        listHP_1SV.append(monhoc)
    danhsachhocphan = dshp(listHP_1SV)
    sv = student(name,mssv,major,ngaysinh,danhsachhocphan)
    ds.append(sv)

    

#khai bao mang
ds = []
n = int(input("Danh sach ban co bao nhieu sinh vien: "))
for i in range(n):
     print("Nhap thong tin sinh vien thu "+str(i+1))
     read_Information(ds)
os.system("cls")
f1='\x1b[6;37;41m'
f2='\x1b[6;30;42m'
last='\033[0m'#mauden

for i in range(n):
    print(f1+"Thong tin sinh vien thu "+str(i+1)+last+"\n")
    ds[i].show()

print(f1+"Danh sach diem tich luy cua toan bo sinh vien\n"+last)
for i in range(n):
    print(f2+"Diem trung binh tich luy cua sinh vien " + ds[i].getname() + " la:",ds[i].tichluy(),last+"\n")