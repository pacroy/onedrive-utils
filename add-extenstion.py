#!/usr/bin/python
# Add file extention
# References:
# - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# - https://docs.python.org/3/tutorial/errors.html
import os, sys, getopt, re, shutil

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
    print("Usage: add-extension.py [-d|--directory] <directory> [-e|--extension] <extension>")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:e:", ["help", "directory=", "extension=", "dry-run"])
    except getopt.GetoptError as err:
        print(f"{bcolors.FAIL}Error: {err}{bcolors.ENDC}")
        print_usage()
        sys.exit(90)

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
    
    if "directory" not in locals() or not directory:
        print(f"{bcolors.FAIL}Error: directory is not specified.{bcolors.ENDC}")
        print_usage()
        sys.exit(91)
    if not os.path.exists(directory):
        print(f"{bcolors.FAIL}Error: '{directory}' does not exist.{bcolors.ENDC}")
        sys.exit(92)
    if "extension" not in locals() or not extension:
        print(f"{bcolors.FAIL}Error: extension is not specified.{bcolors.ENDC}")
        print_usage()
        sys.exit(93)

    os.chdir(directory)
    print('Working Directory: ' + directory)

    extensionRegex = re.compile(r'\.(jpg|jpeg|png)', re.IGNORECASE)

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

if __name__ == "__main__":
    main(sys.argv[1:])
