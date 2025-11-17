class Node:
    def __init__(self):
        self.leftCnt=0
        self.rightCnt=0
        self.left=None
        self.right=None
        self.val=-1
class Trie:
    def __init__(self):
        self.root= Node()

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n=len(parents)
        root=-1
        gr=[[] for i in range(n)]
        for i in range(n):
            if parents[i]==-1:
                root=i
            else:
                gr[parents[i]].append(i)
        q=[[] for i in range(n)]
        for i in range(len(queries)):
            a=[queries[i][1],i]
            q[queries[i][0]].append(a)
        trie = Trie()
        ans=[-1 for i in range(len(queries))]
        def add(val):
            node=trie.root
            for i in range(18,-1,-1):
                if (val>>i & 1):
                    node.rightCnt+=1
                    if node.right==None:
                        node.right=Node()
                    node=node.right
                else:
                    node.leftCnt+=1
                    if node.left==None:
                        node.left=Node()
                    node=node.left
            node.val=val
        def remove(val):
            node=trie.root
            for i in range(18,-1,-1):
                if (val>>i & 1):
                    node.rightCnt-=1
                    node=node.right
                else:
                    node.leftCnt-=1
                    node=node.left
            node.val=-1
        def getAns(val):
            node=trie.root
            for i in range(18,-1,-1):
                if (val>>i & 1):
                    if node.leftCnt==0:
                        node=node.right
                    else:
                        node=node.left
                else:
                    if node.rightCnt==0:
                        node=node.left
                    else:
                        node=node.right

            return node.val^val

        def dfs(node):
            add(node)
            for i in q[node]:
                ans[i[1]]=getAns(i[0])
            for ch in gr[node]:
                dfs(ch)
            remove(node)
        dfs(root)
        return ans


        