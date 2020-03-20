# ------------------------------------------------------------------------------
# Author:   Lauren Canning
# Name:     Module 4
#
# Description: 
# Functions for reading weekly hours, rate, name, calculating invoice
# total, and the billing file.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# readWeeklyHours - Accepts input from user for hours worked.
# ------------------------------------------------------------------------------
def readWeeklyHours(week):
    hours = 0
    while hours < 35 or hours > 80:
        try:
            hours = float(input('Enter hours worked for week '+str(week)+': '))
        except ValueError: 
            print("Invalid number of hours, must be between 35 and 80.\n")
            continue
        if hours < 35 or hours > 80:
            print("Invalid number of hours, must be between 35 and 80.\n")
            continue
    return float(hours)

# ------------------------------------------------------------------------------
# readHourlyRate - Accepts input from user for hourly paid rate.
# ------------------------------------------------------------------------------
def readHourlyRate():
    hourly_rate = 0.00
    while hourly_rate < 20.00:
        try:
            hourly_rate = float(input('Hourly Rate: '))
        except ValueError:
            print("Invalid Hourly Rate, must be at least $20.00/hour.\n")
            continue
        if hourly_rate < 20.00:
            print("Invalid Hourly Rate, must be at least $20.00/hour.\n")
            continue
    return float(hourly_rate)

# ------------------------------------------------------------------------------
# readEmployeeName - Accepts employee name.
# ------------------------------------------------------------------------------
def readEmployeeName():
    employee_name = ''
    while employee_name == '':
        employee_name = (input('Employee Name: '))
        if employee_name == '':
            print("Employee name must be entered.\n")
            continue
    return str(employee_name)

# ------------------------------------------------------------------------------
# calcInvoiceTotal - Calculates the invoice total due for employee pay.
# ------------------------------------------------------------------------------
def calcInvoiceTotal(hourly_rate,total_hours):
    if total_hours > 160:
        amt_due = (total_hours-160)*(hourly_rate*1.05) + (160*hourly_rate)
    else:
        amt_due = hourly_rate * total_hours
    return amt_due

# ------------------------------------------------------------------------------
# resetBillingFile - Resets (or creates) the billing record file.
# ------------------------------------------------------------------------------
def resetBillingFile():
    billing = open("Billing.txt","w")
    billing.close()

# ------------------------------------------------------------------------------
# writeBillingRecord - Creates billing record file with new information.
# ------------------------------------------------------------------------------
def writeBillingRecord(employee_name,hourly_rate,hoursPerWeek):
    billing = open("Billing.txt",'a')

    billing.write(employee_name+"\n"+str(hourly_rate)+"\n"+ \
        str(hoursPerWeek[0])+"\n"+str(hoursPerWeek[1])+"\n"+ \
        str(hoursPerWeek[2])+"\n"+str(hoursPerWeek[3])+"\n")
    billing.close()
            
# ------------------------------------------------------------------------------
# readNextString - Reads next line of record as a string.
# ------------------------------------------------------------------------------
def readNextString(record):
    inFile = record.readline().rstrip('\n')
    return inFile

# ------------------------------------------------------------------------------
# readNextFloat - Reads next line of record as a float.
# ------------------------------------------------------------------------------
def readNextFloat(record):
    inFile = float(readNextString(record))
    return inFile
