groups = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
res = []
for group in groups:
    res.append(sum(group) / len(group))

print(res)