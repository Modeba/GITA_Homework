students = {
    "student1": {"name": "ანა", "age": 20, "grade": 9},
    "student2": {"name": "ნიკო", "age": 22, "grade": 8},
    "student3": {"name": "მარიამ", "age": 21, "grade": 10}
}

highest_grade = [None, 0]

# ბეჭდავს თითოეული სტუდენტის სახელი და ქულა
for student in students:
    name  = students[student]["name"]
    grade = students[student]["grade"]
    # ამოწმებს თუ კონკრეტულ სტუდენტს ყველაზე მაღალი ქულა აქვს და ინახავს ცვლადში
    if grade > highest_grade[1]:
        highest_grade[0] = name
        highest_grade[1] = grade
    print(name, grade)

# ბეჭდავს ყველაზე მაღალი ქულის მქონე სტუდენტს და მის ქულას
print(highest_grade)

# ლექსიკონში ამატებს მეოთხე სტუდენტს
students["student4"] = {"name": "სოფო", "age": 23, "grade": 9}