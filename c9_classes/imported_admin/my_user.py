from users import Admin


admin = Admin("saman", "ghasemi", "samanhur", 20)
admin.describe_user()

admin.privileges.show_privileges()

print("\nAdding privileges...")

admin.privileges.privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
print(f"\nThe admin {admin.username} has these privileges: ")
admin.privileges.show_privileges()
