"""
Yunsun Park
CP1404 Practical
emails

Estimate: 60 minutes
Actual:   minutes


"""

dictionary = dict()

def add_record(name, email):
    dictionary[name] = email
    save()

# saving values to file
def save():
    with open('emails.txt', 'w') as handle:
        handle.write(str(dictionary))
        handle.close()

# looks up email for given name
def lookup_email(name):
    read()
    if name in dictionary.keys():
        return dictionary[name]

# delets an email of given email
def delete_entry(name):
    read()
    if name in dictionary.keys():
        dictionary[name] = None
        del dictionary[name]
        save()
        return True
    return False

# Menu display
def menu():
    print("")
    print("Menu")
    print("-----------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5.Quit the program")
    print("")
    try:
        selection = int(input("Enter your choice: "))
        return selection
    except:
        print("Invalid Input")

# reads data from file
def read():
    with open("emails.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(",")
            dictionary[key] = value

# Main function execution starts from here
if __name__ == '__main__':

    while True:
        choice = menu()
        if choice == 1:
            name = input("Enter a name: ")
            try:
                email = lookup_email(name)
                if (email != None):
                    print(email)
                else:
                    print("No Data Found")
            except:
                print("The specified name was not found")
        elif choice == 2:
            name = input("Enter name: ")
            email = input("Enter Email Address: ")
            add_record(name, email)
            print("Name and Email has been added")
        elif choice == 3:
            name = input("Enter the Name: ")
            email = input("Enter new Email Address")
            add_record(name, email)
            print("Information updated")
        elif choice == 4:
            name = input("Enter the Name: ")
            try:
                delete_entry(name)
                print("Information deleted")

            except:
                print("Something went wrong!!! please try again later")
        elif choice == 5:
            save()
            print("Information Saved")
            break;
        else:
            print("invalid input")