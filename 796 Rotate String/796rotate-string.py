"""class Solution:
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        double_str = s+s
        return double_str.find(goal)!=-1"""
    
class Solution:
    def rotateString(self, s,goal):
        if len(s)!=len(goal):
            return False
        double_str = s+s
        return double_str.find(goal)!=-1