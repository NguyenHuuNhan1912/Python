n = int(input("Nhap so can tinh giai thua: "))

#Ham de qui tinh giai thua
def GiaiThua(n):
    if n == 0:
        return 1
    return n * GiaiThua(n - 1)

print(str(n) + "! =",str(GiaiThua(n)))
