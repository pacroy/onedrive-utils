#!/usr/bin/python
# Add file extention
# References:
# - [Python - Command Line Arguments - Tutorialspoint](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
# - [8. Errors and Exceptions — Python 3.9.5 documentation](https://docs.python.org/3/tutorial/errors.html)
# - [regex - Using endswith with case insensivity in python - Stack Overflow](https://stackoverflow.com/questions/45637600/using-endswith-with-case-insensivity-in-python)
# - [Extracting extension from filename in Python - Stack Overflow](https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python)
# - [python - How to print colored text to the terminal? - Stack Overflow](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal)
# - [python - How to check if the string is empty? - Stack Overflow](https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty)
# - [python - How do I check if a variable exists? - Stack Overflow](https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists)
import os, sys, getopt, re, shutil, pyperclip

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_usage():
    print("Usage:")
    print("  python add-extension.py [-d directory] [-e extension] [--dry-run]")
    print()
    print("Arguments:")
    print("  -d, --directory directory : Specify a directory to scan for files. Omit to use the value from the clipboard.")
    print("  -e, --extension string    : Specify an extension string to append to the filename. Omit to use 'jpg'.")
    print("      --dry-run             : Run the program without making any change.")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:e:", ["help", "directory=", "extension=", "dry-run"])
    except getopt.GetoptError as err:
        print(f"{bcolors.FAIL}Error: {err}{bcolors.ENDC}")
        print_usage()
        sys.exit(90)

    directory = ""
    extension = ""
    dry_run = False

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory = os.path.abspath(arg)
        elif opt in ("-e", "--extension"):
            extension = arg
        elif opt == "--dry-run":
            dry_run = True
    
    if not directory:
        directory = pyperclip.paste()
    if not directory:
        print(f"{bcolors.FAIL}Error: directory is not specified.{bcolors.ENDC}")
        print_usage()
        sys.exit(91)
    if not os.path.exists(directory):
        print(f"{bcolors.FAIL}Error: '{directory}' does not exist.{bcolors.ENDC}")
        sys.exit(92)
    if not extension:
        extension = "jpg"

    print('Directory: ' + directory)

    extensionRegex = re.compile(r'\.(jpg|jpeg|png|mp4|mov)', re.IGNORECASE)

    for item in os.listdir(directory):
        abspath = os.path.join(directory, item)
        if os.path.isfile(abspath):
            print(item, end="")
            filename, ext = os.path.splitext(item)
            if not extensionRegex.findall(ext):
                newname = item + f".{extension}"
                newabspath = os.path.join(directory, newname)
                print(f"{bcolors.WARNING}\t->\t{newname}{bcolors.ENDC}")
                if not dry_run:
                    shutil.move(abspath, newabspath)
            else:
                print()

if __name__ == "__main__":
    main(sys.argv[1:])
