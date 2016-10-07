# Difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum

sum_squares = 0
squares_sum = 0
for i in range(101):
    sum_squares += i**2
    squares_sum += i
squares_sum **= 2

print(abs(sum_squares - squares_sum))
# 25164150
