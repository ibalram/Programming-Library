# https://leetcode.com/problems/word-search-ii/


"""
If we think naively, we have to search for every word by checking from every starting point of grid.
we can search any word using backtracking/dfs. Now There large number of words can be in input
and then dfs for every every word for every starting cell will be too slow.
Time complexity: O(K*(m*n)*(4^l)), l = max length of a word


So we can improve searching part by using Trie data structure. So overall algorithm will be following.
1. First insert all the words in the Trie. SO that we can search as fast as we can.
2. Now do backtracking from every starting cell of grid, by checking in the Trie parallely for sequence of word formed.
3. Also maintain the set of found words in the list.

Time complexity: O((m*n)*(4^l)), l = max length of a word
Space complexity: O(l), infact 26*l for trie


"""



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        trie = {}
        for word in words:
            root = trie
            for i in word:
                if i not in root:
                    root[i] = {}
                root = root[i]
            root["word"] = word
        res =set()
        def dfs(i,j,root):
            if "word" in root:
                res.add(root["word"])
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                x = i+dx
                y = j+dy
                if 0<=x<n and 0<=y<m and (x,y) not in vis and board[x][y] in root:
                    vis[(x,y)] = 1
                    dfs(x,y,root[board[x][y]])
                    del vis[(x,y)]

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    vis={(i,j):1}
                    dfs(i,j,trie[board[i][j]])
        return list(res)


