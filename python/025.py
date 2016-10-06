# Index of first term in the Fibonacci sequence to contain 1000 digits

a = 1
b = 1
i = 1
while len(str(a)) < 1000:
    a, b = b, a + b
    i += 1
print(i)
# 4782
