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
    num1=input("enter the number 1: ")
    num2=input("enter the number 2: ")
    if(num1>num2):
        smaller=num2
    else:
        smaller=num1
    for x in range(2,smaller+1):
        if( (num1%x) == 0 and (num2%x) == 0):
            hcf=x

    print hcf

if __name__ == '__main__':
    main()
