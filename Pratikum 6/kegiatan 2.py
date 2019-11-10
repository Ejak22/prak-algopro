## Program Akun
## Dibuat oleh Daffa L200190204
import random
angka = random.randint(0,1000)

Nama = "Reza Pratama"
TanggalLahir = "22 Januari 2002"
NamaSingkat = Nama[0]+"."+Nama[9]+"."+Nama[2:8]
Username = Nama [0] + TanggalLahir[:2] + TanggalLahir [3:9]
Password = Nama[2:3] + str(angka)

print (Nama)
print (TanggalLahir)
print (NamaSingkat)
print (Username)
print (Password)
