# pelajaran 6. casting tipe data
# casting merubah data dari satu tipe
# ke tipe data yang lain
# tipe data:int,float,str,bool

## integer

print("====integer====")
data_int = 9;
print("data =", data_int, ",type =",type(data_int))
# operator cesting, merubah data di atas
# rubah dari data di atas jadi float,str,bool
data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)#akan false jika data integer 0
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

## float
print("====float====")
data_float = 9;
print("data =", data_float, ",type =",type(data_float))
# operator cesting, merubah data di atas
# rubah dari data float jadi int,str,bool
data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)#akan false jika data integer 0
print("data =", data_int, ",type =",type(data_int))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))


# boolean
print("=== boolean ====")
# dari data boolean ke integer,str,float
data_bool = 9.9;

print("data =", data_bool, ",type =",type(data_bool))

data_int    = int(data_bool)# akan di bulatkan ke bawah
data_str    = str(data_bool)
data_float  = float(data_bool)#akan false jika data integer 0
print("data =", data_int, ",type =",type(data_int))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_float, ",type =",type(data_float))


# str
print("=== string ====")
# dari data str ke integer,boolean,,float
data_str = "10";

print("data =", data_str, ",type =",type(data_str))

data_int    = int(data_str)# str harus angka
data_bool   = bool(data_str)# penjelasan di bawah
data_float  = float(data_str)# str harus angka
# bool akan false jika str kosomg(tidak di isi)
# string ke bool= niali akan tetap falt
# kecuali str di atas tidak di isi di baris 52
# str karakter(tulisan/nama) tidak bisa di rubah ke 
# ke bool hanya bisa(false,true,dan angka)
print("data =", data_int, ",type =",type(data_int))
print("data =", data_bool, ",type =",type(data_bool))
print("data =", data_float, ",type =",type(data_float))
