count = 0
with open('new_file.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        # Tu ASCII aris 65 - 90 shoris an martivad .isupper()
        if 65 <= ord(line[0]) <= 90:
            count += 1

print(count)