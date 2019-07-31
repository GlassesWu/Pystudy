def digui(x):
    if x == 1:
        return 1
    else:
        return x * digui(x-1)

print(digui(1))
print(digui(3))
