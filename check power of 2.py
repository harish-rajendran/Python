#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     08-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n=input()
    for i in range(2,n):
        if(i<n):
            j=2**i
            if(j==n):
                print("yes")
                break
    else:
        print("no")


if __name__ == '__main__':
    main()
