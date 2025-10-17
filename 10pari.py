print("Questo programma stampa i primi 10 numeeri pari")

print(range (0,10))

primi = range(2,10)

print(primi[4])

testo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullamco laboriosam, nisi ut aliquid ex ea commodi consequatur. Duis aute irure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

a = 0

for lettera in testo:
    if lettera == ",":
        a = a + 1
        
print(a)

b=0

parola = "supercalifragilistichespiralidoso"

for lettera in parola:
    if lettera in "aeiou":
        b = b + 1
        
print(b)

lista_vocali = ["a","e","i","o","u"]

c = 0

for lettera in lista_vocali:
    if lettera in parola:
        print("\"" ,lettera,"\" compare ")
#        c = c + 1
#print(c)
