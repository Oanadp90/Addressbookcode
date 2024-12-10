class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name,phone_number,email)
        self.contacts.append(new_contact)

        #This ADD contact isn't working...
        #AttributeError: 'list' object has no attribute 'add'
        #we will now remove line 17 in order to allow for our definition to work and print the information
        #we will now add the phone number and email within the print statement on line 20, so that the message can be printed
        print(f"Contact '{name}', '{phone_number}', '{email}' added successfully.")

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
        found = False
        for contact in self.contacts:
            if contact.name == name:
                print(f"Found contact: Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
                found = True
                break
        if not found:
            print(f"Contact with name: {name} not found!")    

    def update_contact(self, old_name, new_name= None, new_phone= None, new_email= None): #Missing UPDATE contact function
        for contact in self.contacts:
            if contact.name == old_name:
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone_number = new_phone
                if new_email:
                    contact.email = new_email
                print(f"Updated contact: Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")    
                return
        print(f"Contact with name {old_name} not found.")            
        
    def delete(self,name):             #Missing DELETE contact function
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' has been deleted.")
                return
        print(f"Contact with name {name} not found!")                  

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        #Missing options
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email) #AttributeError: 'list' object has no attribute 'add'
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            #Needs code here to check incorrect user choice 
            print("")

if __name__ == "__main__":
    main()                    #AttributeError: 'list' object has no attribute 'add'
