from auth.session import login_user

def authenticate(email, password, role):

    # Placeholder authentication

    if email and password:

        login_user(role, email)

        return True

    return False