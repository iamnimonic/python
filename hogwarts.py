students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jac Russel"},
        {"name": "Draco", "house": "Slytherin", "patronus": "Otter"},
]

def main():
    # print(students[0]["house"])
    for student in students:
        print(student["name"])

main()