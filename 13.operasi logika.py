# operasi logika atau boolean

# not, or, and, xor(^)

#1.not
# not artinya tidak/ kebalikan( ke balikan dari true adalah false)
print('===not===')
a = True
c = not a
print('data a =',a)

print('===not===')
print('data c =',c)

#2. or
# kalau ada true hasil nya true
print('===or===')
a = False
b = False
c = a or b
print(a,'or',b,'=',c)

print('===or===')
a = False
b = True
c = a or b
print(a,'or',b,'=',c)

print('===or===')
a = True
b = False
c = a or b
print(a,'or',b,'=',c)

print('===or===')
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

# 3. and
# kalau ada false maka hasil nya false
# kalau ke duanya true baru hasil nya true
print('===and===')
a = False
b = False
c = a or b
print(a,'and',b,'=',c)

print('===and===')
a = False
b = True
c = a and b
print(a,'and',b,'=',c)

print('===and===')
a = True
b = False
c = a and b
print(a,'and',b,'=',c)

print('===and===')
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

# 4. xor(^)
# kalau ada dua nilai true dan fals maka hasil nya true
# kalau ke dua nilai itu true maka hasil nya akan false
# kalau kedua nilai false maka hasil nya false
print('===xor===')
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)

print('===xor===')
a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)

print('===xor===')
a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)

print('===xor===')
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)
