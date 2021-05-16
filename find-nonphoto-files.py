#!/usr/bin/python
# Find non-photo files in a directory and its all subdirectories
# References:
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
    print("Usage: python find-nonphoto-files.py [-d|--directory] <directory>")

def find_directory(directory, regex):
    count = 0
    print(f"{directory}", end="")
    for item in os.listdir(directory):
        abspath = os.path.join(directory, item)
        if os.path.isfile(abspath):
            filename, ext = os.path.splitext(item)
            if not regex.findall(ext):
                count += 1
    if count > 0:
        print(f"\t<-\t{bcolors.WARNING}{count} files found{bcolors.ENDC}")
    else:
        print()
    return count

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:", ["help", "directory="])
    except getopt.GetoptError as err:
        print(f"{bcolors.FAIL}Error: {err}{bcolors.ENDC}")
        print_usage()
        sys.exit(90)

    directory = ""

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory = os.path.abspath(arg)
    
    if not directory:
        print(f"{bcolors.FAIL}Error: directory is not specified.{bcolors.ENDC}")
        print_usage()
        sys.exit(91)
    if not os.path.exists(directory):
        print(f"{bcolors.FAIL}Error: '{directory}' does not exist.{bcolors.ENDC}")
        sys.exit(92)

    extensionRegex = re.compile(r'\.(jpg|jpeg|png)', re.IGNORECASE)
    for dirpath, dirnames, filenames in os.walk(directory):
        find_directory(dirpath, extensionRegex)

if __name__ == "__main__":
    main(sys.argv[1:])
