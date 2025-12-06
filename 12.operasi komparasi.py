# operasi komparasi(untuk membandingkan nilai)

#setiap hasil dari hasil komparasi adalah boolean
# (=) itu asigment, (==) itu membandingkan

# >, <, >=, <=, == ,!=, is, is not

a = 4
b = 2


#1. lebih bear dari (>)
print('==== lebih besaar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)

hasil = b > 3
print(b,'>',3,'=',hasil)

hasil = b > 2
print(b,'>',2,'=',hasil)

#2. kurang dari (<)
print('==== kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)

hasil = b < 3
print(b,'<',3,'=',hasil)

hasil = b < 2
print(b,'<',2,'=',hasil)

#4. lebih dari samadengan(>=)
print('==== lebih dari samadengan(>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)

hasil = b >= 3
print(b,'>=',3,'=',hasil)

hasil = b >= 2
print(b,'>=',2,'=',hasil)

#5. kurang dari sama dengan(<=)
print('==== kurang dari samadengan(<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)

hasil = b <= 3
print(b,'<=',3,'=',hasil)

hasil = b <= 2
print(b,'<=',2,'=',hasil)
hasil = a <= 3
print(a,'<=',3,'=',hasil)

hasil = b <= 3
print(b,'<=',3,'=',hasil)

#6. samadengan(==)
# (=) itu asigment, (==) itu membandingkan
# literal dengan objek
print('====  samadengan(==)')
hasil = a == 4
print(a,'==',4,'=',hasil)

hasil = b == 4
print(b,'==',4,'=',hasil)
hasil = a == 4
print(a,'==',4,'=',hasil)

#7. tidak samadengan(!==)
print('==== tidak samadengan(!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)

hasil = b != 4
print(b,'!=',4,'=',hasil)

#"8.(is) sebagai komparasi objek identity"
# (is) adalah membandingkan objek/memori (a/ huruf) itu memori
# (4/angka) itu literal tidak disimpan di memori
print('==== object identity(is)')
x = 5 # ini adalah assigment membuat object
y = 5
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai y =,',y,'id = ',hex(id(x)))
hasil = x is y
print('x,is,y =',hasil)
# contoh 2
x = 5 # ini adalah assigment membuat object
y = 6
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai y =,',y,'id = ',hex(id(x)))
hasil = x is y
print('x,is,y =',hasil)

# 9. (is not) adalah yang tidak samadengan
print('==== object identity(is not)')
x = 5 # ini adalah assigment membuat object
y = 5
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai y =,',y,'id = ',hex(id(x)))
hasil = x is not y
print('x,is not,y =',hasil)
# contoh 2
x = 5 # ini adalah assigment membuat object
y = 6
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai y =,',y,'id = ',hex(id(x)))
hasil = x is not y
print('x,is not,y =',hasil)
