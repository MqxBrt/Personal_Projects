global grid
global fullColumns
grid = []
fullColumns = []

def fillGrid() :
    for i in range (6) :
        grid.append([])
        for j in range (7) :
            grid[i].append(" ")

def displayGrid() :
    print("|1|2|3|4|5|6|7| ")
    print("--------------- ")
    for i in range(len(grid)) :
        tab = ""
        for j in range(len(grid[i])) :
            if (j == 0) :
                tab += grid[i][j]
            else :
                tab = tab + "|" + grid[i][j]
        tab = "|" + tab + "| \n"
        print(tab)
    print("--------------- \n")

def addPiece(column, playerID) :
    column -= 1
    i = 5
    while(grid[i][column] != " ") :
        i -= 1
    if (playerID == 1) :
        grid[i][column] = "X"
    else :
        grid[i][column] = "O"
    if (i == 0) :
        fullColumns.append(column+1)
    lastPlaced = []
    lastPlaced.append(column)
    lastPlaced.append(i)
    lastPlaced.append(playerID)
    return lastPlaced

def checkWin(lastPlaced) :
    x = lastPlaced[0]
    y = lastPlaced[1]
    playerID = lastPlaced[2]
    if (playerID == 1):
        playerSymbol = "X"
    else :
        playerSymbol = "O"
    #Check UNDER (Down) last placed
    if (y <= 2) :
        sumDown = 0
        while (y+sumDown+1 < 6 and grid[y+sumDown+1][x] == playerSymbol) :
            sumDown += 1
        if (sumDown+1 >= 4) :
            return True
    #Check NEXT TO last placed
    if ((x > 0 and grid[y][x-1] == playerSymbol) or (x < 6 and grid[y][x+1] == playerSymbol)) :
        sumLeft = 0
        sumRight = 0
        if (x > 0 and grid[y][x-1] == playerSymbol) :
            sumLeft = 1
            while (x-sumLeft-1 >= 0 and grid[y][x-sumLeft-1] == playerSymbol) :
                sumLeft += 1
        if (x < 6 and grid[y][x+1] == playerSymbol) :
            sumRight = 1
            while (x+sumRight+1 <= 6 and grid[y][x+sumRight+1] == playerSymbol) :
                sumRight += 1
        sumSides = sumLeft + sumRight
        if (sumSides+1 >= 4) :
            return True
    #Check DIAGONAL Left last placed
    if ((x > 0 and y > 0 and grid[y-1][x-1] == playerSymbol) or (x < 6 and y < 5 and grid[y+1][x+1] == playerSymbol)) :
        sumUpLeft = 0
        sumDownRight = 0
        if (x > 0 and y > 0 and grid[y-1][x-1] == playerSymbol) :
            sumUpLeft = 1
            while (x-sumUpLeft-1 >= 0 and y-sumUpLeft-1 >= 0 and grid[y-sumUpLeft-1][x-sumUpLeft-1] == playerSymbol) :
                sumUpLeft += 1
        if (x < 6 and y < 5 and grid[y+1][x+1] == playerSymbol) :
            sumDownRight = 1
            while (x+sumDownRight+1 <= 6 and y+sumDownRight+1 <= 5 and grid[y+sumDownRight+1][x+sumDownRight+1] == playerSymbol) :
                sumDownRight += 1
        sumDiagonalLeft = sumUpLeft + sumDownRight
        if (sumDiagonalLeft+1 >=4) :
            return True
    #Check DIAGONAL Right last placed
    if ((x < 6 and y > 0 and grid[y-1][x+1] == playerSymbol) or (x > 0 and y < 5 and grid[y+1][x-1] == playerSymbol)) :
        sumUpRight = 0
        sumDownLeft = 0
        if (x < 6 and y > 0 and grid[y-1][x+1] == playerSymbol) :
            sumUpRight = 1
            while (x+sumUpRight+1 <= 6 and y-sumUpRight-1 >= 0 and grid[y-sumUpRight-1][x+sumUpRight+1] == playerSymbol) :
                sumUpRight += 1
        if (x > 0 and y < 5 and grid[y+1][x-1] == playerSymbol) :
            sumDownLeft = 1
            while (x-sumDownLeft-1 >= 0 and y+sumDownLeft+1 <= 5 and grid[y+sumDownLeft+1][x-sumDownLeft-1] == playerSymbol) :
                sumDownLeft += 1
        sumDiagonalRight = sumUpRight + sumDownLeft
        if (sumDiagonalRight+1 >=4) :
            return True
    return False
    
def validColumn(column) :
    integersTab = ["1","2","3","4","5","6","7"]
    if (column not in integersTab) :
        print("Wrong column value\n")
        return False
    else :
        if (int(column) in fullColumns) :
            print("Column is full\n")
            return False
    return True

def run() :
    fillGrid()
    currentTurn = 0
    gameWon = False
    print("Bienvenue sur Puissance 4\n")
    while (not gameWon and currentTurn < 42) :
        currentTurn += 1
        if (currentTurn%2 == 1) :
            currentPlayer = 1
            currentPlayerSymbol = "X"
        else : 
            currentPlayer = 2
            currentPlayerSymbol = "O"
        
        print("\n"*25)
        displayGrid()
        print("Player ",currentPlayer," [",currentPlayerSymbol,"], pick a column (0 to exit) :\n")
        columnPlayed = input()
        if (columnPlayed == "0") :
            return
        while (not validColumn(columnPlayed)) :
            columnPlayed = input()
            if (columnPlayed == "0") :
                return
        gameWon = checkWin(addPiece(int(columnPlayed), currentPlayer))
    if (gameWon) :
        print("\n"*25)
        displayGrid()
        print("Player ",currentPlayer," wins the game in ",currentTurn," turns !\n")
    else : 
        grid[0][int(columnPlayed)-1] = currentPlayerSymbol
        print("\n"*25)
        displayGrid()
        print("Draw after ",currentTurn," turns ...\n")
    
run()