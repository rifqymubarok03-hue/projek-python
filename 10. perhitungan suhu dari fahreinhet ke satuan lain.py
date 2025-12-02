# perhitungan suhu level 2

print("\nprogram konversi temperatur\n")

# fahreinheit ke satuan lain
fahreinheit = float (input("masukan suhu dalam fahreinheit: " ))
print("suhu adalah",fahreinheit,"fahreinheit")
 
# celcius rumus = (5/9 * (fahreinheit-32))
celcius = (5/9 * (fahreinheit-32))
print("suhu adalah",celcius,"celcius")

# reamur rumus = 4/9(f-32)
reamur = (4/9 * (fahreinheit-32))
print("suhu adalah",reamur,"reamur")

# kelfin rumus = (hasil celcius + 273.15)
kelvin = (celcius + 273.15) 
print("suhu adalah",kelvin,"kelvin")
