print("\nWELCOME TO PAY CALCULATOR") # to check that it is working

hours = float (input("\nEnter hours per week: "))
rate = float (input("Enter rate per hour: "))
pay = hours * rate 
print ("\nThis is your pay per week:", pay)

# I could alternatively remove
# float above and instead set pay = float(hours) * float(rate)
