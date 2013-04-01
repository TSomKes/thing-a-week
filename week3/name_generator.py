#!/usr/bin/env python

import random


def GetRandomName(filename):
    """Return randomly-selected name from the given file"""

    with open(filename) as nameFile:
        return random.choice(nameFile.read().splitlines())


def GetName(gender):
    """Return randomly-assembled gender-appropriate name"""
    if gender == 'F':
        firstName = GetRandomName("first_female.txt")
    elif gender == 'M':
        firstName = GetRandomName("first_male.txt")
    else:
        firstName = "It's Pat"

    lastName = GetRandomName("last.txt")

    fullName = firstName + " " + lastName

    return gender + " " + fullName


for i in range(10):
    gender = random.choice(['F', 'M'])
    print GetName(gender)
