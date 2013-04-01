#!/usr/bin/env python

import argparse
import random


def ParseArguments():
    parser = argparse.ArgumentParser("./name_generator.py [OPTION]... [FILE]")

    parser.add_argument("-c",
            "--count",
            type=int,
            default=1,
            help="the number of names to be generated (default: %(default)s)")
    parser.add_argument("-g",
            "--gender",
            choices=['?', 'f', 'm'],
            default='?',
            help="the gender of the name(s) to be generated (default: %(default)s)")

    return parser.parse_args()


def GetRandomName(filename):
    """Return randomly-selected name from the given file"""

    with open(filename) as nameFile:
        return random.choice(nameFile.read().splitlines())


def GetName(gender):
    """Return randomly-assembled gender-appropriate name"""
    if gender == 'f':
        firstName = GetRandomName("first_female.txt")
    elif gender == 'm':
        firstName = GetRandomName("first_male.txt")
    else:
        firstName = "It's Pat"

    lastName = GetRandomName("last.txt")

    fullName = firstName + " " + lastName

    return gender + " " + fullName


args = ParseArguments()

gender = args.gender
count = args.count

for i in range(count):
    print GetName(gender)
