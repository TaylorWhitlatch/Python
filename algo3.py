n = 13195
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print (n)

known_primes = [2,3]
def is_prime(n):
    total_primes = len(known_primes)
    for i in range(0,total_primes):
        if (n % known_primes[i]==0):
            return False
        else:
            # it might be prome, it might not.
            # Its just not divisible by this number
            continue

    known_primes.append(n)
    return True
print known_primes
print is_prime(13195)
