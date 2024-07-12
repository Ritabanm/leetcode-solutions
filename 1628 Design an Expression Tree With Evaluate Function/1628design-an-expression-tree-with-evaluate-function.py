import abc 
from abc import ABC, abstractmethod 


class Node(ABC):
    
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
    
  
class NumericNode(Node):
    
    def __init__(self, val):
        self.val = val
        
    def evaluate(self):
        return self.val

    
class OperatorNode(Node):
    
    def __init__(self, oper, left, right):
        self.oper = oper
        self.left = left
        self.right = right
        
    def evaluate(self):
        if self.oper == '+':
            return self.left.evaluate() + self.right.evaluate()
        if self.oper == '-':
            return self.left.evaluate() - self.right.evaluate()
        if self.oper == '*':
            return self.left.evaluate() * self.right.evaluate()
        if self.oper == '/':
            return self.left.evaluate() // self.right.evaluate()
        

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        opers = set('-+*/')
        for c in postfix:
            if c not in opers:
                stack.append(NumericNode(int(c)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(OperatorNode(c, left, right))
        return stack[0]
		