
scrabble = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 'y', 4, 2, 4.3, 'z', 10, 1, 5.3]


letters = scrabble[0::4]
points = scrabble[1::4]
amounts = scrabble[2::4]
ratios = scrabble[3::4]


point_group = list(zip(points, letters))
point_group.sort(reverse=True)

amount_group = list(zip(amounts, letters))
amount_group.sort(reverse=True)

ratio_group = list(zip(ratios, letters))
ratio_group.sort()


print("The highest point in the scrabble game:")
print(f"    1) \"{point_group[0][1]}\" with {point_group[0][0]} points.")
print(f"    2) \"{point_group[1][1]}\" with {point_group[1][0]} points.")
print(f"    3) \"{point_group[2][1]}\" with {point_group[2][0]} points.")
print(f"    4) \"{point_group[3][1]}\" with {point_group[3][0]} points.")


print("The highest amount in the scrabble game:")
print(f"    1) \"{amount_group[0][1]}\" with {amount_group[0][0]} pieces.")
print(f"    2) \"{amount_group[1][1]}\" with {amount_group[1][0]} pieces.")
print(f"    3) \"{amount_group[2][1]}\" with {amount_group[2][0]} pieces.")
print(f"    4) \"{amount_group[3][1]}\" with {amount_group[3][0]} pieces.")

print("The lowest ratio in the scrabble game:")
print(f"    1) \"{ratio_group[0][1]}\" with {ratio_group[0][0]} percent.")
print(f"    2) \"{ratio_group[1][1]}\" with {ratio_group[1][0]} percent.")
print(f"    3) \"{ratio_group[2][1]}\" with {ratio_group[2][0]} percent.")
print(f"    4) \"{ratio_group[3][1]}\" with {ratio_group[3][0]} percent.")