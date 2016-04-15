x = 1
y = 1
fib = 0
total = 0
count = 0

while fib < 4000000:
    fib = x + y

    if fib % 2 == 0:
        total += fib

    if count % 2 == 0:
        x += y
    else:
        y += x
    count += 1

print(total)
