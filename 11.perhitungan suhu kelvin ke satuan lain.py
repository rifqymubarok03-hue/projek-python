# perhitungan suhu kelvin ke satuan lain


print("\nprogram konversi temperatur\n")

# kelvin ke satuan lain
kelvin = float (input("masukan suhu dalam kelvin: " ))
print("suhu adalah",kelvin,"kelvin")
 
# celcius rumus = (k - 273.15)
celcius = (kelvin - 273.15)
print("suhu adalah",celcius,"celcius")

# reamur rumus = (4/5 * (kelvin - 273))
reamur = (4/5 * (kelvin - 273.15))
print("suhu adalah",reamur,"reamur")

# kelfin rumus = ((kelvin - 273.5) * 9/5 + 32)
fahreinhet = ((kelvin - 273.15) * 9/5 + 32) 
print("suhu adalah",fahreinhet,"kelvin")
