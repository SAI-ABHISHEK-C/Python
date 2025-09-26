d = {"Alice":85,"Bob":35,"Mike":65}
s = input("Enter the name of the student: ")
if s.capitalize() in d:
    print(f"{s}'s marks:",d[s])
else:
    print("Student not found")