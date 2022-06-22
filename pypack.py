#!/usr/local/bin/python3.10
from sys import argv
from dataio.fetch import FetchAndInstall

commandList = {
    '-i' : FetchAndInstall,
    '--install' : FetchAndInstall
}

try:
    if argv[1] in commandList:
        commandList[argv[1]](argv[2])
    else:
        print("that is not a valid command.")
except IndexError:
    print("index error occured. have you put a base argument?")


