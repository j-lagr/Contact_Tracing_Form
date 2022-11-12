#Write a python program for contact tracing:
# - Display a menu of options
contacts = {}
info =[]
def menu():
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
    menu=input("| What can we do for you today? |")
    print("---------------------------------")

def yesno():
    While True:
        homemenu= input("Do you want to go bac to the menu? [Y/N] ")
        if homemenu == "Y":
            menu()
            break
        elif homemenu == "N":
            print("Thank you for filling out the contact tracing form!")

# Menu:
# 1 -> Add an item
if menu == "1":
    name = input("Enter your first and last name: ")
    age = input("Enter your age: ")
    phone_num= input("Enter your phone number (ex. 09xxxxxxxxx): ")
    test_covid= input("Did you test positive for COVID or have any COVID-like symptoms? ")

    info.append(age)
    info.append(phone_num)
    info.append(test_covid)
    print (info)
    contacts[name]=info
    print (contacts)

    # 2 -> Search
elif menu == "2":
    search = input("Enter the first an1d last name of the contact: ")
    if search == contacts:
        print("Name:", search)
        print(contacts.get("search"))

# 3 -> Edit info
# 4 -> Delete info
# 5 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# - Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# Use dictionary to store the info
# Use the full name as keyThe value is another dictionary of personal information
# - Option 2: Search, ask full name then display the record
# - Option 3: Ask the user if want to exit or retry.