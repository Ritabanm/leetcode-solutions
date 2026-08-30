class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event2[0]< event1[0]:
            event1, event2 = event2, event1
        if event1[1]<event2[0]:
            return False
        return True
        