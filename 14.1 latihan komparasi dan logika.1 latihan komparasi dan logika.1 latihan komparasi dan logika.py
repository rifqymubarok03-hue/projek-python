# 14.1 latihan komparasi dan logika

# 1). ---0+++++5----8+++++11------
inputuser = float(input("masukan angka yang brnilai\nlebih besar dari 0 \natau \nkurang dari 5\n" \
"\nlebih besar dari 8 \natau \nkurang dari 11\n:"))
print("==soal nomer 1==")
# ----0++++++
islebihbesardari =(inputuser > 0)
print("lebih dari 0 =", islebihbesardari)

# ++++5---
iskurangdari =(inputuser < 5)
print("kurang dari 5 =", iskurangdari)

# -----8+++++
islebihbesardari =(inputuser > 8)
print("lebih besar dari 8 =", islebihbesardari)

# +++++11-----
iskurangdari =(inputuser < 11)
print("kurang dari 11 =", iskurangdari)


# correct
isCorrect = iskurangdari or islebihbesardari
print("angka yang anda masukan: ", isCorrect)

# kasus irisan/ di tengah tengah
print("\n",10*"=","\n")

inputuser = float(input("masukan angka yang brnilai\nlebih besar dari 0 \ndan \nkurang dari 5\n" \
" \nlebih bear dari 5 \ndan \nkurang dari 8 " \
"\nlebih besar dari 8 \ndan \nkurang dari 11:"))
print("==kasus irisan==")
# 0+++++
islebihbesardari =(inputuser > 0)
print("lebih besar dari 0 =", islebihbesardari)

# +++++5
iskurangdari =(inputuser < 5)
print("kurang dari 5 =", iskurangdari)

# 5+++++
islebihbesardari =(inputuser > 5)
print("lebih besar dari 5 =", islebihbesardari)

# +++++8
iskurangdari =(inputuser < 8)
print("kurang dari 8 =", iskurangdari)

# 8++++++
islebihbesardari =(inputuser > 8)
print("lebih besare dari 8 =", islebihbesardari)

# +++++11
iskurangdari =(inputuser < 11)
print("kurang dari 11 =", iskurangdari)


isCorrect = iskurangdari and islebihbesardari
print("angka yang anda masukan: ", isCorrect)


# 2)+++++0-----5++++8-----11++++++


inputuser = float(input("masukan angka yang brnilai\nkurang dari 0 \natau \nlebih besar dari 5\n" \
"\nkurang dari 8 \natau \nlebih besar dari 11\n:"))
print("==soal nomer 2==")
# +++++0
iskurangdari =(inputuser < 0)
print("lebih dari 0 =", iskurangdari)

# -----5+++++
islebihbesardari =(inputuser > 5)
print("lebih besar dari 5 =", islebihbesardari)

# +++++8-----
iskurangdari =(inputuser < 8)
print("lebih besar dari 8 =", iskurangdari)

# +++++11-----
iskurangdari =(inputuser < 11)
print("kurang dari 11 =", iskurangdari)


# correct
isCorrect = iskurangdari or islebihbesardari
print("angka yang anda masukan: ", isCorrect)

# kasus irisan/ di tengah tengah
print("\n",10*"=","\n")

# +++++0-----5++++8-----11++++++)
# jadi ---0+++5+++8++++11----
inputuser = float(input("masukan angka yang brnilai\nlebih besar dari 0 \ndan \nkurang dari 5\n" \
" \nlebih bear dari 5 \ndan \nkurang dari 8 " \
"\nlebih besar dari 8 \ndan \nkurang dari 11:"))
print("==kasus irisan==")
# 0+++++
islebihbesardari =(inputuser > 0)
print("lebih besar dari 0 =", islebihbesardari)

# +++++5
iskurangdari =(inputuser < 5)
print("kurang dari 5 =", iskurangdari)

# 5+++++
islebihbesardari =(inputuser > 5)
print("lebih besar dari 5 =", islebihbesardari)

# +++++8
iskurangdari =(inputuser < 8)
print("kurang dari 8 =", iskurangdari)

# 8++++++
islebihbesardari =(inputuser > 8)
print("lebih besare dari 8 =", islebihbesardari)

# +++++11
iskurangdari =(inputuser < 11)
print("kurang dari 11 =", iskurangdari)


isCorrect = iskurangdari and islebihbesardari
print("angka yang anda masukan: ", isCorrect)
