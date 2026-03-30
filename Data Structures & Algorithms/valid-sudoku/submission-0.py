class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  
        for r in range(9):
            for c in range(9):
                current = board[r][c]
                square_num = (r//3)*3 + (c//3)
                if current == ".":
                    continue
                if(current in rows[r] or current in cols[c] or current in squares[square_num]):
                    return False
                cols[c].add(current)
                rows[r].add(current)
                squares[square_num].add(current)
        return True