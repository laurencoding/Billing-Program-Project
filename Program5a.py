# -------------------------------------------------------------------
# Author:   Lauren Canning
# Name:     Program 5a
#
# Description: 
# Reads record from Billing.txt file and produces a control report
# -------------------------------------------------------------------
from Module4 import *

def main():
    print("Employee	Rate\tweek 1\tweek 2\tweek 3\tweek 4\tHours\tTotal")
    
    try:
        record = open("Billing.txt","r")        

    except ValueError:
        resetBillingFile()

    billable_hours = 0
    billable_due = 0
    employee_name = readNextString(record)

    while employee_name != '':    
        hourly_rate = readNextFloat(record)
        
        hoursPerWeek = []
        for i in range(4):
            hoursPerWeek.append(readNextFloat(record))
        
        total_hours = sum(hoursPerWeek)
        
        amt_due = calcInvoiceTotal(hourly_rate,total_hours)
        billable_hours += total_hours
        billable_due += amt_due

        print("\n" + employee_name +"\t\t$"+ format(hourly_rate,',.2f') +"\t"+ \
            format(hoursPerWeek[0],',.2f') +"\t"+ format(hoursPerWeek[1],',.2f') +"\t"+ \
            format(hoursPerWeek[2],',.2f') +"\t"+ format(hoursPerWeek[3],',.2f') +"\t"+ \
            format(total_hours,',.2f') +"\t$"+ format(amt_due,',.2f'))

        employee_name = readNextString(record)

    record.close()

    avg_billable_hours = billable_due / billable_hours

    print("\n\nTotal Billable Due:\t$"+format(billable_due,',.2f')+ \
        "\nTotal Billable Hours:\t"+format(billable_hours,',.2f')+ \
        "\nAverage Billable Hours:\t"+format(avg_billable_hours,',.2f'))

