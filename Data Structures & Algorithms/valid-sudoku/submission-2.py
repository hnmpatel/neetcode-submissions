class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [[[]] for i in range(9)]
        columns = [[[]] for i in range(9)]
        for i in range(9):
            tmp_row = []
            for j in range(9):
                n = board[i][j]
                k = (i // 3) * 3 + (j // 3)
                if not ('1' <= n <= '9'):
                    continue

                # Row rule check
                if n in tmp_row:
                    return False
                else:
                    tmp_row.append(n)

                # Column rule check
                if n in columns[j]:
                    return False
                else:
                    columns[j].append(n)

                # 3 x 3 Grid rule check
                if n in grids[k]:
                    return False
                else:
                    grids[k].append(n)
        return True
                
                
            