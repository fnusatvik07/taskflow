"""User registration.

NOTE FOR CLASS: this intentionally has a bug. It accepts empty forms , 
any field can be blank and a user is still created. We fix this live with
Claude Code by asking it to "add input validation to the registration form".
"""


def register_user(users, form):
    """Add a new user from a submitted registration form.

    Bug: there is no validation here. Empty username / email / password
    all sail straight through and create a (useless) user.
    """
    user = {
        "username": form.get("username", ""),
        "email": form.get("email", ""),
        "password": form.get("password", ""),
    }
    users.append(user)
    return user
