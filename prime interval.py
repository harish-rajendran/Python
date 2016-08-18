#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     07-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    num = input("Enter a number : ")
    num1= input("Enter a number : ")
    for x in range (num,num1):
        count=0
        for i in range(2,x):
                if(x%i ==  0):
                    count=1
                    break
        if(count==0):
            print x


if __name__ == '__main__':
    main()