from clear import clear
from owner import get_owner
from helpmenu import help_menu
from idle import idle
from writer import write_entry
from reader import read_entry
from finder import find_keyword
from directory import view_directory
from menu import menu

def main():

    clear()
    owner = get_owner()
    print('=' * 40)
    print(f"{owner}'s diary")
    menu()
    while True:
        print(f"\nEnter command: ")
        choice = input(">>> ").lower()

        if choice == "idle":
            idle()
        elif choice == "exit":
            print("Exiting...")
            break
        elif choice == "find":
            find_keyword()
        elif choice == "read":
            read_entry()
        elif choice == "write":
            write_entry()
        elif choice == "dir":
            view_directory()
        elif choice == "help" or choice == "h":
            help_menu()
        elif choice == "clear":
            clear()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
