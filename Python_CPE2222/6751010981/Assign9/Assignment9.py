while True:
    size = int(input("Please enter the size: "))
    if size !=0:
        print("#" * size)
        for i in range(size - 2):
            print("#" + " " * (size - 2) + "#")
        print("#" * size)

    elif size == 0:
        break
