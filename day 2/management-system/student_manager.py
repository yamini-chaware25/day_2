import csv

FILE = "student_data.csv"

FIELDS = [
    "ID",
    "Name",
    "Department",
    "Age",
    "Marks"
]


def read_students():

    try:
        with open(FILE, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    except FileNotFoundError:
        print("student_data.csv not found.")
        return []


def save_students(students):

    with open(FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDS
        )

        writer.writeheader()
        writer.writerows(students)


def display_students(students):

    if not students:
        print("\nNo records found.")
        return

    print("\n" + "=" * 75)

    print(
        f"{'ID':<8}"
        f"{'Name':<15}"
        f"{'Department':<18}"
        f"{'Age':<8}"
        f"{'Marks':<10}"
    )

    print("=" * 75)

    for student in students:

        print(
            f"{student['ID']:<8}"
            f"{student['Name']:<15}"
            f"{student['Department']:<18}"
            f"{student['Age']:<8}"
            f"{student['Marks']:<10}"
        )

    print("=" * 75)


def add_student():

    students = read_students()

    student_id = input("Enter ID: ")

    for student in students:

        if student["ID"] == student_id:
            print("ID already exists.")
            return

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Department": department,
        "Age": age,
        "Marks": marks
    }

    students.append(student)

    save_students(students)

    print("Student added successfully.")


def update_student():

    students = read_students()

    student_id = input("Enter ID to update: ")

    for student in students:

        if student["ID"] == student_id:

            print("\nLeave blank to keep old value.")

            name = input(f"Name [{student['Name']}]: ")
            department = input(
                f"Department [{student['Department']}]: "
            )
            age = input(f"Age [{student['Age']}]: ")
            marks = input(f"Marks [{student['Marks']}]: ")

            if name:
                student["Name"] = name

            if department:
                student["Department"] = department

            if age:
                student["Age"] = age

            if marks:
                student["Marks"] = marks

            save_students(students)

            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():

    students = read_students()

    student_id = input("Enter ID to delete: ")

    new_students = [
        student
        for student in students
        if student["ID"] != student_id
    ]

    if len(new_students) == len(students):

        print("Student not found.")

    else:

        save_students(new_students)

        print("Student deleted successfully.")


def search_student():

    students = read_students()

    keyword = input("Enter ID or Name: ").lower()

    result = []

    for student in students:

        if (
            keyword in student["ID"].lower()
            or keyword in student["Name"].lower()
        ):
            result.append(student)

    display_students(result)


def filter_student():

    students = read_students()

    print("\n1. Department")
    print("2. Age")
    print("3. Marks greater than")

    choice = input("Enter choice: ")

    result = []

    if choice == "1":

        department = input("Enter Department: ").lower()

        result = [
            student
            for student in students
            if student["Department"].lower() == department
        ]

    elif choice == "2":

        age = input("Enter Age: ")

        result = [
            student
            for student in students
            if student["Age"] == age
        ]

    elif choice == "3":

        try:

            marks = float(
                input("Enter minimum marks: ")
            )

            result = [
                student
                for student in students
                if float(student["Marks"]) >= marks
            ]

        except ValueError:

            print("Please enter a valid number.")
            return

    else:

        print("Invalid choice.")
        return

    display_students(result)


def sort_students():

    students = read_students()

    print("\n1. Sort by Name")
    print("2. Sort by Age")
    print("3. Sort by Marks")

    choice = input("Enter choice: ")

    try:

        if choice == "1":

            students.sort(
                key=lambda x: x["Name"].lower()
            )

        elif choice == "2":

            students.sort(
                key=lambda x: int(x["Age"])
            )

        elif choice == "3":

            students.sort(
                key=lambda x: float(x["Marks"]),
                reverse=True
            )

        else:

            print("Invalid choice.")
            return

        display_students(students)

    except ValueError:

        print("Invalid data in CSV.")