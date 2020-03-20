# -------------------------------------------------------------------
# Author:   Lauren Canning
# Name:     Program 5
#
# Description: 
# Input billing information for employee for invoice output and
# ask if you want to input another employee. It will also create a file
# called Billing.txt to hold the billing record.
# -------------------------------------------------------------------
from Module4 import *

def main():
    resetBillingFile()

    another = 'y'
    while another == 'y':
        
        hoursPerWeek = []
        for i in range(4):
           hoursPerWeek.append(readWeeklyHours(i+1))
        total_hours = sum(hoursPerWeek)

        avg_hours = float(total_hours/4)

        hourly_rate = readHourlyRate()
        employee_name = readEmployeeName()
        amt_due = calcInvoiceTotal(hourly_rate,total_hours)
        
        if total_hours <= 160:
            print("\n\n"+employee_name+" worked no overtime.\n\nInvoice"+ \
                "\nResource: "+employee_name+"\t\tAverage weekly hours: "+format(avg_hours,',.2f'))

            print("\nTotal billable hours: "+format(total_hours,',.2f')+ \
                "\trate: $"+format(hourly_rate,',.2f'))
            print("Regular Hours:"+format(total_hours,',.2f'),"@ $"+format(hourly_rate,',.2f')+ \
                "\t= $"+format(amt_due,',.2f'))
            print("Amount Due: $"+format(amt_due,',.2f')+"\n")

        else:
            overtime_hours = total_hours - 160
            overtime_rate  = hourly_rate * 1.05
            overtime_pay   = overtime_hours * overtime_rate
            regular_pay    = 160 * hourly_rate

            print("\n\n"+employee_name,"worked",overtime_hours,"hours of overtime.\n\nInvoice"+ \
                "\nResource:"+employee_name+"\t\tAverage weekly hours: "+format(avg_hours,',.2f'))

            print("\nTotal billable hours: "+format(total_hours,',.2f')+ \
                "\trate: $"+format(hourly_rate,',.2f'))
            print("Overtime Hours: "+format(overtime_hours,',.2f'),"@ $"+format(overtime_rate,',.2f')+ \
                "\t= $"+format(overtime_pay,',.2f'))
            print("Regular Hours: 160 @ $"+format(hourly_rate,',.2f')+ \
                "\t= $"+format(regular_pay,',.2f'))
            print("Amount Due: $"+format(amt_due,',.2f')+"\n")

        writeBillingRecord(employee_name,hourly_rate,hoursPerWeek)

        another = input("Enter another employee? ('y'= yes): ")
        if another == 'y' or another == 'Y':
            continue
        else:
            break

    print("\nProgram ended normally.")

