x = 30

while True:
    divisible = True
    for y in range(3, 21):
        if x % y != 0:
            divisible = False
            break

    if divisible:
        print(x)
        break

    x += 10
