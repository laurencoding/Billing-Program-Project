# -------------------------------------------------------------------#
# Author:   Lauren Canning
# Name:     Program 6
#
# Description: 
# This Billing System menu program will allow the user to select an 
# option and execute the corresponding program. 
# -------------------------------------------------------------------#
import Program5, Program5a


def main():
    while True:
        print('Billing System Menu:\n')
        print('\t0 - end')
        print('\t1 - Enter billing data')
        print('\t2 - Display adhoc billing report')

        try:
            option = int(input('\nOption ==> '))

        except ValueError:
            print("Please enter an available option.")

        if option == 0:
            break

        elif option == 1:
            Program5.main()

        elif option == 2:
            Program5a.main()

        else:
            print("Please enter an available option.")

    print("Program ended successfully.")


main()
