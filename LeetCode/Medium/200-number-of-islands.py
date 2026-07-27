# Number of Islands [Medium][Acceptance: 64.8%]
# https://leetcode.com/problems/number-of-islands/description/

class Solution(object):
    def numIslands(self, grid):

        # Spread function
        def identifyIsland(start, visited, grid):

            queue = deque([start])
            visited.add(start)

            while len(queue) > 0:
                coord = queue.popleft()
                m, n = coord[0], coord[1]
                 
                #check up
                if m != 0 and grid[m-1][n] == "1" and (m-1,n) not in visited:
                    queue.append((m-1,n))
                    visited.add((m-1,n))
                #check right
                if n != len(grid[0])-1 and grid[m][n+1] == "1" and (m,n+1) not in visited:
                    queue.append((m,n+1))
                    visited.add((m,n+1))

                #check down
                if m != len(grid)-1 and grid[m+1][n] == "1" and (m+1,n) not in visited:
                    queue.append((m+1,n))
                    visited.add((m+1,n))

                #check left
                if n != 0 and grid[m][n-1] == "1" and (m,n-1) not in visited:
                    queue.append((m,n-1))
                    visited.add((m,n-1))
            return

        visited = set()
        islands = 0

        # Walk throught the matrix
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1" and (m,n) not in visited:
                    islands +=1
                    identifyIsland((m,n), visited, grid)
        
        return islands
