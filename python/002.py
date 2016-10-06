# Find the sum of even-valued Fibonacci terms under 4M

def fib(n):
    sum = 0
    a = 0
    b = 1
    while b < n:
        a, b = b, a + b
        if a % 2 == 0:
            sum += a
    return sum

print(fib(4000000))
# 4613732
