"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-search/
"""


class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
                or board[row][col] == "0"
            ):
                return False

            board[row][col] = "0"
            result = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )
            board[row][col] = word[index]

            return result

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
