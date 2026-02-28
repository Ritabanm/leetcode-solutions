class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def dfs(cur_idx, expression, cur_sum, prev_num):
            if cur_idx == len(num):
                if cur_sum == target:
                    res.append(expression)
                return
            
            for i in range(cur_idx, len(num)):
                cur_str = num[cur_idx:i+1]
                if cur_str[0] == '0' and len(cur_str) > 1:
                    break  # Skip leading zero numbers
                
                cur_num = int(cur_str)
                if cur_idx == 0:
                    # Start of expression; no operator needed
                    dfs(i+1, cur_str, cur_num, cur_num)
                else:
                    # Recursive calls for +, -, and *
                    dfs(i+1, expression + '+' + cur_str, cur_sum + cur_num, cur_num)
                    dfs(i+1, expression + '-' + cur_str, cur_sum - cur_num, -cur_num)
                    dfs(i+1, expression + '*' + cur_str, cur_sum - prev_num + prev_num * cur_num, prev_num * cur_num)

        # Start DFS from index 0 with an empty expression
        dfs(0, "", 0, 0)
        return res
