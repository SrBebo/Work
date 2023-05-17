students = {# we create a dictionary of students
    "Juan":{
        "note1":8.2,
        "note2":9.1,
        "note3":7.5
    },
    "Pedro":{
        "note1":9.2,
        "note2":6.1,
        "note3":8.5
    },
    "Maria":{
        "note1":7.2,
        "note2":8.1,
        "note3":9.5
    },
}

def get_average_notes_student(student: str) -> float:#function to get the average of notes of each student
    return round((students[student]["note1"] + students[student]["note2"] + students[student]["note3"])/3, 3)#return the average of notes of student

def get_average_note_class(student: str) -> float:#function to get the average of notes of class
    average = 0
    for student in students:
        average += get_average_notes_student(student)
    return round(average/len(students),3)

print("The average of each student is:\n")
for student in students:
    print(f"{student}: {get_average_notes_student(student)}")

print("\nThe average of class is:\n"+str(get_average_note_class(student)))
