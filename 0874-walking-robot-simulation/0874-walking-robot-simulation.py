class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = d = ans = 0
        obstaclesSet = set(map(tuple, obstacles))

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d + 3) % 4
            else:
                for _ in range(c):
                    nx, ny = x + dirs[d][0], y + dirs[d][1]
                    if (nx, ny) in obstaclesSet:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans
