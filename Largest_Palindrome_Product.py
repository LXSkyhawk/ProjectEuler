products = []

for x in range(1, 1000):
    for y in range(x, 1000):
        product = str(x * y)

        if product == product[::-1]:
            products.append(int(product))

print(max(products))
