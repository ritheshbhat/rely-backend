

users = {
    "user1": "password1",
    "user2": "password2"
}

# Define a custom authentication function
@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        return username