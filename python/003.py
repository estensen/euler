# Largest prime factor of the number 600851475143

def largest_prime_factors(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n /= i
        i += 1
    return n

print(largest_prime_factors(600851475143))
# 6857
