import random
a=0
a = random.randint(1, 9)
print (a)

b = int(input("dimmi quale numero ho pensato"))

if a == b:
    print("bravo")
else:
    print("sbagliato il numero era",a)