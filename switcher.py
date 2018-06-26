# !/usr/bin/env python
import sys
import os
import argparse
import subprocess

# Globals
PHPINI = "/etc/apache2/"
FILEINI = "httpd.conf"

def main():
    #Relocate to correct directory
    changeDir()

def changeDir(dir=PHPINI):
    os.chdir(dir)
    # print(os.getcwd())

if __name__ == "__main__":
    sys.exit(main())