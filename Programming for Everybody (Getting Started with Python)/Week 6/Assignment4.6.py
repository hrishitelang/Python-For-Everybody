def computepay(h,r):
    if h<=40:
    	return h*r
    elif h>40:
        return (h*r + (h-40)*0.5*r)

hrs = float(input("Enter Hours:"))
rph = float(input("Enter Rate per hour:"))
p = computepay(hrs,rph)
print("Pay",p)
