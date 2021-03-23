# This program hashes file directories
# Megan Reardon and Dawson Eldred
# SY402 - Lab8

import os
import hashlib

def main():

    # f = open("textfile.txt", "a")
    buffer = 65536
    ignore = set(['dev', 'proc', 'run', 'sys', 'tmp', 'var/lib', 'var/run', 'usr/src', 'usr/lib'])
    sha2 = hashlib.sha256()

    for root, dirs, files in os.walk("/"):
        dirs[:] = [d for d in dirs if d not in ignore]
        for directories in dirs:
            path = os.path.join(root,directories)

        for filename in files:
            newpath = str(path) + "/" + str(filename)
    # used tutorialspoint.com/python/os_walk.htm for the code above
    # used stackabuse.com/python-list-files-in-a-directory/ for the code above

            # print(newpath)

            try:
                with open(str(newpath), 'rb') as f:
                    while True:
                        data = f.read(buffer)
                        if not data:
                            break
                        sha2.update(data)
                        print("Sha2: {0}".format(sha2.hexdigest()))
            except:
                continue
            # used stackoverflow.com/questions/22058048/hashing-a-file-in-python for the above code
            # print(os.path.join(root, filename))


    # f = open("textfile.txt", "r")




main()
