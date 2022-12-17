import sys
import os.path
from os import path
import argparse

def dir_path(pathName):
    if os.path.isdir(pathName):
        return pathName
    else:
        raise NotADirectoryError(pathName)

parser = argparse.ArgumentParser(
    description='COR AL PIT is a program that given images determine if your heart is healthy or not.',
    epilog="Example of use: python .\main.py -p 'your_path'")

parser.add_argument('-p','--path', type=dir_path, help= "the path with the videos")

def parse():
    return parser.parse_args()

def usage_help():
    return parser.print_help()

def main(path):
    print(path)


if __name__ == '__main__':
    if(len(sys.argv) == 3):
        parse()
        main("XD")

    else: 
        usage_help()

