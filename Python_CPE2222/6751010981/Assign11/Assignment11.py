print("Making a list of Factorial series of n")
n = int(input("Enter 'n' of Factorial number: "))
flist = []
sum = 1
for i in range(1, n + 1):
    sum *= i
    flist.append(sum)
print(f"A list of Factorial series of {n} is {flist}")