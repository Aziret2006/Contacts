from views import (migration, sign_up, log_in, get_current_user,
                   create_contact, get_contact, show_contacts,
                   update_contact,delete_contact)


def main():
    migration()

    while True:
        user = get_current_user()
        if user is None:
            action = input("Enter 1 to 'Log in'\nEnter 2 to 'Sign up'\nEnter 3 to exit\n: ").strip()
            if action == '1':
                log_in()
            elif action == '2':
                sign_up()
            elif action == '3':
                print("Good bye!")
                break
            else:
                print("\nIncorrect command!\n")
        else:
            action = input("\nEnter 1 to create contact\nEnter 2 to search contact\nEnter 3 to show all contact\n"
                           "Enter 4 to update contact\nEnter 5 to delete contact\nEnter 6 to exit\n: ").strip()
            if action == '1':
                create_contact()
            elif action == '2':
                get_contact()
            elif action == '3':
                show_contacts()
            elif action == '4':
                update_contact()
            elif action == '5':
                delete_contact()
            elif action == '6':
                print(f"Good bye! See you soon {user.username}!")
                break
            else:
                print("\nIncorrect command!\n")


if __name__ == '__main__':
    main()
