#!/usr/bin/python
# -*- coding: utf-8 -*-

# ptr.szczepanski@gmail.com

import sys, yaml, pprint


# variables
file_path = sys.argv[1]


# functions
def readYaml(file_path):
    pprint.pprint(yaml.load(open(file_path).read()))


# main
def main():
    readYaml(file_path)

  
# run main
if __name__ == '__main__':
    main()
