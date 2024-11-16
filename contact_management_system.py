

# Need while loop for the menu choices >>> create the choices
# create the functions >>> created add, display, delete, edit, search
# create a sample dictionary
# need to import re
# create regex patterns for email and phone

import re

contacts = {
    "123-456-7890" : {
        "Name" : "Den Russell",
        "Phone number" : "123-456-7890",
        "Email address" : "den.russell@email.com"

    }

}

phone_pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")
email_pattern = email_pattern_specific = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def add_contact():
    phone = input("Enter phone number (Format 000-000-0000): ")
    if not phone_pattern.match(phone):
        print("Invalid format.")
        return

    if phone in contacts:
        print("\nContact already exists.")
        return
    
    name = input("Enter name: ")
    email = input("Enter email address: ")
    if not email_pattern.match(email):
        print("Invalid email.")
        return
    
    contacts[phone] = {
        "Name" : name,
        "Phone number" : phone, 
        "Email address" : email
    }
    print("\nContact added successfully.")

def edit_contact():
    phone = input("Enter the phone number of the contact you wish to edit (000-000-0000): ")
    if phone not in contacts:
        print("Contact not found.")
        return
    
    name = input("Enter new name: ")
    new_phone = input("Enter new phone number: ")
    email = input("Enter new email address: ")
    
    if new_phone in contacts:
        print("Contact already exists.")
        return
    
    contacts.pop(phone)
    contacts[new_phone] = {
        "Name" : name,
        "Phone number" : phone,
        "Email address" : email
    }

    print("\nContact updated successfully.")


def delete_contact():
    phone = input("Enter the phone number of the contact you wish to delete (000-000-0000):")
    if phone in contacts:
        del contacts[phone]
        print(f"{phone} deleted successfully.")
        return
    else:
        print("Phone not found.")
        return


def search_contact():
    phone = input("Enter phone number: ")
    if phone in contacts:
        contact = contacts[phone]
        print("\nContact Details:")
        print(f"Name: {contact["Name"]}")
        print(f"Phone Number: {contact["Phone number"]}")
        print(f"Email Address: {contact["Email address"]}")
    
    else:
        print("Contact not found.")


def display_all_contacts():
    if not contacts:
        print("No contacts.")
        return
    
    for phone, details in contacts.items():
        print(f"\nName: {details["Name"]}")
        print(f"Phone number: {phone}")
        print(f"Email address: {details["Email address"]}")

def export_to_text_file():
    try:
        with open("contacts.txt", "w") as file:
            for phone, details in contacts.items():
                file.write(f"{phone},{details['Name']},{details['Email address']}\n")
        print("Contacts exported to contacts.txt successfully.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")
     
   


def main():
    print("\n\nWelcome to the Contact Management System!\n\nMenu:")

    while True:
        print("\n1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Quit")

        try:
            choice = input("\nEnter choice: ")

            if choice == "1":
                add_contact()
            elif choice == "2":
                edit_contact()
            elif choice == "3":
                delete_contact()
            elif choice == "4":
                search_contact()
            elif choice == "5":
                display_all_contacts()
            elif choice == "6":
                export_to_text_file()
            elif choice == "7":
                break
            else:
                print("Invalid choice.")
        
        except Exception as e:
            print(f"Error occured: {e}")
        
    
if __name__ == "__main__":
    main()