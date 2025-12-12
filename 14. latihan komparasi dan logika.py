#14. latihan komparasi dan logika

# membuat gabungan area rentang dari angka
#+++++3-----10+++++

inputuser = float(input("masukan angka yang brnilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

#+++++3-------
# memeriksa angka kurang dari 3
# "is "biar true atau false
iskurangdari =(inputuser < 3)
print("kurang dari 3 =", iskurangdari)

#---------10++++++
#memeriksa angka lebih dari 10
islebihdari = (inputuser > 10)
print( "lebihdari 10 =", islebihdari)

#++++++3------10+++++
#"isCorrect" untuk tau bener atau enggak nya
# gabungkan dengan "or"
isCorrect = iskurangdari or islebihdari
print("angka yang anda masukan: ", isCorrect)



#------3++++++10------
# kasus irisan/tengah tengah
# atau di ganti jadi dan
print("\n",10*"=","\n")
inputuser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

#-----3+++++++
# lebih dari 3
islebihdari = inputuser > 3
print("lebih dari 3 =", islebihdari)

#++++++++++10-------
# kurang dari 10
iskurangdari = inputuser < 10
print("kurang dari 10 =", iskurangdari)


#------3++++++10------
isCorrect = iskurangdari and islebihdari
print("angka yang anda masukan: ", isCorrect)
