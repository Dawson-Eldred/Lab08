# This program hashes file directories
# Megan Reardon and Dawson Eldred
# SY402 - Lab8

import os

def main():

    # f = open("textfile.txt", "a")

    ignore = set(['dev', 'proc', 'run', 'sys', 'tmp', 'var/lib', 'var/run'])

    for root, dirs, files in os.walk("/"):
        dirs[:] = [d for d in dirs if d not in ignore]
        for filename in files:
            # f.write(os.path.join(root, filename))
            print(os.path.join(root, filename))
            print()
        for filename in dirs:
            # f.write(os.path.join(root,filename))
            print(os.path.join(root,filename))
            print()


    # f = open("textfile.txt", "r")

# used tutorialspoint.com/python/os_walk.htm for the code above
# used stackabuse.com/python-list-files-in-a-directory/ for the code above



main()
