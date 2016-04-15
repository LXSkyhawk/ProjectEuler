num = 600851475143
factors = []

x = 2
while num >= x:
    if num % x == 0:
        factors.append(x)

        while num % x == 0:
            print(num)
            num /= x
    x += 1

print(factors)
