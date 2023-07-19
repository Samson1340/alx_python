for x in range(100):
    if x <= 9:
        print("0{},".format(x), end=' ')
    else:
        print("{},".format(x), end=' ')