from loader import load_students, save_students
from analytics import show_analytics


def display_students(students):
    print("\n===== STUDENT RECORDS =====")

    if not students:
        print("No students found.")
        return

    for student_id, student in enumerate(students, start=1):
        print(
            student_id,
            student["name"],
            student["phone"],
            student["email"]
        )


def main():

    students, total, rejected = load_students()

    while True:

        print("\n===== STUDENT REGISTRATION SYSTEM =====")
        print("1. View all students")
        print("2. Search student")
        print("3. Register student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Analytics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_students(students)

        elif choice == "2":
            search = input("Enter name, phone or email: ").strip().lower()

            found = False

            for student in students:
                if (search in student["name"].lower()
                    or search in student["phone"]
                    or search in student["email"].lower()):

                    print(student)
                    found = True

            if not found:
                print("Student not found.")

        elif choice == "3":
            name = input("Enter student name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            from validator import validate_contact
            is_valid, reason = validate_contact(name, phone, email)

            if not is_valid:
                print("Registration failed:", reason)
            elif any(s["phone"] == phone.strip() for s in students):
                print("Phone already exists.")
            elif any(s["email"].lower() == email.strip().lower() for s in students):
                print("Email already exists.")
            else:
                student = {
                    "name": name.strip(),
                    "phone": phone.strip(),
                    "email": email.strip()
                }
                students.append(student)
                print("Student registered successfully!")

        elif choice == "4":
            phone = input("Enter current phone number: ")
            for student in students:
                if student["phone"] == phone:
                    student["name"] = input("Enter new name: ")
                    student["email"] = input("Enter new email: ")
                    print("Student updated!")
                    break
            else:
                print("Student not found.")

        elif choice == "5":
            phone = input("Enter phone number to delete: ")
            for student in students:
                if student["phone"] == phone:
                    students.remove(student)
                    print("Student deleted successfully!")
                    break
            else:
                print("Student not found.")

        elif choice == "6":
            show_analytics(students, total, rejected)

        elif choice == "7":
            save_students(students)
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()