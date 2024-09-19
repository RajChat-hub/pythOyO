#!/usr/bin/python3
import os
import pythoyo
import sys  # Import sys to handle exit

def start_shell():
    while True:
        text = input("(｡･ÿ･｡)ﾉ★ > ")
        if text.strip() == "cyear":
            os.system('clear' if os.name == 'posix' else 'cls')
            continue
        if text.strip() == "exyit()":  # Add the exyit() function to exit the shell
            print("Exiting pythOyO shell.")
            sys.exit()  # Exit the shell
        if text.strip() == "":
            continue
        result, error = pythoyo.run("<stdin>", text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))

if __name__ == "__main__":
    start_shell()
