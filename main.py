multi:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for elem in multi:
    for elem2 in multi:
        print(f"{elem} x {elem2} = {elem*elem2}")

        if elem2 == 9:
            print()

