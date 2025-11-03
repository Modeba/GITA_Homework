user_input = 0
total_sum  = 0

while user_input != "sum":
    if int(user_input) > 0:
        total_sum += int(user_input)
    user_input = input()

print(total_sum)