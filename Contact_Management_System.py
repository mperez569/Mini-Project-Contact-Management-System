#mini project
import os
import re
contacts = {}

def print_welcome_message():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

def add_contact():
    unique_id = input("Enter unique identifier (phone/email): ").strip()
    if unique_id in contacts:
        print("Contact already exists. Use edit option to update.")
        return

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    additional_info = input("Enter additional information (address, notes): ").strip()

    contacts[unique_id] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Information": additional_info
    }
    print(f"Contact added for {unique_id}")

def edit_contact():
    unique_id = input("Enter the unique identifier of the contact to edit: ").strip()
    if unique_id not in contacts:
        print("Contact not found.")
        return

    print("Leave field blank to keep current value.")
    name = input(f"Enter new name (current: {contacts[unique_id]['Name']}): ").strip() or contacts[unique_id]['Name']
    phone = input(f"Enter new phone number (current: {contacts[unique_id]['Phone']}): ").strip() or contacts[unique_id]['Phone']
    email = input(f"Enter new email address (current: {contacts[unique_id]['Email']}): ").strip() or contacts[unique_id]['Email']
    additional_info = input(f"Enter new additional information (current: {contacts[unique_id]['Additional Information']}): ").strip() or contacts[unique_id]['Additional Information']

    contacts[unique_id] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Information": additional_info
    }
    print(f"Contact updated for {unique_id}")

def delete_contact():
    unique_id = input("Enter the unique identifier of the contact to delete: ").strip()
    if unique_id in contacts:
        del contacts[unique_id]
        print(f"Contact deleted for {unique_id}")
    else:
        print("Contact not found.")

def search_contact():
    unique_id = input("Enter the unique identifier of the contact to search: ").strip()
    if unique_id in contacts:
        contact = contacts[unique_id]
        print(f"Details for {unique_id}:")
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Additional Information: {contact['Additional Information']}")
    else:
        print("Contact not found.")

def display_contacts():
    if contacts:
        print("Contacts List:")
        for unique_id, contact in contacts.items():
            print(f"ID: {unique_id}")
            print(f"  Name: {contact['Name']}")
            print(f"  Phone: {contact['Phone']}")
            print(f"  Email: {contact['Email']}")
            print(f"  Additional Information: {contact['Additional Information']}")
            print()
    else:
        print("No contacts available.")

def export_contacts():
    filename = input("Enter filename to export to (e.g., contacts.txt): ").strip()
    try:
        with open(filename, 'w') as file:
            for unique_id, contact in contacts.items():
                file.write(f"ID: {unique_id}\n")
                file.write(f"Name: {contact['Name']}\n")
                file.write(f"Phone: {contact['Phone']}\n")
                file.write(f"Email: {contact['Email']}\n")
                file.write(f"Additional Information: {contact['Additional Information']}\n")
                file.write("\n")
        print(f"Contacts exported to {filename}")
    except Exception as e:
        print(f"An error occurred while exporting: {e}")

def import_contacts():
    filename = input("Enter filename to import from (e.g., contacts.txt): ").strip()
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            contact = {}
            unique_id = None
            for line in lines:
                if line.startswith("ID: "):
                    if unique_id and contact:
                        contacts[unique_id] = contact
                    unique_id = line.strip()[4:]
                    contact = {}
                elif line.startswith("Name: "):
                    contact['Name'] = line.strip()[6:]
                elif line.startswith("Phone: "):
                    contact['Phone'] = line.strip()[7:]
                elif line.startswith("Email: "):
                    contact['Email'] = line.strip()[7:]
                elif line.startswith("Additional Information: "):
                    contact['Additional Information'] = line.strip()[26:]
            if unique_id and contact:
                contacts[unique_id] = contact
        print(f"Contacts imported from {filename}")
    except Exception as e:
        print(f"An error occurred while importing: {e}")

def main():
    while True:
        print_welcome_message()
        choice = input("Select an option (1-8): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

main()
