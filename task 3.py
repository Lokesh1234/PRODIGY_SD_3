class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")

    new_contact = Contact(name, phone_number, email)
    contacts.append(new_contact)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("Contact List:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact.name} - {contact.phone_number} - {contact.email}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the index of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            contact.phone_number = input(f"Enter new phone number for {contact.name}: ")
            contact.email = input(f"Enter new email address for {contact.name}: ")
            print("Contact edited successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"{deleted_contact.name} has been deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def main():
    contacts = []

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
