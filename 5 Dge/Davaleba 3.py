matrix = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y']
]

for i in range(len(matrix)):
    # საჭიროა შიდა ლუპის i ინდექსიდან დაწყება, რათა ელემენტები რომლებმაც უკვე შეიცვალეს პოზიცია, უკან არ დაბრუნდნენ.
    for j in range(i, len(matrix[i])):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

for row in matrix:
    print(row)