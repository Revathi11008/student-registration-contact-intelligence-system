import csv
from validator import validate_contact


def load_students():
    students = []
    seen_phones = set()
    seen_emails = set()
    rejected = []
    total = 0

    with open("contacts.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            name = row["name"]
            phone = row["phone"]
            email = row["email"]

            valid, reason = validate_contact(name, phone, email)

            if not valid:
                rejected.append(reason)
                continue

            if phone.strip() in seen_phones:
                rejected.append("Duplicate phone")
                continue

            if email.strip().lower() in seen_emails:
                rejected.append("Duplicate email")
                continue

            seen_phones.add(phone.strip())
            seen_emails.add(email.strip().lower())

            students.append({
                "name": name.strip(),
                "phone": phone.strip(),
                "email": email.strip()
            })

    print("Total records:", total)
    print("Accepted records:", len(students))
    print("Rejected records:", len(rejected))

    for reason in rejected:
        print("Rejected:", reason)

    return students, total, rejected


def save_students(students):
    with open("students_clean.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "phone", "email"]
        )
        writer.writeheader()
        writer.writerows(students)

    print("Student records saved successfully!")


if __name__ == "__main__":
    load_students()
