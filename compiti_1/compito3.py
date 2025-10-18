def count_cons(word):
#    vowels = 'aeiou'
    cons = 'bcdfghlmnpqrstvxz'
    return sum(1 for char in word.lower() if char in cons)

def count_vowels(word):
    vowels = 'aeiouyjè'
#    cons = 'bcdfghlmnpqrstuvxz'
    return sum(1 for char in word.lower() if char in vowels)

def count_num(word):
    nums = '0123456789'
    return sum(1 for char in word.lower() if char in nums)

# Esempio
nome = input("come ti chiami?\n ")
conta_vocali = count_vowels(nome)
conta_consonanti = count_cons(nome)
conta_numeri = count_num(nome)
print(f"Il nome '{nome}' contiene {conta_vocali} vocali, {conta_consonanti} consonanti e {conta_numeri} numeri .")
