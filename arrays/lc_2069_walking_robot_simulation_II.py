"""Walking Robot Simulation II"""

"""Problem: https://leetcode.com/problems/walking-robot-simulation-ii/"""

direct = ["East", "North", "West", "South"]

class Robot:
    def __init__(self, width, height):
        self.length = 2 * (width + height - 2)
        self.w = width
        self.h = height
        self.distance = 0
        self.started = False

    def step(self, num):
        self.distance = (self.distance + num) % self.length
        self.started = True

    def getPos(self):
        if self.distance < self.w:
            return [self.distance, 0]
        if self.distance < self.w + self.h - 1:
            return [self.w - 1, self.distance - self.w + 1]
        if self.distance < 2 * self.w + self.h - 2:
            return [self.length - self.distance - self.h + 1, self.h - 1]
        return [0, self.length - self.distance]

    def getDir(self):
        if self.distance == 0 and self.started:
            return direct[3]
        if self.distance < self.w:
            return direct[0]
        if self.distance < self.w + self.h - 1:
            return direct[1]
        if self.distance < 2 * self.w + self.h - 2:
            return direct[2]
        return direct[3]
    