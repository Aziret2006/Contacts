from models import User, Contact, PhoneNumber


def migration():
    User.create_schema_query()
    Contact.create_schema_query()
    PhoneNumber.create_schema_query()


def sign_up():
    print("Sign up!\n\n")
    username = input("Enter username(max 20, min 10 symbols): ").strip().lower()
    password_one = input("Enter password (max 20, min 10 symbols): ")
    password_two = input("Password confirm\n: ")

    if 8 <= len(username) <= 20:
        if password_one == password_two:
            user = User(
                username=username,
                password=password_two
            )
            user.create()
            print(f"Congratulations! User {username} your sign up!😁")
        else:
            print("Password missmatch\n")
    else:
        print("Incorrect! Username length should be (max 20, min 10 symbols)! Try again\n")


def log_in():
    print("Log in!\n\n")
    username = input("Enter your username: ").strip().lower()
    password = input("Enter your password: ")

    user = User.get_or_none(username=username)
    if user is not None:
        if user.check_password(password=password):
            User.SESSION_USER = user
        else:
            print("\nPassword or username incorrect!\n")
    else:
        print(f"\nUser with {username} is not definded! 🔎?\n")


def get_current_user():
    return User.SESSION_USER


def create_contact():
    contact_name = input("Enter contact name (max symbols 50): ")
    contact = Contact(
        name=contact_name,
        client_id=User.SESSION_USER.id
    )
    contact_id = contact.create()

    numbers = []

    while True:
        number = input("Enter phone number (0202287569): ")
        is_valid = PhoneNumber.is_valid_number(number=number)
        if is_valid:
            number = PhoneNumber(
                number=number,
                contact_id=contact_id
            )
            numbers.append(number)
            add_additional_number = input("Enter 1 to add additional\nEnter 2 to finish\n: ")
            if add_additional_number == '2':
                break
        else:
            print("Incorrect format phone_number!")

    for number in numbers:
        number.create()


def show_contacts():
    contacts = Contact.all(user_id=User.SESSION_USER.id)
    if contacts is not None:
        for contact in contacts:
            contact_name, contact_numbers = contact
            print(f"\nContact: {contact_name} - {contact_numbers if contact_numbers is not None else 'Phones is empty!'}\n")
    else:
        print("\nEmpty!\n")


def get_contact():
    name = input("Enter contact name for search (max symbols 50): ")
    contact = Contact.get_or_none(
        name=name,
        user_id=User.SESSION_USER.id
    )
    if contact is not None:
        contact_name, contact_numbers = contact
        print(f"\nContact: {contact_name} - {contact_numbers}\n")
    else:
        print(f"\nUser with {name} is not definded! 🔎?\n")


def update_contact():
    name = input("Enter contact name to update (max symbols 50): ")

    contact = Contact.get_or_none(
        name=name,
        user_id=User.SESSION_USER.id
    )
    if contact is not None:
        contact_id = Contact.get_id(name=name)
        contact_name, contact_numbers = contact
        print(f"\nContact: {contact_name} - {contact_numbers if contact_numbers is not None else 'Phones is empty!'}\n")
        while True:
            action = input("Enter 1 to update cont.name\nEnter 2 to update cont.number(s)"
                           "\nEnter 3 to add phone number\nEnter 4 to exit\n: ").strip()
            if action == '1':
                new_name = input("Enter new name (max 50): ")
                change_name = Contact.update_name(
                    new_name=new_name,
                    name=name,
                    user_id=User.SESSION_USER.id
                )
                print("\nName edited success!😁\n")
            elif action == '2':
                number = input("Enter new number(0554596670):")
                is_valid_number = PhoneNumber.is_valid_number(number=number)
                if is_valid_number:
                    changed_number = Contact.update_numbers(
                        number=number,
                        contact_id=contact_id,
                        user_id=User.SESSION_USER.id)
                    print("\nPhone number edited success\n")
                else:
                    print("\nIncorrect format phone number!\n")
            elif action == '3':
                number = input("Enter phone number (0202287569): ")
                is_valid = PhoneNumber.is_valid_number(number=number)
                if is_valid:
                    number = PhoneNumber(
                        number=number,
                        contact_id=contact_id
                    )
                    number.create()
                    print("Number added success!\n")
                else:
                    print("Incorrect format phone_number!")

            elif action == '4':
                break
    else:
        print(f"\nUser with {name} is not definded! 🔎?\n")


def delete_contact():
    name = input("Enter contact name to delete (max symbols 50): ")
    is_deleted = Contact.delete(
        name=name,
        user_id=User.SESSION_USER.id
    )
    if is_deleted:
        print(f"Contact {name} is deleted success!\n")
    else:
        print(f"\nUser with {name} is not definded! 🔎?\n")
