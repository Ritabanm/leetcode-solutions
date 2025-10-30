class Solution:
    def expTree(self, s: str) -> 'Node':
        def rank(op):
            if op=='*' or op=='/': return 2
            elif op=='+' or op=='-': return 1
            else: return 0
        
        def infixToPostfix(s):
            postfix = []
            st = []
            for ch in s:
                if ch >= '0' and ch <='9':
                    postfix.append(ch)
                else:
                    if ch=='(':
                        st.append('(')
                    elif ch==')':
                        while len(st)>0 and st[-1]!='(':
                            postfix.append(st.pop())
                        st.pop()
                    else:
                        while len(st)>0 and rank(ch) <= rank(st[-1]):
                            postfix.append(st.pop())
                        st.append(ch)
            while len(st)>0:
                postfix.append(st.pop())
            return postfix
        
        postfix = infixToPostfix(s)

        def postfixToTree(postfix):
            st = []
            for e in postfix:
                if e not in ['+', '-', '*', '/']:
                    st.append(Node(e))
                else:
                    right = st.pop()
                    left = st.pop()
                    n_node = Node(e, left, right)
                    st.append(n_node)
            return st.pop()
            
        root = postfixToTree(postfix)
        return root