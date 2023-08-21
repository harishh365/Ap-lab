import math
p=int(input("Enter Principal Amount:"))
r=int(input("Enter Rate of Interest:"))
t=int(input("Enter Time Period:"))
si=(p*r*t)/100
print("Simple Interest:",si)
amt=p*(1+r/100)**t
ci=amt-p
print("Compound Interest:",ci)