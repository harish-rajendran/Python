#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Admin
#
# Created:     06-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a="harish the boss"
    l=len(a)
    b=l-1
    c=[]
    for x in range (b,-1,-1):
       c+=a[x]
    print c
    result=" ".join(c)
    print result
if __name__ == '__main__':
    main()
