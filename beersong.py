word = "bottles"

for bottle_num in range(99, 0, -1):
    print(bottle_num, word, "of beer on the wall.")
    print(bottle_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")

    if bottle_num == 1:
        print("No bottles are on the wall.")
    else:
        new_num = bottle_num - 1

        if new_num == 1:
            word = " bottle"
        print(new_num, word, "of beer on the wall.")
        print()