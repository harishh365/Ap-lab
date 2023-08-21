quantity=int(input("Enter Quantity sold:"))
item=float(input("Enter price of per item:"))
disc=float(input("Enter Discount %:"))
tax=float(input("Enter Tax %:"))
amount=quantity*item
discount=amount*(disc/100)
finalAmount=amount-discount
tax_price=(tax/100)*finalAmount
bill=finalAmount+tax_price
print("Bill Amount:",bill)