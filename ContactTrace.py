#Write a python program for contact tracing:
# - Display a menu of options
contacts = {}
info =[]
def home():
    print()
    print("---------------------------------")
    print("| PourOver Contact Tracing Form |")
    print("---------------------------------")
    print("|                               |")
    print("|     |1| Fill out the form     |")
    print("|     |2| Search for contact    |")
    print("|     |3| Edit contact          |")
    print("|     |4| Delete contact        |")
    print("|     |5| Exit                  |")
    print("|                               |")
    print("---------------------------------")
    menu=input("| What can we do for you today? |\t")
    print("---------------------------------")

    if menu =="1":
        add_contact()
    elif menu=="2":
        search_contact()
    elif menu=="3":
        edit_contact()
    elif menu=="4":
        delete()
    elif menu=="5":
        print("Thank you for filling out the form!")
        exit()
    else:
        print ("Invalid option. Try Again.")
        yesno()


def yesno():
    while True:
        homemenu=input("Do you want to go back to the menu? [Y|N] ")
        if homemenu == "Y":
            home()
            break
        elif homemenu == "N":
            print("Thank you for filling out the contact tracing form!")
            exit()
        else:
            print("Invalid option")
                


# Menu:
# 1 -> Add an item
def add_contact():
    name = input("Enter your name: ").upper()
    age = input("Enter your age: ")
    phone_num= input("Enter your phone number (ex. 09xxxxxxxxx): ")
    test_covid= input("Did you test positive for COVID or have any COVID-like symptoms? ")
    info.append(age)
    info.append(phone_num)
    info.append(test_covid)
    print (info)
    contacts[name]=info.copy()
    print("Name:", name)
    print("Age:",contacts.get(name)[0])
    print("Phone Number:", contacts.get(name)[1])
    print("Covid Status:", contacts.get(name)[2])
    info.clear()
    yesno()

# 2 -> Search
def search_contact():
    search = input("Enter the name of the contact you want to search: ").upper()
    if search in contacts:
        print("Name:", search)
        print("Age:",contacts.get(search)[0])
        print("Phone Number:", contacts.get(search)[1])
        print("Covid Status:", contacts.get(search)[2])
        yesno()
    else:
        print("Contact not found.")
        yesno()

# 3 -> Edit info
def edit_contact():
    edit = input("Enter the name of the contact you want to edit: ").upper()
    if edit in contacts:
        print("1. Name:", edit)
        print("2. Age:",contacts.get(edit)[0])
        print("3. Phone Number:", contacts.get(edit)[1])
        print("4. Covid Status:", contacts.get(edit)[2])
        edit_what=input("What information do you want to edit? [1-4]")
        if edit_what == "1":
            new_name= input("Enter the new name: ")
            contacts[new_name]=contacts.pop(edit)
            print(contacts[new_name])
        elif edit_what =="2":
            new_age= input("Enter new age: ")
            contacts.get(edit)[0]=new_age
            print(contacts[edit])
        elif edit_what =="3":
            new_number= input("Enter the new phone number: ")
            contacts.get(edit)[1]=new_number
            print(contacts[edit])
        elif edit_what =="4":
            new_status= input("Enter new COVID status: ")
            contacts.get(edit)[2]=new_status
            print(contacts[edit])
        print("Updated information: ")
        print("Name:", edit)
        print("Age:",contacts.get(edit)[0])
        print("Phone Number:", contacts.get(edit)[1])
        print("Covid Status:", contacts.get(edit)[2])
        yesno()
    else:
        print("Contact not found.")
        yesno()


# 4 -> Delete info
def delete():
    delete_info= input("Enter the name of the contact that you want to delete: ").upper()
    del contacts[delete_info]
    print ("The contact has been deleted")
    yesno()

home()