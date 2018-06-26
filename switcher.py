# !/usr/bin/env python
import sys
import os


# globalConsts
CONFDIR = "/etc/apache2/"
CONFFILE = "testhttpd.conf"


def main():
    #Relocate to correct directory
    changeDir()
    confFile = readFile()
    switcher(confFile)


# Find and update version in php.ini
def switcher(confFile):
    print("Starting Values")
    print(confFile[175])
    print(confFile[176])
    if '#' not in confFile[175]:
        confFile[175] = "#" + confFile[175]
        confFile[176] = confFile[176][1:]
    else:
        confFile[175] = confFile[175][1:]
        confFile[176] = "#" + confFile[176]
    print("Ending Values")
    print(confFile[175])
    print(confFile[176])
    


# Switch to correct directory of file
def changeDir(dir=CONFDIR):
    os.chdir(dir)
    # print(os.getcwd())


#Read file into Memory
def readFile(confFile=CONFFILE):
    try:
        with open(confFile, 'r') as file:
            file = file.read().splitlines()
            return file
    except Exception as ex:
        errorPrint(ex)


# Method to handle excepts
def errorPrint(ex):
    print("Error: ", ex)

if __name__ == "__main__":
    sys.exit(main())