#!/usr/bin/python3
import sys  # To handle command-line arguments
import pythoyo  # Import your interpreter module (assuming pythoyo is the main part of your interpreter)

# Function to run .pyoyo files
def run_pyoyo_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
        result, error = pythoyo.run(filename, code)  # Assuming your interpreter has a run() function
        
        if error:
            print(error.as_string())  # Display the error if any
        elif result:
            print(result)  # Output the result if no error

# Main function to check if a .pyoyo file is passed as a command-line argument
def main():
    if len(sys.argv) > 1:
        # If a file is passed as an argument, run it
        filename = sys.argv[1]
        if filename.endswith('.pyoyo'):
            run_pyoyo_file(filename)
        else:
            print(f"Error: {filename} is not a valid .pyoyo file.")
    else:
        # If no file is passed, run the interpreter interactively
        print("Starting pythOyO interactive shell...")
        # Call the function to start your interactive shell
        # Assuming the interactive shell part exists in your code
        start_shell()  # Adjust this based on how your shell is invoked in your interpreter

if __name__ == "__main__":
    main()
