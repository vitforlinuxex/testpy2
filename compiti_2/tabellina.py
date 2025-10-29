num_pari = 0
i = 1
print("\nTabellina usando il ciclo while e for: \n")
while i < 11:
    for x in range(1,11):
        num_pari = i * x
        print(num_pari," ", end="")
    print("")
    i += 1