#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()

        def backtrack(n, row, cur_trail):
            if row == n:
                self.result.append(cur_trail)
                return

            for col in range(n):
                if (col in self.cols) or (row + col in self.pie) or (row - col in self.na):
                    continue 

                self.cols.add(col)
                self.pie.add(row + col)
                self.na.add(row - col)

                backtrack(n, row+1, cur_trail+[col])

                self.cols.remove(col)
                self.pie.remove(row+col)
                self.na.remove(row-col)
        backtrack(n, 0, [])

        return self._generate_result(n)
    
    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.' * i + 'Q' + '.' * (n- i-1))

        return [board[i:i+n] for i in range(0, len(board), n)]
        
# @lc code=end

