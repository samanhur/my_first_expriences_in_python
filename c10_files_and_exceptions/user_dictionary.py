from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None


def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What's your user name? ")
    age = input("How old are you? ")
    job = input("What's your job? ")

    user_dict = {
        "username": username,
        "age": age,
        "job": job,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path("user_info.json")
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"I know you're {user_dict['age']} years old!")
        print(
            f"{user_dict['job'].title()} is a great job." " Thank you for doing that!"
        )
    else:
        user_dict = get_new_user_info(path)
        msg = (
            f"We'll remember you when you return, " f"dear {user_dict['username'].title()}"
        )
        print(msg)


greet_user()
