row = input("Enter the cell row name: ")
col = int(input("Enter the cell col name: "))
array_1 = {"A","C","E","G"}
array_2 = {"B","D","F","H"}
if row in array_1:
    if col in range(1,9):
        if col%2 == 0:
            print("White")
        else:
            print("Black")
elif row in array_2:
    if col in range(1,9):
        if col%2 == 0:
            print("Black")
        else:
            print("White")
else:
    print("Please enter the valid cell name.")