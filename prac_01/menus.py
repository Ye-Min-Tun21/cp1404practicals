MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")
choice = ""
while choice != "Q":
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    elif choice != "Q":
        print("Invalid choice")
print("Finished.")
