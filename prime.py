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
    num = input("Enter a number : ")
    count = 0
    if(num > 1):
        if(num == 2):
            print num,"is a prime number"
        else:
            for i in range(2,num):
                if((num%i) == 0):
                    count += 1

            if(count == 0):
                print num," is a prime number."
            else:
                print num," is not a prime number."
    else:
        print num," is not a prime number"

if __name__ == '__main__':
    main()
