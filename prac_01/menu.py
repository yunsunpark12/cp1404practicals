MENU = "(H)ello\n(G)oodbye\n(Q)uit"
QUIT_MESSAGE = "Finished."

name = input("Enter name: ")
print(MENU)
choice = input(">>>").upper()

while choice != "Q":
    if choice == "H":
       print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>>").upper()

print(QUIT_MESSAGE)