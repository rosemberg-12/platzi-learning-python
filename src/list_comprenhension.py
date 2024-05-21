pairs_one = []

for i in range(0, 10):
    pairs_one.append(i * 2)

print(pairs_one)

pairs_two = [i * 2 for i in range(0, 10)]
print(pairs_two)


pairs_one = []

for i in range(0, 10):
    if i % 2 == 0:
        pairs_one.append(i * 2)

print(pairs_one)

pairs_two = [i * 2 for i in range(0, 10) if i % 2 == 0]
print(pairs_two)
