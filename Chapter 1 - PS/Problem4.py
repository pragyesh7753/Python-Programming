import os

# Selecvt the directory whose content you want to list
# Specify the directory path; use '.' for the current directory
directory_path = '/Python-Programming'

try:
    # Get the list of all files and directories
    entries = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
