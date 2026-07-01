"""Authentication using callback style.

This is written with callbacks ON PURPOSE. In class we ask Claude Code to
"refactor the authentication module to use async/await instead of callbacks"
and watch it modernise this file.
"""

import time


def authenticate(users, username, password, on_success, on_error):
    """Authenticate a user, then invoke on_success(user) or on_error(reason)."""

    def _lookup():
        for user in users:
            if user["username"] == username:
                return user
        return None

    user = _lookup()
    if user is None:
        on_error("User not found")
        return

    # Pretend this is a slow check (e.g. password hashing / a DB round-trip).
    time.sleep(0.1)

    if user["password"] == password:
        on_success(user)
    else:
        on_error("Invalid password")
