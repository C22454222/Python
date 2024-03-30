def prompt_open(mode):
    while True:
        try:
            file_name = input("Enter a file name: ")
            file_handle = open(file_name, mode)
            print(f"File '{file_name}' found.")
            return file_handle
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Please enter a valid file name.")
        except PermissionError:
            print(f"You don't have permission to {mode} this file. Please choose another file.")

# Example usage:
file_mode = 'r'  # You can change this to 'w' if you want to open the file in write mode
file_handle = prompt_open(file_mode)

# You can now work with the file using the file_handle, e.g., read or write data.
