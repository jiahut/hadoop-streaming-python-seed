#! /usr/bin/env python
#coding:utf-8

import sys

def read_input(file):
        for line in file:
            yield line.rstrip().split("\t")

def main():
        for items in read_input(sys.stdin):
            print("%s\t%s" %("_".join(items[0:2]), "_".join(items[2:])))

if __name__ == "__main__":
    main()
