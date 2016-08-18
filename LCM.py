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
    num1=input("enter the number: ")
    num2=input("enter the number: ")
    if(num1>num2):
        greater=num1
    else:
        greater=num2
    for x in range(2,num1*num2):
        if(x%num1==0 and x%num2==0):
            print x
            break


if __name__ == '__main__':
    main()
