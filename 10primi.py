def count_primes(n):
    primes = []
    num = 2

    while len(primes) < n:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1

    return primes

print(count_primes(10))