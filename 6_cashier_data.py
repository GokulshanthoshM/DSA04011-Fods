import numpy as np

item_prices=[]
quantities=[]
item_size=int(input("Enter the size:"))
for price in range(item_size):
              a=int(input("Enter the item pize: "))
              b=int(input("Enter the quantity size: "))
              item_prices.append(a)
              quantities.append(b)


discount_rate=float(input("Enter the discount rate: "))
tax_rate=float(input("Enter the tax rate: "))

total=sum(item*quantity for item,quantity in zip(item_prices,quantities))

discount=total*(discount_rate/100)
after_discount=total-discount
tax=after_discount*(tax_rate/100)
final=after_discount+tax

print(f"Total after discount is {after_discount}")
print(f"Tax amount is {tax}")
print(f"Your total Bill is {final}")
    
