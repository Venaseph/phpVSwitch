#! /usr/bin/env python
import sys
import os
import time
import subprocess as sp
import webbrowser as wb


# globalConsts
CONFDIR = "/etc/apache2/"
CONFFILE = "httpd.conf"


def main():
    #Relocate to correct directory
    changeDir()
    # Read in current httpd.conf file
    confFile = readFile()
    # Adjust list to reflect correct PHP Version
    switcher(confFile)
    # Write-to file
    writeFile(confFile) 
    # Restart Apache
    restartApache()
    # Open info PHP to confirm
    openPhpInfo()


def openPhpInfo():
    wb.open_new('http://localhost/info.php')


#restarts Apache
def restartApache():
    try:
        # Restart command, check_call does not always wait long enough on the restart
        sp.check_call("sudo apachectl restart".split())
        # Added time to offset it
        time.sleep(2)
        print("Apache Restarted")
    except Exception as ex:
        errorPrint(ex)

# Write-to httpd.conf
def writeFile(confFile):
    # Currently needs to be run sudo due to permissions, could subprocess it out I think if nes down the road
    with open(CONFFILE, 'w') as file:
        file.writelines(l for l in confFile)

# Find and update version in php.ini
def switcher(confFile):
    if '#' not in confFile[175]:
        confFile[175] = "#" + confFile[175]
        confFile[176] = confFile[176][1:]
    else:
        confFile[175] = confFile[175][1:]
        confFile[176] = "#" + confFile[176]


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
            file = file.readlines()
            return file
    except Exception as ex:
        errorPrint(ex)


# Method to handle excepts
def errorPrint(ex):
    print("Error: ", ex)

if __name__ == "__main__":
    sys.exit(main())