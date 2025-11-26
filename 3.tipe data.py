# a =10, a adalah variabel dengan nilai 10
# " ada 6 tipe data di python"

# 1.integer(int)
# 2.Float(float)
# 3.string(str)
# 4.boolean(bool)
# 5.complex(complex)
# 6.ctypes(di ambil dari bahasa c)

# 1.integer
# tipe data: angka satuan yang gak ada
# koma nya (integer) berapapun nilai nya
# dia tetap integer
data_integer = 11
print("data :", data_integer)
print("- bertipe : ", type(data_integer))

# 2. tipe data : dengan koma(float)
# 1,5 = Tuple (Kumpulan data: angka 1 dan angka 5)
#1.5 = Float (Bilangan desimal satu koma lima)
# tipe data: angka dengan koma(float)
data_float = 1.5
print("data :", data_float)
print("- bertipe : ", type(data_float))

# 3. tipe data: kumpulan karakter
#  adalah (string)
data_string = "erlina"
print("data :", data_string)
print("- bertipe : ", type(data_string))

# 4. boolean
#tipe data: biner true/false adalah (boolean)
# true = benar, false = salah, itu adalah boolean
# boolean adalah tipe data benar atau salah
# kalau 0 dia jadi false(salah) selain 0 akan true
data_bool = True
print("data :", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data khusus

# 5. bilangan complex
# 5(real), 6(imaginer)
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe : ", type(data_complex))

# 6. tipe data dari bahasa c

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe : ", type(data_c_double))

