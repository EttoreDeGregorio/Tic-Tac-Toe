import os

arr = [" "] * 9
moves = [""] * 9
pos = [1, 5, 9]

def board():
    os.system("clear")
    c = 0

    for i in range(11):
        if i == 3 or i == 7:
            print ("------+-------+------")
        
        else:
            for j in range(11):
                if j == 3 or j == 7:
                    print("|",  end = " ")

                elif i in pos and j in pos:
                    print(arr[c], end = " ")
                    c += 1
                
                elif j == 10:
                    print (" ")

                else:
                    print (" ", end = " ")
    #print(arr)
    #print(moves)

def move():
    for i in range(len(moves) + 1):
        con = 0
        board()
        if i < 9:
            if i == 0 or i % 2 == 0:
                while con == 0:
                    x = int(input("\nInserisci la posizione di X: "))
                    if x > 9:
                        print("\nValore non valido")
                    
                    else:
                        if x in moves:
                            print("\nPosizione Occupata")

                        else:
                            arr[x - 1] = "X"
                            con = 1

            else:
                 while con == 0:
                    x = int(input("\nInserisci la posizione di O: "))
                    if x > 9:
                        print("\nValore non valido")
                    
                    else:
                        if x in moves:
                            print("\nPosizione Occupata")

                        else:
                            arr[x - 1] = "O"
                            con = 1

            moves[int(i)] = x
            
            if i >= 4:
                win(check_win())

        else:
            print("\n\n------ DRAW ------\n\n")

def check_win():
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[0] == arr[2]:
        return arr[0]
    
    elif arr[3] == arr[4] and arr[4] == arr[5] and arr[3] == arr[5]:
        return arr[3]
    
    elif arr[6] == arr[7] and arr[7] == arr[8] and arr[6] == arr[8]:
        return arr[6]

    elif arr[0] == arr[3] and arr[3] == arr[6] and arr[0] == arr[6]:
        return arr[0]
    
    elif arr[1] == arr[4] and arr[4] == arr[7] and arr[1] == arr[7]:
        return arr[1]

    elif arr[2] == arr[5] and arr[5] == arr[8] and arr[2] == arr[8]:
        return arr[2]
    
    elif arr[0] == arr[4] and arr[4] == arr[8] and arr[0] == arr[8]:
        return arr[0]

    elif arr[2] == arr[4] and arr[4] == arr[6] and arr[2] == arr[6]:
        return arr[2]
    
    else:
        pass

def win(x):
    board()

    if x == "X":
        print("\n\n ------ X WINS ------ \n\n")
        exit()

    elif x == "O":
        print("\n\n ------ O WINS ------ \n\n")
        exit()

    else:
        pass

def main():
    move()

if __name__ == "__main__":
    main()