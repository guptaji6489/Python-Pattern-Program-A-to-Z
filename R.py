for row in range(7):
    for col in range(7):    
        if (col==0 or (col==6 and row<3)) or (row==0 or row==3) or (row==col and row>3):
            print("*",end="")
        else:
            print(end=" ")
    print()
