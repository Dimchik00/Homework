numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
numbers.remove(1)
k = 0
for i in numbers:
    is_prime = True
    for f in range(2, i // 2 + 1):
        if i % f == 0:
            k = k + 1
    if (k <= 0 ) :
        is_prime = True
        is_prime = primes.append(i)
    else:
        is_prime = False
        is_prime = not_primes.append(i)
        k = 0
print(primes)
print(not_primes)
