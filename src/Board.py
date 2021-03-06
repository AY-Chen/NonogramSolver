'''
Class to represent a board. 
'''

class Board:
    _width = 5
    _height = 5
    _horizontalHints = [] # hints for the rows as a list of tuples
    _verticalHints = [] # hints for columns as a list of tuples
    _board = [] # board is a list of lists, such that each element of _board is a row
    
    def __init__(self, width, height, horizontalHints, verticalHints):
        self._height = height
        self._width = width
        self._horizontalHints = horizontalHints
        self._verticalHints = verticalHints
        
    def getBoardAsText(self):
        '''Prints the board as a space separated string, as is
        0 corresponds to an empty square, 1 is a filled square and 2 is an "x" '''
        printout = ""
        for i in range(self._height):
            row = " ".join(map(str, self._board[i]))
            row = row + "\n"
            
            printout = printout + row            
        
        return printout
        
    def getBoardAsTextWithSquares(self):
        '''Prints the board as a space separated string of x, ■, □'''
        boardWithNumbers = self.getBoardAsText()
        boardWithSymbols = ""
        
        # TODO: map the 0, 1, 2 notation to the other symbols? Might be a pointless function
        
        return boardWithSymbols
    
    def setSquare(self, x, y, val):
        '''Set the square at (x, y) to the value given by val
        val should be either 0, 1, or 2'''
        if not (val == 0 or val == 1 or val == 2):
            raise ValueError("Invalid assignment to location ({}, {}) on the board. Val is not 0, 1, or 2.".format(x, y))
        
        if not (x in range(self._width) or y in range(self._height)):
            raise ValueError("Invalid assignment to location ({}, {}) on the board. " +
            "\nThe given location is outside the limits of the {}x{} board.".format(x, y, self._width, self._height))
        
        self._board[y][x] = val
    
if __name__ == "__main__":
    boardTest = Board(3, 3, [], [])
    boardTest._board = [[0, 2, 0], [1, 0, 0], [1, 0, 0]]
    print(boardTest.getBoardAsText())
    print("---")
    boardTest.setSquare(1, 1, 2)
    print(boardTest.getBoardAsText())
    
        
        
        