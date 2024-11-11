def read_and_modify_file(input_filename, output_filename):
    try:
        # Read the contents of the input file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (example: converting to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Successfully written modified content to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written to.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask user for the input and output filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the file to write the modified content to: ")

# Run the function
read_and_modify_file(input_filename, output_filename)