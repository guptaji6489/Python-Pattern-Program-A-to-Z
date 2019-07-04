for row in range(8):
    for col in range(7):    
        if (col==0 or col==6) or (row==0 or row==6) or (row==7 and col==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
