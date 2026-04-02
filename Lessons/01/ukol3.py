names = ["Alice", "Bob", "Charlie", "David", "Eve"]
pairs = []

# create pairs of names
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        pairs.append(names[i] + " - " + names[j])

print(pairs)