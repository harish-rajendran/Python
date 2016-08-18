#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      HARISH
#
# Created:     07-08-2016
# Copyright:   (c) Admin 2016
# Licence:
#-------------------------------------------------------------------------------

def prime():
    num = input("Enter the number : ")
    count=0
    if(num>1):
        if(num==2):
            print num
        else:
            for x in range(2,num):
                if(num%x == 0):
                    count+=1
                    break
            if(count==0):
                print num
            else:
                print "nott"


if __name__ == '__main__':
    prime()