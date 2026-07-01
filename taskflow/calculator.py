"""Pure helper functions for task statistics.

These are deliberately simple and side-effect free, which makes them
perfect for the "write unit tests" demo in class.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Note: no zero-handling yet, a nice edge case for the tests demo.
    return a / b


def percentage(part, whole):
    return (part / whole) * 100


def completion_rate(tasks):
    """Return the percentage of tasks marked done (0 when there are none)."""
    if not tasks:
        return 0
    done = sum(1 for task in tasks if task.get("done"))
    return round(percentage(done, len(tasks)), 1)
