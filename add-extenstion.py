#!/usr/bin/python
# Add file extention
# References:
# - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# - https://docs.python.org/3/tutorial/errors.html
import os, sys, getopt, traceback

def print_usage():
    print("Usage: add-extension.py -h --help")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:", ["help", "directory="])
    except getopt.GetoptError as err:
        print("Error: {0}".format(err))
        print_usage()
        sys.exit(90)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory = os.path.abspath(arg)
    
    if not os.path.exists(directory):
        print("Error: '{0}' does not exist.".format(directory))
        sys.exit(91)
    os.chdir(directory)
    print('Working Directory: ' + directory)

    for item in os.listdir(directory):
        abspath = os.path.join(directory, item)
        if os.path.isfile(abspath):
            print(item)

if __name__ == "__main__":
    main(sys.argv[1:])
