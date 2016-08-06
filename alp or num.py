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
     c = raw_input("Enter a character:")
     if(c.isalpha() == True):
        print("The character is an alphabet")
     elif(c.isalnum() == True):
        print("The character is a number")
     else:
        print("It is neither an alphabet nor a number")

if __name__ == '__main__':
    main()
