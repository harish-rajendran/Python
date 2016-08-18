#-------------------------------------------------------------------------------
# Name:        module3
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
    c=raw_input("enter the character to be searched for")
    d=c.lower()
    e=c.upper()
    a=s.count(d)
    b=s.count(e)
    add=a+b
    print "the char is ",c
    print "no of times ",add

if __name__ == '__main__':
    main()
