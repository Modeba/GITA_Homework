my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
temp = list(my_list[0])
temp[-1] = 30
my_list[0] = tuple(temp)

print(my_list)