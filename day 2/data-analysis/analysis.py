import csv
from collections import Counter

FILE = "student_data.csv"


def read_data():
    try:
        with open(FILE, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    except FileNotFoundError:
        print("Error: student_data.csv not found.")
        return []


def record_count(data):
    print("\n===== RECORD COUNT =====")
    print("Total records:", len(data))


def missing_values(data):
    print("\n===== MISSING VALUES =====")

    if not data:
        return

    for column in data[0].keys():
        count = 0

        for row in data:
            if row[column].strip() == "":
                count += 1

        print(f"{column}: {count}")


def duplicate_records(data):
    print("\n===== DUPLICATE RECORDS =====")

    ids = [row["ID"] for row in data]

    duplicates = [
        item for item, count in Counter(ids).items()
        if count > 1
    ]

    if duplicates:
        print("Duplicate IDs:", duplicates)
    else:
        print("No duplicate records found.")


def marks_statistics(data):
    print("\n===== MARKS STATISTICS =====")

    marks = []

    for row in data:
        try:
            marks.append(float(row["Marks"]))
        except (ValueError, KeyError):
            pass

    if not marks:
        print("No valid marks found.")
        return

    average = sum(marks) / len(marks)

    print(f"Average Marks : {average:.2f}")
    print(f"Minimum Marks : {min(marks)}")
    print(f"Maximum Marks : {max(marks)}")


def department_statistics(data):
    print("\n===== DEPARTMENT-WISE STATISTICS =====")

    departments = {}

    for row in data:

        department = row["Department"]

        if department not in departments:
            departments[department] = []

        try:
            departments[department].append(
                float(row["Marks"])
            )
        except ValueError:
            pass

    for department, marks in departments.items():

        print(f"\nDepartment: {department}")
        print("Number of Students:", len(marks))

        if marks:
            average = sum(marks) / len(marks)

            print(f"Average Marks: {average:.2f}")
            print(f"Minimum Marks: {min(marks)}")
            print(f"Maximum Marks: {max(marks)}")


def main():

    data = read_data()

    if not data:
        return

    while True:

        print("\n==============================")
        print("       DATA ANALYSIS")
        print("==============================")

        print("1. Record Count")
        print("2. Missing Values")
        print("3. Duplicate Records")
        print("4. Average / Minimum / Maximum")
        print("5. Department-wise Statistics")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            record_count(data)

        elif choice == "2":
            missing_values(data)

        elif choice == "3":
            duplicate_records(data)

        elif choice == "4":
            marks_statistics(data)

        elif choice == "5":
            department_statistics(data)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()