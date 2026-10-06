from student_manager import (
    add_student,
    update_student,
    delete_student,
    search_student,
    filter_student,
    sort_students,
    display_students,
    read_students
)


def main():

    while True:

        print("\n======================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Filter Student")
        print("6. Sort Students")
        print("7. Display All Students")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":
                add_student()

            elif choice == "2":
                update_student()

            elif choice == "3":
                delete_student()

            elif choice == "4":
                search_student()

            elif choice == "5":
                filter_student()

            elif choice == "6":
                sort_students()

            elif choice == "7":
                students = read_students()
                display_students(students)

            elif choice == "8":
                print("\nThank you for using Student Management System!")
                break

            else:
                print("\nInvalid choice. Please enter 1-8.")

        except Exception as error:
            print("\nSomething went wrong:", error)


if __name__ == "__main__":
    main()