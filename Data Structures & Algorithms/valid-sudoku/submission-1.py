class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                tupleKey  = tuple((i//3,j//3))
                if cur == ".":
                    continue
                
                if (cur in rows[i]) or (cur in cols[j]) or (cur in squares[tupleKey]):
                    return False

                rows[i].add(cur)
                cols[j].add(cur)
                squares[tupleKey].add(cur)
                
                #print(board[i][j])
        return True
        