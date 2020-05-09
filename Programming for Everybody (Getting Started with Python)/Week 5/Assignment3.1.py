#Enter inputs
hrs = input("Enter Hours:")
h = float(hrs)
rph = float(input("Enter rate per hour:"))
if h>40 :
    print(40*rph + (h-40)*1.5*rph)
else :
    print(h*rph)
