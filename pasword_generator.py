import random
elements = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
longitud = int(input('introduce la longitud de tu contraseña'))
password = ''

for i in range(longitud):
    password += random.choice(elements)
    print(i)
print(password)