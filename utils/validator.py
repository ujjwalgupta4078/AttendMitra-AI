import re

def validate_student(name, roll_no, email, mobile):

    if name.strip() == "":
        return False, "Name cannot be empty."

    if roll_no.strip() == "":
        return False, "Roll Number cannot be empty."

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(email_pattern, email):
        return False, "Invalid email address."

    if len(mobile) != 10 or not mobile.isdigit():
        return False, "Mobile number must contain exactly 10 digits."

    return True, "Validation Successful"