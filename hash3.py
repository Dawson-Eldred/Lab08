# This program hashes file directories
# Megan Reardon and Dawson Eldred
# SY402 - Lab8

import os
import hashlib
from datetime import datetime
import csv
import time

def update(hashlist):

    # f = open("textfile.txt", "a")
    buffer = 65536
    ignore = set(['dev', 'proc', 'run', 'sys', 'tmp', 'var/lib', 'var/run', 'usr/src', 'usr/lib', 'usr/share'])
    sha2 = hashlib.sha256()

# Implementing step 4, running back through and re-hashing every file to compare hashes. Then printing changes
    for root, dirs, files in os.walk("/"):
        dirs[:] = [d for d in dirs if d not in ignore]
        for directories in dirs:
            path = os.path.join(root,directories)
        for filename in files:
            newpath2 = str(path) + "/" + str(filename)

   # used tutorialspoint.com/python/os_walk.htm for the code above
   # used stackabuse.com/python-list-files-in-a-directory/ for the code above
            try:
                with open(str(newpath2), 'rb') as f:
                    while True:
                        data = f.read(buffer)
                        if not data:
                            break
                        sha2.update(data)
                        hash2 = sha2.hexdigest()

                        if hash2 not in hashlist:
                            print("File:" + " " + str(newpath2) + " " + "is new or has changed")
                        else:
                            continue

# Implementing step 3 of the lab
                        currenttime = "{:%Y-%b-%d %H:%M:%S}".format(datetime.now())
                        with open('results_file.csv', mode='a+', newline='') as results_file:
                            results_writer = csv.writer(results_file, delimiter=',')

                            results_writer.writerow([str(newpath2),str(hash2),str(currenttime)])

            except:
                continue

   # f = open("textfile.txt", "r")

    return

def main():
    buffer = 65536
    ignore = set(['dev', 'proc', 'run', 'sys', 'tmp', 'var/lib', 'var/run', 'usr/src', 'usr/lib'])
    sha2 = hashlib.sha256()
    hashlist = []

# Implementing step 1 of the lab
    for root, dirs, files in os.walk("/"):
        dirs[:] = [d for d in dirs if d not in ignore]
        for directories in dirs:
            path = os.path.join(root,directories)
        for filename in files:
            newpath = str(path) + "/" + str(filename)
    # used tutorialspoint.com/python/os_walk.htm for the code above
    # used stackabuse.com/python-list-files-in-a-directory/ for the code above

 # Implementing step 2 of the lab
            try:
                with open(str(newpath), 'rb') as f:
                    while True:
                        data = f.read(buffer)
                        if not data:
                            break
                        sha2.update(data)
                        hash = sha2.hexdigest()
                        hashlist.append(hash)
                        # print(hash)

            except:
                continue
            # used stackoverflow.com/questions/22058048/hashing-a-file-in-python for the above code
            # print(os.path.join(root, filename))

# Code below puts the program to sleep to allow for any file changes - mostly testing purposes
    print("Program will now sleep to allow changes to files to be made")
    time.sleep(10)
    update(hashlist)

main()
