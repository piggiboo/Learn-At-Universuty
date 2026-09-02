A = ((1, 3, 5),
     (2, 4, 6),)

AT = tuple(zip(*A))

AAT = tuple(
    tuple(sum(x * y for x, y in zip(row_a, col_b)) for col_b in zip(*AT))
    for row_a in A
)

print("*"*100)
print(f"{'Matrix with Tuple':^100}")
print("*"*100)

a11_1 = input("Enter row number of 'A' matrix : ")
a11_2 = input("Enter column number of 'A' matrix : ")
print (f"The 'a11' element in the 'A' matrix is {A[int(a11_1) - 1][int(a11_2) - 1]}")
print("-"*100)

b11_1 = input("Enter row number of the transpose of 'A' matrix : ") 
b11_2 = input("Enter column number of the transpose of 'A' matrix : ")
print (f"The 'b11' element in the transpose of the 'A' matrix is {AT[int(b11_1) - 1][int(b11_2) - 1]}")
print("-"*100)
  
c11_1 = input("Enter row number of the multiplication of matrices 'A' and transpose of 'A' :")
c11_2 = input("Enter column number of the multiplication of matrices 'A' and transpose of 'A' :")
print (f"The 'c11' element in the multiplication of matrices 'A' and transpose of 'A' is {AAT[int(c11_1) - 1][int(c11_2) - 1]}")
print("-"*100)