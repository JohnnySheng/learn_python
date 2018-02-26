def greet_users(users):
    for user in users:
        print("Hello " + user.title() + "!")

greet_users(['Johnny', 'Tom'])