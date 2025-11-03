lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open('new_file.txt','w') as f:
    for element in lst:
        f.write(element + '\n')