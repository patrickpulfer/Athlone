fullname = str(input("Enter your first and last names, separated by a space: "))
firstname, lastname = fullname.split()
username = firstname.lower() + lastname[0].lower()

print(username)