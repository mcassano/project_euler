n1 = 1
n2 = 2
sum = 2
while (n2 <= 4000000):
    temp = n2
    n2 = n2 + n1
    n1 = temp
    if n2 % 2 == 0:
        sum += n2

print sum
    
