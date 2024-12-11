
from colorama import Fore
#imported colorama library so that we can have a bit more colour to our code

print("Welcome to the Address Book program!")

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "0754 322 532", "Alice@gmail.com"),
            Contact("Tommy", "0743 223 493", "Tommy@yahoo.com")
        ]

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name,phone_number,email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}', '{phone_number}', '{email}' added successfully.")

        #This ADD contact isn't working...
        #AttributeError: 'list' object has no attribute 'add'
        #we will now remove line 17 in order to allow for our definition to work and print the information
        #we will now add the phone number and email within the print statement on line 20, so that the message can be printed
        
    def display_all_contacts(self): 
        if not self.contacts:
            print("No contacts found.")
        else:
            print("All contacts: ")    
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
            #Errors in code here : Condition statements are not set in the right way, it should start with if, continue with elif and finish with else
            #So, in this cas we need to remove "for" and add "elif" on line 28 and also change "contact" to "Contact" and "contacts" to "self.contacts"
            #Also fix the indentation on line 29 for the print statement to execute the print message

    def search_contact(self,name): #Missing SEARCH contact function
        found = False  #A boolean variable found is initialized to False. This variable will track whether the contact with the given name is found in the list of contacts.
        #If the contact is found, found will be set to True, and the program will stop searching further.
        for contact in self.contacts:
            if contact.name == name:
                print(f"Found contact: Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
                found = True #This is to indicate that the contact was found
                break #And this is to exit the game early and prevent more searching once contact has been found
        if not found:   #If not found, print the message "Contact with "name: " was not found!"
            print(f"Contact with name: {name} not found!")    
          
    def update_contact(self, initial_name, updated_name= None, updated_phone= None, updated_email= None): #Missing UPDATE contact function
        for contact in self.contacts:# Iterate through all contacts in the contact book
            if contact.name == initial_name: # Check if the current contact's name matches the one that needs to be updated
                if updated_name:# If a new name is provided, update the contact's name
                    contact.name = updated_name
                if updated_phone:# If a new phone number is provided, update the contact's phone number
                    contact.phone_number = updated_phone
                if updated_email:# If a new email is provided, update the contact's email
                    contact.email = updated_email
                print(f"Updated contact: Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}") # Print the updated contact information 
                return
        print(f"Contact with name {initial_name} not found.")    # If no contact with the given name is found, print an error message         
        
    def delete(self,name):             #Missing DELETE contact function
        for contact in self.contacts: #This function is done a similar way as the above so comments are the same,except this time i have 
            #created a delete function so that the user can have an option to delete a contact by using the self.contacts.remove() method
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' has been deleted.")
                return
        print(f"Contact with name {name} not found!")         

def main():
    contact_book = ContactBook()

    while True:    #Loop that will help our code check each condition statement and execute the code based
        print(Fore.YELLOW + "\n--- Contact Book Menu ---") #Missing options for printing a message everytime the user will enter an option, which will print out the Menu of the contact book that includes : Add a new contact, display all contacts, Search Contact, Update contact,Delete contact and Exit options for user to choose from.
        print(Fore.GREEN + "1. Add New Contact")
        print(Fore.MAGENTA + "2. Display All Contacts")
        print(Fore.RED + "3. Search Contact")
        print(Fore.LIGHTGREEN_EX + "4. Update Contact")
        print(Fore.LIGHTRED_EX + "5. Delete Contact")
        print(Fore.LIGHTYELLOW_EX + "0. Exit")                      
        
        
        choice = input(Fore.BLUE + "Enter your choice: ") #This variable is for allowing the user to enter their choice

        # These are condition statements that will check and see what information the user will input
        #Also to add, display, search and delete based on what the user would enter
        
        if choice == "1":      #condition statement to decide if user will enter 1, add contact in the address book by calling contact_book.add_contact()method and giving the contact information as arguments: name, phone_number, email.
            name = input("Enter name: ") 
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":  #condition statement to decide if user will enter 2, call method contact_book.display_all_contacts() and display all contacts from the contactbook
            contact_book.display_all_contacts()
        elif choice == "3": #condition statement to decide if user will enter 3, call method contact_book.search_contacts() to search the contact name the user will enter
            name = input("Enter name: ")
            contact_book.search_contact(name)
        elif choice == "4": #condition statement to decide if user will enter 4, call method contact_book.update_contact() to update the contact with the new name or phone number/email the user will choose
            initial_name = input("Please enter the name of the contact you wish to update: ")
            updated_name = input("Please enter the new name: ")
            updated_phone = input("Please enter the new number: ")
            updated_email = input("Please enter the new email: ")
            contact_book.update_contact(initial_name, updated_name, updated_phone, updated_email)
        elif choice == "5":  #condition statement to decide if user will enter 5, to delete a specific contact name that they would choose
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete(name)
        elif choice == "0": #contition statement that will allow user to exit the Addressbook
            print("Exiting Contact Book. Goodbye!")
            break # this is to break the loop once the user will choose 0
        else:    # this is a condition statement from the structure if, elif and else to handle error when an user would input anything else except information for the Addressbook and also print a message to let them know that they need to enter a valid input.
            print("Invalid choice. Please enter a valid option.")  

if __name__ == "__main__":  #This is to run the code in the terminal as we have 2 different classes that we have built our code from, i hope this explanation makes sence.
    main()            
