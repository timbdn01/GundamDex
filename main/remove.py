import os

def remove_gundam(gundam_id, directory_path, gundam_list):
    gundam_list.remove(gundam_id)
    file_name = f"{gundam_id.name.replace(' ', '_')}.txt"
    file_path = os.path.join(directory_path, file_name)
    try:
        os.remove(file_path)
        print(f"Gundam {gundam_id.name} has been removed from the system.\n")
    except FileNotFoundError:
        print(f"File for Gundam {gundam_id.name} not found. It may have already been removed.\n")
    except Exception as e:
        print(f"Error removing Gundam data file: {e}\n")

def remove_all_gundams(directory_path, gundam_list):
    gundam_list.clear()
    try:
        for file_name in os.listdir(directory_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(directory_path, file_name)
                os.remove(file_path)
        print("All Gundam data files have been removed from the system.\n")
    except Exception as e:
        print(f"Error removing Gundam data files: {e}\n")