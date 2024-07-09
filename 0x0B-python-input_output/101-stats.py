#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A Complex module/Script containing  functionalities
    that help Parses log

    Attributes:
        filesize: A necessary global variable
        statuscode: key, value map of status codes occurences
        from the total inputs
"""


from sys import stdin, stdout
import random
import time
import signal

# Global variables here
filesize = 0  #: int: A necessary global variable
statuscode = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}


# Function that generates (string) of the present status then prints
def printlog():
    """Prints to the standard output

    Args:
        filesize: The total file size
        statuscode: an array of status code
    """
    s = f"File size: {filesize}"
    for code in statuscode:
        if (sc := statuscode[code]) != 0:
            s += f"\n{code}: {sc}"
    print(s)


# handles the sigint ^C from the terminal/OS
def handler(signum, frame):
    """Handles signals sent from the OS

    Args:
        signum: the number representing the signal
        frame: The stack frame of the functions
    """
    printlog()


# Does the job of extracting necessary log value
def doYourJob():
    """These guy does the job of reading
    from the standard output and extracting the
    necessary value
    """
    i = 0
    global filesize
    for line in stdin:
        if len(line) > 1:
            le = line.split()
            try:
                filesize += int(le[-1])
                statuscode[le[-2]] += 1
            except Exception:
                continue
            i += 1
            if ((i % 10) == 0):
                printlog()
    # Prints log, if the loops stop at Non multiple of 10
    if (i % 10 or i == 0):
        printlog()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    doYourJob()
