from edit_view import *
from creation import *
from argparse import ArgumentParser
import sys

def parse_args():



    parser = ArgumentParser()

    parser.add_argument('-students', '-s', type = str, help = "students table")
    parser.add_argument('-professors', '-p', type = str, help = "professors table")
    parser.add_argument('-degrees','-d', type = str, help = "degrees table")
    parser.add_argument('-classes','-c', type = str, help = 'classes table') 

    args = parser.parse_args()

    return args



if __name__ == "__main__":
    try:
        args = parse_args()
    except ValueError as e:
        sys.exit(str(e))
        

    if args.students and args.professors and args.degrees and args.classes:
        args_list = [args.students, args.professors, args.degrees, args.classes]
        menu(args_list)
    elif args.students or args.professors or args.degrees or args.classes:
        sys.exit("Error, you are missing a file. \nIf you wish to enter Edit/View Mode, please provide 4 files (students, professors, degrees, classes)\nIf you need to create a database, simply run the program with no arguments")
    else:
        create()