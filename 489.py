# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """




class Solution:
    def cleanRoom(self, robot):

        # idea/observation:
        # 1) since coordinates are not directly available, use relative coordinates
        # 2) based on the current direction, find the next direction and move accodingly.
        # 3) let up, right, down, left maps to 0, 1, 2, 3
        # 4) if we are facing down, then the next right is actually left in a relative sense.
        # 5) if our current direction is 1, then after a right turn, it is 2 and so on.
        # 6) the order of direction matters ((-1,0),(0,1),(1,0),(0,-1)), as from dir[i] we should move to dir[i+1%4]


        dir=((-1,0),(0,1),(1,0),(0,-1))
        vis=set()

        def dfs(i, j, d):
            vis.add((i, j))
            robot.clean()

            for k in range(4):
                nd = (d + k) % 4
                di, dj = dir[nd]
                ni, nj = i + di, j + dj

                if (ni, nj) not in vis and robot.move():
                    dfs(ni, nj, nd)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                robot.turnRight()

        dfs(0, 0, 0)
