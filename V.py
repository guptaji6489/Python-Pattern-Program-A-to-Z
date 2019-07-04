for row in range(5):
    for col in range(9):    
        if (col==row) or (row==0 and col==8) or (row==1 and col==7) or  (row==2 and col==6) or  (row==3 and col==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
