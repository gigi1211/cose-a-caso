import random
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
numero = int(input('da quanti caratteri vuoi che sia la password?'))
password = ''
for i in range(numero):
    password+=(random.choice(caratteri))
print(password)






