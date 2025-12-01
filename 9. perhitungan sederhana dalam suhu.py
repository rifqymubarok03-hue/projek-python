# 9. perhitungan sederhana
# latihan konversi satuan temperatur

# program konversi celsius ke satuan lain

print("\nprogram konversi temperatur\n")
#celcius
celcius = float(input("masukan suhu dalam celcius : "))
print("suhu adalah",celcius, "celcius")

#reamur
# rumus (4/5)c
reamur= (4/5) * celcius
print("suhu dalam reamur adalah ",reamur,"reamur")

#fahreinhet
# rumus 9/5 * celcius + 32
fahreinhet = ((9/5) * celcius) + 32
print("suhu dalam fahreinhet adalah ",fahreinhet,"fahreinhet")

#kelvin
#kelvin = celcius +273
kelvin = celcius +273
print("suhu dalam kelvin adalah ",kelvin,"kelvin")

