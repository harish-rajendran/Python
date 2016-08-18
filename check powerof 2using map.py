#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Admin
#
# Created:     08-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    num=input()
    squares = list(map(lambda x: 2**x, range(num)))
    try:
        b=squares.index(num)
        if(squares[b]==num):
            print("its a square of 2 ")
    except ValueError:
        print "no its not a square of 2"




if __name__ == '__main__':
    main()
