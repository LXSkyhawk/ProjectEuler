x = 3
count = 2
while count < 10001:
    x += 2
    prime = True
    for y in range(2, int(x**(0.5))+1):
        if x % y == 0:
            prime = False
            break
    if prime:
        count += 1
print(x)
