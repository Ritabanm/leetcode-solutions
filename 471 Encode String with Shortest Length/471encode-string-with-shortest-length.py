class Solution:
    
    def encode(self, s: str) -> str:
        memo = {}
        return self._get_encoded_str(s, memo)
    
    def _get_encoded_str(self, s, memo):
        if s == "" or len(s) < 5:
            return s
        if s in memo:
            return memo[s]
        chosen_str = s
        min_len = len(s)
        for i in range(1, len(s)//2 + 1):
            encoded_str = s
            prefix = s[:i]
            suffix = s[i:]
            prefix_count = self._get_prefix_count(prefix, suffix)
            encoded_prefix = self._get_encoded_str(prefix, memo)
            encoded_suffix = self._get_encoded_str(suffix, memo)
            if prefix_count > 0:
                k = prefix_count * len(prefix)
                encoded_suffix_from_k = self._get_encoded_str(suffix[k:], memo)
                encoded_str = str(prefix_count + 1) + "[" + encoded_prefix + "]" + encoded_suffix_from_k
            encoded_part_str = encoded_prefix + encoded_suffix 
            if len(encoded_str) > len(encoded_part_str):
                encoded_str = encoded_part_str
            if min_len > len(encoded_str):
                chosen_str = encoded_str
                min_len = len(encoded_str)
        memo[s] = chosen_str
        return chosen_str

    """
    Helper method finds the count of prefix in suffix.
    """
    def _get_prefix_count(self, prefix, suffix):
        count = 0
        i = 0
        while i < len(suffix):
            j = suffix.find(prefix, i)
            if i != j:
                break
            count += 1
            i = j + len(prefix)
        return count