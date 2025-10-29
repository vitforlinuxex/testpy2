height=2*int(input("altezza triangolo\n"))
for i in range(0,height,2):
    print(' ' * (height - int(i/2) - 1) + '*' * (i + 1))