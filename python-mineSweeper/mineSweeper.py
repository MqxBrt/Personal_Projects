#python .\mineSweeper.py
#python3 mineSweeper.py

import os
import random
import platform

def main() :

    #Declaring grids needed
    global displayedGrid
    global hiddenGrid
    global truthGrid

    global flaggedCells
    flaggedCells = []

    #Displays array of array (max 16*16)
    def graph2DArray(myArray) :
        width = len(myArray[0])
        height = len(myArray)

        if (height<1 or height>16) :
            print("Error : invalid array size")
            exit()
        for i in range (height) :
            if (len(myArray[i]) != width) :
                print("Error : invalid array size")
                exit()

        hexa = ["A","B","C","D","E","F"]
        firstRow = "   │"
        for i in range (width) :
            if (i > 9) :
                j = i - 10
                firstRow += " " + hexa[j] + " │"
            else :
                firstRow += " " + str(i) + " │"

        middleRow = "───┼"
        lastRow = "───┴"

        for i in range (width) :
            if (i == width - 1) :
                lastRow += "───┘"
                middleRow += "───┤"
            else :
                lastRow += "───┴"
                middleRow += "───┼"

        print("\t" + firstRow)
        print("\t" + middleRow)

        for i in range (height) :
            if (i > 9) :
                j = i - 10
                display = " " + hexa[j] + " │"
            else :
                display = " " + str(i) + " │"
            for j in range (len(myArray[i])) :
                display = display + " " + str(myArray[i][j]) + " │"
            print("\t" + display)
            if (i == len(myArray) - 1) :
                print("\t" + lastRow)
            else :
                print("\t" + middleRow)
        print("\n")
        return 1

    #Updates grid display
    def refreshDisplay() :
        if (platform.system() == "Windows") : 
            os.system("cls")
        elif (platform.system() == "Linux" or platform.system() == "Darwin") :
            os.system("clear")
        print("\n"*3)
        graph2DArray(displayedGrid)

    #Returns array of arrays (h*w) filled with s
    def fillGrid(height, width, s) :
        myGrid = []
        for i in range (height) :
            tempTab = []
            for j in range (width) :
                tempTab.append(s)
            myGrid.append(tempTab)
        return myGrid

    #Setting all grids up
    displayedGrid = fillGrid(16, 16,"█")
    #Grid displayed on game screen
    hiddenGrid = fillGrid(16, 16, False)
    #Grid with mines (True if one on [i,j], else False)
    truthGrid = fillGrid(16, 16, True)
    #Grid with revealed status (True if unknown, esle False)
    flaggedCells.append(0)

    #Returns true if input is ok in mode, else false
    def validInput(x,mode) :
        if (mode == "difficulty") :
            return x in ["1","2","3"]
        if (mode == "rowcol") :
            return x in ["0","1","2","3","4","5","6","7","8","9","A","a","10","B","b","11","C","c","12","D","d","13","E","e","14","F","f","15"]
        if (mode == "yesno") :
            return x in ["Y","y","N","n","1","0"]

    #Sets grid up depending on difficulty chosen
    def createGame(difficulty) :
        if (difficulty == "1") :
            bombs = 0
            while (bombs < 20) :
                x = random.randint(0,15)
                y = random.randint(0,15)
                if (not (hiddenGrid[x][y])) :
                    hiddenGrid[x][y] = True
                    bombs += 1
            return 1
        if (difficulty == "2") :
            bombs = 0
            while (bombs < 40) :
                x = random.randint(0,15)
                y = random.randint(0,15)
                if (not (hiddenGrid[x][y])) :
                    hiddenGrid[x][y] = True
                    bombs += 1
            return 1
        if (difficulty == "3") :
            bombs = 0
            while (bombs < 60) :
                x = random.randint(0,15)
                y = random.randint(0,15)
                if (not (hiddenGrid[x][y])) :
                    hiddenGrid[x][y] = True
                    bombs += 1
            return 1

    #Turns string into decimal
    def hexaToDecimal(x) :
        if (x in ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]) :
            return int(x)
        else :
            if (x == "A" or x == "a") :
                return 10
            if (x == "B" or x == "b") :
                return 11
            if (x == "C" or x == "c") :
                return 12
            if (x == "D" or x == "d") :
                return 13
            if (x == "E" or x == "e") :
                return 14
            if (x == "F" or x == "f") :
                return 15

    #Returns the number of bombs around (x,y)
    def calcNeighbors(x,y) :
        xNeighbors = 0
        if (hiddenGrid[x][y]) :
            return -1
        for i in range (-1,2) :
            if (x+i < 0 or x+i >= 16) :
                continue
            for j in range (-1,2) :
                if (y+j < 0 or y+j >= 16) :
                    continue
                try:
                    if (hiddenGrid[x+i][y+j]) :
                        xNeighbors += 1
                except IndexError:
                    pass
        return xNeighbors

    #Reveals all the grid
    def revealAll() :
        for i in range (16) :
            for j in range (16) :
                xNeighbors = calcNeighbors(i,j)
                if (xNeighbors == - 1) :
                    displayedGrid[i][j] = "‼"
        #uncomment next 5 lines if you want to display all cells once over
                #else :
                    #if (xNeighbors == 0) :
                        #displayedGrid[i][j] = " "
                    #else :
                        #displayedGrid[i][j] = str(xNeighbors)

    #Reveals one cell and trigger verification on all neighbors
    def revealOne(x,y) :
        if (truthGrid[x][y]) :
            if (displayedGrid[x][y] == "◄") :
                flaggedCells[0] += flagCell(x,y)
            xNeighbors = calcNeighbors(x,y)
            if (xNeighbors == 0) :
                displayedGrid[x][y] = " "
                truthGrid[x][y] = False
                floodFill(x,y)
            else :
                displayedGrid[x][y] = str(xNeighbors)
                truthGrid[x][y] = False

    #Reveals all adjacent cells
    def floodFill(x,y) :
        for i in range (-1,2) :
            if (x+i < 0 or x+i >= 16) :
                continue
            for j in range (-1,2) :
                if (y+j < 0 or y+j >= 16) :
                    continue
                try:
                    revealOne(x+i,y+j)
                except IndexError:
                    pass

    #Flags a cell without revealing it
    def flagCell(x,y) :
        if (displayedGrid[x][y] == "◄") :
            if (truthGrid[x][y]) :
                displayedGrid[x][y] = "█"
            else :
                displayedGrid[x][y] = str(calcNeighbors(x,y))
            return -1
        else : 
            if (truthGrid[x][y]) :
                displayedGrid[x][y] = "◄"
                return 1
            else :
                return 0

    #Restarts a new game
    def restart() :
        print("\nDo you want to restart a game ? (Y/N)")
        restartInput = input()
        while (not validInput(restartInput,"yesno")) :
            (print("\nInvalid choice"))
            restartInput = input()
        if (restartInput in ["Y","y","1"]) :
            main()

    #Launches the game
    def run() :

        refreshDisplay()

        print("Welcome to MineSweeper !\n")
        print("\t1 • Easy")
        print("\t2 • Medium")
        print("\t3 • Hard\n")
        print("Choose difficulty level (0 to exit) :")
        difficultyLevel = input()

        if (difficultyLevel == "0") :
            return
        while (not validInput(difficultyLevel,"difficulty")) :
            print("\nWrong difficulty value\n")
            difficultyLevel = input()
            if (difficultyLevel == "0") :
                return
        createGame(difficultyLevel)

        flagMode = False
        while (hiddenGrid != truthGrid) :
            refreshDisplay()
            if (flagMode) :
                print("- FLAG MODE ON (-1 to turn off) -")
                print(str(flaggedCells[0]) + "/" + str(int(difficultyLevel)*20) + " flagged cells")
            print("Select a cell :\n")
            print("# Row (-1 to flag / -2 to cancel / -3 to exit) :")
            rowPlayed = input()
            if (rowPlayed == "-1") :
                flagMode = not flagMode
                continue
            if (rowPlayed == "-2") :
                continue
            if (rowPlayed == "-3") :
                restart()
                return
            while (not validInput(rowPlayed,"rowcol")) :
                print("\nWrong row value")
                rowPlayed = input()
                if (rowPlayed == "-1") :
                    flagMode = not flagMode
                    break
                if (rowPlayed == "-2") :
                    break
                if (rowPlayed == "-3") :
                    restart()
                    return

            if (rowPlayed in ["-1","-2","-3"]) :
                continue

            print("\n# Column (-1 to flag / -2 to cancel / -3 to exit) :")
            colPlayed = input()
            if (colPlayed == "-1") :
                flagMode = not flagMode
                continue
            if (colPlayed == "-2") :
                continue
            if (colPlayed == "-3") :
                restart()
                return
            while (not validInput(colPlayed,"rowcol")) :
                print("\nWrong column value")
                colPlayed = input()
                if (colPlayed == "-1") :
                    flagMode = not flagMode
                    break
                if (colPlayed == "-2") :
                    break
                if (colPlayed == "-3") :
                    restart()
                    return

            if (colPlayed in ["-1","-2","-3"]) :
                continue

            x = hexaToDecimal(rowPlayed)
            y = hexaToDecimal(colPlayed)
            neighbors = calcNeighbors(x,y)
            if (not flagMode) :
                if (neighbors == -1) :
                    if (displayedGrid[x][y] == "◄") :
                        print("\nYou're about to reveal a flagged cell, continue ? (Y/N)")
                        proceedRes = input()
                        while (not validInput(proceedRes,"yesno")) :
                            (print("\nInvalid choice"))
                            proceedRes = input()
                        if (proceedRes in ["Y","y","1"]) :
                            revealAll()
                            refreshDisplay()
                            print("BOOM !")
                            print("You lost...\n")
                            return 0
                        else :
                            continue
                    else :
                        revealAll()
                        refreshDisplay()
                        print("BOOM !")
                        print("You lost...\n")
                        restart()
                        return 0
                else :
                    if (displayedGrid[x][y] == "◄") :
                        print("\nYou're about to reveal a flagged cell, continue ? (Y/N)")
                        proceedRes = input()
                        while (not validInput(proceedRes,"yesno")) :
                            (print("\nInvalid choice"))
                            proceedRes = input()
                        if (proceedRes in ["Y","y","1"]) :
                            revealOne(x,y)
                        else :
                            continue
                    else :
                        revealOne(x,y)
            else :
                flaggedCells[0] += flagCell(x,y)

        refreshDisplay()
        print("CONGRATULATIONS !")
        print("You won.\n")
        restart()
        return 1

    run()

main()
