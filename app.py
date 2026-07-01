"""TaskFlow, a tiny task manager used in the "Claude Code for Builders" class.

This is the main entry point. Run it with:

    python app.py

It is intentionally small so we can read, change, and break it live.
"""

from flask import Flask, request, render_template, redirect, url_for

from taskflow.registration import register_user
from taskflow.auth import authenticate
from taskflow.calculator import completion_rate

app = Flask(__name__)

# In-memory "database" for the demo (resets every restart, that's fine for class).
users = []
tasks = [
    {"title": "Set up Claude Code", "done": True},
    {"title": "Clone the demo repo", "done": True},
    {"title": "Fix the registration bug", "done": False},
    {"title": "Write unit tests", "done": False},
]


@app.route("/")
def home():
    rate = completion_rate(tasks)
    return render_template("index.html", tasks=tasks, rate=rate)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form = {
            "username": request.form.get("username", ""),
            "email": request.form.get("email", ""),
            "password": request.form.get("password", ""),
        }
        register_user(users, form)
        return redirect(url_for("home"))
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
