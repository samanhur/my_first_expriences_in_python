# def build_profile(first, last, **user_info):
#     """Build a dictionary containig everything we know about a user."""
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info


# New version:
def build_profile(first_name, last_name, **others):
    """Build a dictionary containing everything we know about a user."""
    user_dict = {
        "name": first_name.title(),
        "family": last_name.title(),
    }
    for key, value in others.items():
        user_dict[key] = value
    
    return user_dict


user_profile = build_profile(
    "saman",
    "ghasemi",
    middle_name="hur",
    field_of_study="mathematics",
    age=19,
    location="tehran",
)
print(user_profile)
