from gundam import Gundam
from add import add_gundam
from search import search_gundam
from edit import edit_gundam_info
import sys
import os

def main():
    gundam_list = []
    print("********Welcome to the Gundam Management System!********\n")
    directory_path = input("Enter the directory path to access Gundam data files (enter blank to use current working directory): ").strip()
    if not directory_path:
        directory_path = os.getcwd()
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    if not os.access(directory_path, os.W_OK):
        print(f"Error: The directory '{directory_path}' is not writable. Please check permissions.")
        sys.exit(1)
    if "/gundams" not in directory_path:
        directory_path = os.path.join(directory_path, "gundams")
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    print(f"\nGundam data files will be accessed at: {directory_path}\n")
    add_txt_to_list(gundam_list, directory_path)
    options(gundam_list, directory_path)

def options(gundam_list, directory_path):
    print("What would you like to do?")
    print("1. Add a Gundam")
    print("2. Search for a Gundam")
    print("3. Edit a Gundam")
    print("4. View all Gundams")
    print("5. Exit\n")
    input_choice = input("\nEnter your choice (1-5): ")
    match input_choice:
        case '1':
            new_gundam = add_gundam(directory_path)
            gundam_list.append(new_gundam)
            options(gundam_list, directory_path)
        case '2':
            search_gundam(gundam_list)
            options(gundam_list, directory_path)
        case '3':
            if gundam_list == []:
                print("\nNo Gundams in the system to edit.\n")
                options(gundam_list, directory_path)
            else:
                print("\nSelect a Gundam to edit:")
                for idx, gundam in enumerate(gundam_list):
                    print(f"{idx + 1}. {gundam.name} ({gundam.model_number})")
                selected_index = int(input("Enter the number of the Gundam to edit: ")) - 1
                if 0 <= selected_index < len(gundam_list):
                    gundam_id = gundam_list[selected_index]
                else:
                    print("\nInvalid selection. Returning to main menu.\n")
                    options(gundam_list, directory_path)
                    return
            edit_gundam_info(gundam_id)
            options(gundam_list, directory_path)
        case '4':
            if gundam_list == []:
                print("\nNo Gundams in the system.\n")
            else:
                for gundam in gundam_list:
                    print(gundam.display_info())
            options(gundam_list, directory_path)
        case '5':
            print("\nExiting the system. Goodbye!")
            sys.exit(0)

def add_txt_to_list(gundam_list, directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    new_gundam = Gundam.convert_from_text(Gundam, content)
                    gundam_list.append(new_gundam)
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")

if __name__ == "__main__":
    main()
