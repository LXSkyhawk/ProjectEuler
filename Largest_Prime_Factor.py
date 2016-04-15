num = 600851475143
factors = []

for x in range(2, num):
    if num % x == 0:
        factors.append(x)

        while num % x == 0:
            num /= x

print(factors)
