def show_analytics(students, total_records=None, rejected=None):

    if total_records is None:
        total_records = len(students)

    if rejected is None:
        rejected = []

    # Data quality
    accepted = len(students)

    if total_records > 0:
        valid_percentage = (accepted / total_records) * 100
    else:
        valid_percentage = 0

    print("\n===== DATA QUALITY REPORT =====")
    print("Total records:", total_records)
    print("Accepted records:", accepted)
    print("Rejected records:", len(rejected))
    print("Valid percentage:", round(valid_percentage, 2), "%")

    print("\nRejection reasons:")
    for reason in rejected:
        print("-", reason)

    # Phone prefix distribution
    phone_counts = {}

    for student in students:
        prefix = student["phone"][0]
        phone_counts[prefix] = phone_counts.get(prefix, 0) + 1

    print("\n===== PHONE PREFIX DISTRIBUTION =====")

    for prefix in ["6", "7", "8", "9"]:
        print(prefix, ":", phone_counts.get(prefix, 0))

    # Email domain frequency
    email_counts = {}

    for student in students:
        domain = student["email"].split("@")[1]
        email_counts[domain] = email_counts.get(domain, 0) + 1

    print("\n===== EMAIL DOMAIN FREQUENCY =====")

    for domain, count in email_counts.items():
        print(domain, ":", count)