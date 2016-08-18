#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Admin
#
# Created:     17-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    s="Do I need to raise a seed round"
    #print set(s)
    dict = {}
    for i in set(s):
        b = s.count(i, 0, len(s))
        dict[i] = b
    print dict


if __name__ == '__main__':
    main()
