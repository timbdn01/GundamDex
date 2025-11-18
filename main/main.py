from gundam import Gundam
from add import add_gundam
from search import search_gundam
import sys

def main():
    gundam_list = []
    print("Welcome to the Gundam Management System!")
    options(gundam_list)

def options(gundam_list):
    print("What would you like to do?")
    print("1. Add a Gundam")
    print("2. Search for a Gundam")
    print("3. View all Gundams")
    print("4. Exit")
    input_choice = input("\nEnter your choice (1-4): ")
    match input_choice:
        case '1':
            new_gundam = add_gundam()
            gundam_list.append(new_gundam)
            options(gundam_list)
        case '2':
            search_gundam(gundam_list)
            options(gundam_list)
        case '3':
            if gundam_list == []:
                print("\nNo Gundams in the system.\n")
            else:
                for gundam in gundam_list:
                    print(gundam.display_info())
            options(gundam_list)
        case '4':
            print("Exiting the system. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
