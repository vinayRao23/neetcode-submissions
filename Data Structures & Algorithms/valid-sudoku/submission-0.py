class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        # rows
        sudokurows = {}
        for index, row in enumerate(board):
            sudokurows[index] = {}
            for val in row:
                if val == ".":
                    continue
                if val not in sudokurows[index]:
                    sudokurows[index][val] = 0
                sudokurows[index][val] += 1
        for outerkey, innerdict in sudokurows.items():
            for innerkey, value in innerdict.items():
                if sudokurows[outerkey][innerkey] != 1:
                    return False

        # columns
        sudokucolumns = {}
        for index, col in enumerate(board):
            sudokucolumns[index] = {}
            for i in range(len(board[index])):
                if board[i][index] == ".":
                    continue
                if board[i][index] not in sudokucolumns[index]:
                    sudokucolumns[index][board[i][index]] = 0
                sudokucolumns[index][board[i][index]] += 1
        for outerkey, innerdict in sudokucolumns.items():
            for innerkey, value in innerdict.items():
                if sudokucolumns[outerkey][innerkey] != 1:
                    return False

        # squares
        sudokusquares = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box_key = (row // 3, col // 3)
                if box_key not in sudokusquares:
                    sudokusquares[box_key] = {}
                if val not in sudokusquares[box_key]:
                    sudokusquares[box_key][val] = 0
                sudokusquares[box_key][val] += 1
        for outerkey, innerdict in sudokusquares.items():
            for innerkey, value in innerdict.items():
                if sudokusquares[outerkey][innerkey] != 1:
                    return False   
                
        return True
                
        