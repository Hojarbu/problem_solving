
'''
Euler 6
The sum of the squares of the first ten natural numbers is,
12+22+...+102=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# Version 1
num = 0
for i in range(0, 101):
    num = num + i**2

print('sum of the squares: ', num)

total=0
for i in range(0, 101):
    total = total + i
result2 = total**2

print('square of the sum: ', result2)
print('difference: ', result2-num)


# version 2

a = sum(i for i in range(1, 101))**2
b = sum(i**2 for i in range(1, 101))
print('version2:', a-b)

# version3
print((sum(i for i in range(1, 101))**2)-(sum(i**2 for i in range(1, 101))))
