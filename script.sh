import subprocess
import sys
import platform
import os

class CPPShell:
    def __init__(self):
        self.version = "C++ 17"
        self.compiler = "GCC 11.4.0"
        self.prompt = ">>> "
    
    def display_startup_message(self):
        print(f"CPP-Shell (version: {self.version})")
        print(f"{platform.system()} {platform.release()} (using {self.compiler})")
        print('Type "help", "credits", or "exit" for more information.')

    def run_cpp_file(self, filename):
        compile_command = f"g++ {filename} -o temp_program"
        run_command = "./temp_program"

        try:
            # Compile the C++ file
            compile_result = subprocess.run(compile_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(compile_result.stdout.decode())

            # Run the compiled program
            run_result = subprocess.run(run_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(run_result.stdout.decode())

        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr.decode())

    def run_shell_script(self, filename):
        try:
            run_command = f"bash {filename}"
            run_result = subprocess.run(run_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(run_result.stdout.decode())
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr.decode())

    def start(self):
        self.display_startup_message()
        while True:
            try:
                command = input(self.prompt)

                if command.lower() == "help":
                    print("Welcome to CPP-Shell. You can run C++ files or shell scripts here.")
                    print("Commands: help, exit, run <filename.cpp>, runscript <filename.sh>")
                elif command.lower() == "exit":
                    print("Exiting CPP-Shell.")
                    break
                elif command.startswith("run "):
                    filename = command.split(" ")[1]
                    if filename.endswith(".cpp"):
                        self.run_cpp_file(filename)
                    else:
                        print("Please provide a C++ file (.cpp).")
                elif command.startswith("runscript "):
                    filename = command.split(" ")[1]
                    if filename.endswith(".sh"):
                        self.run_shell_script(filename)
                    else:
                        print("Please provide a shell script file (.sh).")
                else:
                    print("Unknown command. Type 'help' for a list of commands.")

            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    shell = CPPShell()
    shell.start()
