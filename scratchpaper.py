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
        print(f"Contact '{name}', '{phone_number}', '{email}' added successfully.")

    def display_all_contacts(self, name, phone_number, email): 
        if self.contacts:
            print("All Contacts: ")
        elif Contact in self.contacts:
            print(f"Name: {name}\nPhone: {phone_number}\nEmail: {email}\n") 
        else:
            print("No contacts found.")

def search_contact(self): #Missing SEARCH contact function
        if Contact in self.contacts:
            print(self)
        elif Contact not in self.contacts:
            print("This contact is not in this list, please add by using ADD option!") 

    def update_contact(self, old_name, new_name= None, new_phone= None, new_email= None): #Missing UPDATE contact function
        if Contact:
            if new_phone:
                contact.phone_number = new_phone
            if new_email:
                contact.email = new_email
            print (f"Contact updated : {Contact}")    
        for Contacts in self.contacts:
            if contact.name == old_name:
                contact.update(new_name,new_phone,new_email)
                print("f"Updated contact: {contact} ")
                      return
        print(f"Contact with name {old_name} not found.")              
            
