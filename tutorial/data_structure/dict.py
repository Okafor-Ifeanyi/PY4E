counts = dict()
names = ['victor', 'ifeanyi', 'izu', 'kosi', 'izu', 'izu', 'victor', 'kosi', 'kosi', 'victor', 'izu']

for name in names:
    # if name not in counts:
    #     counts[name] = 1
    # else:
    #     counts[name] += 1

    # This line replaces the commented code above
    counts[name] = counts.get(name, 0) + 1

print(counts)