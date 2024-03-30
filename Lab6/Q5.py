while True:
    # (a) Ask the user for the file name, handle bad file name
    file_str = input("Open what file: ")

    try:
        with open(file_str, 'r') as input_file:
            while True:
                # (c) Ask for a line number, handle ValueError
                find_line_str = input("Which line (integer): ")
                try:
                    find_line_int = int(find_line_str)  # Convert input to an integer
                    line_count_int = 1

                    for line_str in input_file:
                        if line_count_int == find_line_int:
                            reversed_line = line_str[::-1]  # Reverse the line
                            print("Line {} of file {} is: {}".format(find_line_int, file_str, reversed_line))
                            break
                        line_count_int += 1
                    else:
                        # This block executes if the for loop completes without a 'break'
                        print("Line {} of file {} not found".format(find_line_int, file_str))
                        break  # Exit the inner loop

                except ValueError:
                    print("Invalid input. Please enter a valid integer for the line number.")

    except FileNotFoundError:
        # (b) Handle IOError (FileNotFoundError) and ask for input again
        print("The file", file_str, "doesn't exist.")

    user_input = input("Do you want to open another file? (y/n): ")
    if user_input.lower() != 'y':
        break

# End of the program
print("End of the program")
