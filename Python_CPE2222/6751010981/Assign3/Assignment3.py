item1 = str(input("Enter The 1st Product Name :"))
price1 = float(input("Enter Price of Product :"))
quantity1 = int(input("Enter Quantity of Product :"))

item2 = str(input("Enter The 2nd Product Name :"))
price2 = float(input("Enter Price of Product :"))
quantity2 = int(input("Enter Quantity of Product :"))

item3 = str(input("Enter The 3rd Product Name :"))
price3 = float(input("Enter Price of Product :"))
quantity3 = int(input("Enter Quantity of Product :"))

print ("-"*50)
print (f"{'Inventory':^50}")
print ("-"*50)

print (f"{'Item':^30}{'Price':<10}{'Quantity':<10}")
print ("-"*50)

print (f"{item1:<30}{price1:<10}{quantity1:>10}")
print (f"{item2:<30}{price2:<10.2f}{quantity2:>10}")
print (f"{item3:<30}{price3:<10.2f}{quantity3:>10}")
print ("-"*50)
total_quantity = quantity1 + quantity2 + quantity3
msg = f"Total Quantity = {total_quantity}"
print (f"{msg:>50}")
print ("-"*50)