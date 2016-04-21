import sys

for x in range(334, 1000):
    for y in range(2, x):
        for z in range(1, y):
            if x + y + z == 1000:
                if z**2 + y**2 == x**2:
                    print(x*y*z)
                    sys.exit()
