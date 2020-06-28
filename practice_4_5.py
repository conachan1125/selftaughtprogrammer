def cast_float():
    try:
        str = input("enter a number:")
        print(float(str))
    except ValueError:
        print("invalid input.")

cast_float()
