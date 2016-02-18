'''
from NotTheDatabase import DBReader

db_reader = DBReader()
# user_data = []


def password_match():
    pass


while True:

    username_to_search = input("Please enter your USERNAME: ")
    password_to_search = input("Shwhat is your password? ")
    try:
        user_data = db_reader.get_by_username(username_to_search)
    except Exception:
        print(db_reader.filter_by_username(username_to_search))

    print(user_data[2:])'''

username = []
password = []

with open("database") as infile:
    data = infile.readlines()
database_list = [line.split(',') for line in data]
for lines in database_list:
    username.append(lines[0])
    password.append(lines[1])

user_password_input = ""
user_input = ""
unknown_user = True
unknown_password = True
unknown_new_user = True
while unknown_user:
    user_input = input("Enter username: ")
    if user_input in username:
        print("Username verified. \nWelcome {}! \nIt's nice to see you again.  \n".format(user_input))
        unknown_user = False
    else:
        print("Not valid username.  Try again or call |1-888-YOU-DUMB|")
username = user_input
while unknown_password:
    user_password_input = input("Please enter password on file: ")
    if user_password_input in password:
        print("Password verified.\n")
        unknown_password = False
    else:
        print("Not valid password.  \nTry again or contact program administrator or call |1-888-YOU-DUMB|")
password = user_password_input

user_data = [line for line in database_list if line[0].lower() == username.lower()]
for items in user_data:
    for item in items:
        if item == username:
            continue
        elif item == password:
            continue
        else:
            print("User specific info: {}".format(item))

while unknown_new_user:
    add_new_user = input("Want to add new user? y/n ")
    if add_new_user.lower() == 'y':
        with open("database", "a") as outfile:
            new_user_name = input("Enter new username: ")
            if new_user_name not in username:
                outfile.write("\n" + (new_user_name).lower())
                outfile.write("," + input("Enter new password: ").lower())
                outfile.write("," + input("Enter the user's name: ").lower())
                outfile.write("," + input("Enter the user's favorite color: ").lower())
                outfile.write("," + input("Enter the user's favorite animal: ").lower())
                print("Awesome, you added a new user!")
                continue
            else:
                print("That's embarrassing, that user already exists.")
    else:
        unknown_new_user = False

logout = input("Ready to log out? y/n ")
if logout.lower() == 'y':
    print("Logged out, bye!")
else:
    print("Too bad, you are logged out. ")
