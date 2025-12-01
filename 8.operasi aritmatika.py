# 1. operasi aritmatika
# urutan yang di kerjain duluan= (),exponen,prioritas,perkalian dan teman teman,pertambahan perkurangan

a = 10
b = 3

# operasi tambah +
hasail = a + b
print(a,'+',b,'=',hasail)


# operasi pengurangan -
hasail = a - b
print(a,'-',b,'=',hasail)


# operasi perkalian *
hasail = a * b
print(a,'*',b,'=',hasail)

# operasi pembagian /
hasail = a / b
print(a,'/',b,'=',hasail)

# operasi exponen(pangkat) **
hasail = a ** b
print(a,'**',b,'=',hasail)

# operasi modulus (sisa pembagian) %
hasail = a % b
print(a,'%',b,'=',hasail)

# operasi floor division (bagi tapi kayak dobel) // 
hasail = a // b #(hasil pembagian yang di bulat kan)
print(a,'//',b,'=',hasail)

# 2. prioritas operasi, operational precedence
'''
   1. ()
   2. exponen **
   3. perkalian dan teman teman * / ** % // 
   4. pertambahan dan pengurangan

'''

x = 3
y = 2
z = 4

hasail = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasail)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y ) * z
print('(',x,'+',y,')*',z,'=',hasil)
