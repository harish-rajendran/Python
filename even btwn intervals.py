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
    a = input("from:")
    b = input("Upto:")
    for x in range(a,b):
        if( x%2 == 0):
            print(x)


if __name__ == '__main__':
    main()
