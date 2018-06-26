# !/usr/bin/env python
import sys
import os
import argparse


# globalConsts
PHPINI = "/etc/apache2/"
FILEINI = "testhttpd.conf"


def main():
    #Relocate to correct directory
    changeDir()
    iniFile = readFile()


# Switch to correct directory of file
def changeDir(dir=PHPINI):
    os.chdir(dir)
    # print(os.getcwd())

#Read file into Memory
def readFile(iniFile=FILEINI):
    try:
        with open(iniFile, 'r') as file:
            iniFile = file.read()
            print(iniFile)
            return iniFile
    except Exception as ex:
        errorPrint(ex)

# Method to handle excepts
def errorPrint(ex):
    print("Error: ", ex)

if __name__ == "__main__":
    sys.exit(main())