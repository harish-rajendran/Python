#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     06-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    num=raw_input("enter the number:")
    rev=num.split()
    print num
    l=len(rev)
    a=l-1
    c=[]
    for x in range(a,-1,-1):
        c+=rev[x]
    d="".join(c)
    print d
    if(num==d):
        print "the number is palindrome"
    else:
        print "the number is not palindrome"

if __name__ == '__main__':
    main()
