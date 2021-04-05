#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = {'up': [0, 1, 'left', 'right'],
                     'down': [0, -1, 'right', 'left'],
                     'left': [-1, 0, 'down', 'up'],
                     'right': [1, 0, 'up', 'down']}
        x, y = 0, 0
        ort = 'up'
        res = 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:
                for step in range(command):
                    if (x + direction[ort][0], y + direction[ort][1]) not in obstacles:
                        x += direction[ort][0]
                        y += direction[ort][1]
                        res = max(res, x**2+y**2)
                    else:
                        break
            else:
                if command == -1:
                    ort = direction[ort][3]
                else:
                    ort = direction[ort][2]
        return res

# @lc code=end

