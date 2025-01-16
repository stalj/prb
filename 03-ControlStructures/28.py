def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Input number of prime numbers to find
N = int(input("Enter the number of leading prime numbers to find: "))
primes = find_primes(N)
print("Prime numbers:", ' '.join(map(str, primes)))
