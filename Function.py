def calculatesalary(h,r):
    if h>40:
        return ((40*r)+((h-40)*(r+r/4)))
    else:
        return h*r

hrs = input("Enter Hours:")
h=float(hrs)

rate = input("Enter Rate per hour:")
r=float(rate)

s = calculatesalary(h,r)
print("Salary is",s)

