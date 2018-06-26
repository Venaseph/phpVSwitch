# !/usr/bin/env python
import sys
import os


# globalConsts
CONFDIR = "/etc/apache2/"
CONFFILE = "testhttpd.conf"


def main():
    #Relocate to correct directory
    changeDir()

    # Read in current httpd.conf file
    confFile = readFile()

    # Adjust list to reflect correct PHP Version
    switcher(confFile)

    # Write-to file
    writeFile(confFile)


# Write-to httpd.conf
def writeFile(confFile):
    pass



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
    try:
        os.chdir(dir)
    except Exception as ex:
        errorPrint(ex)


# Read file into Memory
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