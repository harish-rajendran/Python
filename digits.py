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
    n=input("enter the number")
    count=0
    while(n>0):
        n=n/10
        count+=1
    print "number of integer is",count
if __name__ == '__main__':
    main()
