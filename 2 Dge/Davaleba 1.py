grade = int(input())

if grade < 51:
    print("Fail")
elif grade < 61:
    print("E")
elif grade < 71:
    print("D")
elif grade < 81:
    print("C")
elif grade < 91:
    print("B")
elif grade < 101:
    print("A")

# grade = int(input())
# grades = ["Fail", "Fail", "Fail", "Fail", "Fail", "E", "D", "C", "B", "A"]
# if grade > 100 or grade < 0: print("Error")
# else: print(grades[grade // 10])