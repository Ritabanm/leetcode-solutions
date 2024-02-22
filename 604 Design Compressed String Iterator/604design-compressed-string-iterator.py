class StringIterator:

    def __init__(self, compressedString: str):
        self.og = compressedString
        self.curr = 0
        self.count = 0
        self.nextLetter = 0
        # initialize variables
        self.scanNext(0)
    def next(self) -> str:
        if self.hasNext():
            self.count -= 1
            return self.og[self.curr]
        else:
            return " "
    def hasNext(self) -> bool:
        if self.count > 0:
            return True
        else:
            # move on to next letter if there is one
            return self.scanNext(self.nextLetter)
        return False
    
    def scanNext(self, index) -> bool:
        repeat = ""
        if index >= len(self.og):
            return False
        self.curr = index
        for i in range(self.curr+1, len(self.og)):
            # edge case
            if i == len(self.og)-1:
                self.nextLetter = i+1
            if self.og[i].isnumeric():
                repeat += self.og[i]
            else:
                self.nextLetter = i
                break
        if repeat == "":
            return False
        self.count = int(repeat)
        return True



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()