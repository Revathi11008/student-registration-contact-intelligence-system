def validate_contact(name, phone, email):

    # Remove extra spaces
    name = name.strip()
    phone = phone.strip()
    email = email.strip()

    # Check name
    if name == "":
        return False, "Name is blank"

    # Check phone number
    if len(phone) != 10 or not phone.isdigit():
        return False, "Invalid 10-digit phone"

    if not phone.startswith(("6", "7", "8", "9")):
        return False, "Invalid 10-digit phone"

    # Check email
    if email.count("@") != 1:
        return False, "Malformed email"

    if any(char.isspace() for char in email):
        return False, "Malformed email"

    username, domain = email.split("@")

    if username == "":
        return False, "Malformed email"

    if "." not in domain:
        return False, "Malformed email"

    if domain.startswith(".") or domain.endswith("."):
        return False, "Malformed email"

    return True, "Valid"


# Testing
print(validate_contact("Revathi", "9876543210", "revathi@gmail.com"))
print(validate_contact("", "9876543210", "revathi@gmail.com"))
print(validate_contact("Anu", "1234567890", "anu@gmail.com"))
print(validate_contact("Rahul", "9876543210", "rahulgmail.com"))
