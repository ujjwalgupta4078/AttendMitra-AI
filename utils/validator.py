def validate_student(name, roll, email):

    if not name:
        return False, "Name is required."

    if not roll:
        return False, "Roll Number is required."

    if "@" not in email:
        return False, "Invalid Email."

    return True, "Valid"