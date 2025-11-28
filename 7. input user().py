# 7. input user()

# data yang di masukan pasti string(str)
data = input("masukan data: ")

print("data = ",data,"type =",type(data))

#jika kita ingin mengambil data integer(int),maka
angka = float(input("masukan angka: "))# terserah mau pakai apa aja
angka = int(input("masukan angka: "))# terserah mau pakai apa aja
print("data = ",angka,"type =",type(angka))


#bagaimana dengan boolean
# biner adalah sistem hitungan cuma 2 angka 0 dan 1
# 1= on/hidup/true/ selain 0 tetap true
# 0= off/mati/false 
biner = bool(int(input("masukan nilai boolean: ")))# terserah mau pakai apa aja
# harus di casting ke integer biar bisa baca angka
print("data = ",biner,"type =",type(biner))
