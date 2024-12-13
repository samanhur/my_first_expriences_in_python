from admin import Admin


admin = Admin("saman", "ghasemi", "samanhur", 20)
admin.describe_user()

admin.privileges.show_privileges()

print("\nAdding privileges...")

admin_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
admin.privileges.privileges = admin_privileges

print(f"\nThe admin {admin.username} has these privileges: ")
admin.privileges.show_privileges()