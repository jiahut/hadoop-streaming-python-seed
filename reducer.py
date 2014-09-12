#!/usr/bin/env python
#coding:utf-8

from itertools import groupby
from operator import itemgetter
import sys
import re

# fix the encode
reload(sys)
sys.setdefaultencoding("utf-8")


re_zh = re.compile(u"[\u4e00-\u9fa5]+")

def test_zh(s):
    return re_zh.match(s)

def read_mapper_output(file):
	for line in file:
		yield line.rstrip().split("\t", 1)

def main():
	data = read_mapper_output(sys.stdin)

	for mid_pid, group in groupby(data, itemgetter(0)):
		try:
                        items = [item.decode("utf-8") for _,item in group ]
                        if len(items) == 2:
                            first, second = items
                            if test_zh(first) and not test_zh(second):
                                sorted_items = [first, second]
                                elems = [ elem for item in sorted_items for elem in item.split("_") ]
                                elems_str = "\t".join(elems)
                                print("%s\t%s" % ( "\t".join(mid_pid.split("_")), elems_str))
                            elif test_zh(second) and not test_zh(first):
                                sorted_items = [second, first]
                                elems = [ elem for item in sorted_items for elem in item.split("_") ]
                                elems_str = "\t".join(elems)
                                print("%s\t%s" % ( "\t".join(mid_pid.split("_")), elems_str))

		except:
                    pass

if __name__ == '__main__':
	main()
