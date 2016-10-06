# Sum of all the multiples of 3 and 5 bellow 1000

def sum_of_multiples(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(sum_of_multiples(1000))
# 233168
