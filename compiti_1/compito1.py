nome = input("come ti chiami?\n ")
print(f"ciao {nome}!")

lista_vocali = ["a","e","i","o","u"]

num_vocali2 = 0
for lettera in lista_vocali:
    if lettera in nome:
        num_vocali2 = num_vocali2 + 1
        print("\"",lettera,"\" compare in ", nome, num_vocali2)     
