# This program hashes file directories
# Megan Reardon and Dawson Eldred
# SY402 - Lab8

import os

def main():
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)

main()
