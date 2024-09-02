class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # i think key is that the optimal solution is brute force
        # but even if you brute force, you will still be O(N)
        # bc the part lengths is unknown but it can atmost be 4 digits in worse case
        # so you'll loop 4 times at most

        # We will call total number of parts N
        # N is unknown in the beginning and we will try to find it by trying different lengths of N (how many digits in N)
        # at the beginning, we will reserve placeholder characters for N
        # at the end when N is known, we will try to replace the placeholder, 
        # but if the len of characters doesn't match, then we will try increasing len of N by 1 and doing the same thing
        
        message_len = len(message)
        for len_n in range(1, 5): # N will have between 1-4 digits
            parts = []
            i = 0
            n_placeholder = '?' * len_n
            while i < message_len:
                item_idx = str(len(parts) + 1)  
                suffix = '<'+item_idx+'/'+n_placeholder+'>'

                # what happens if suffix > limit?
                if len(suffix) >= limit:
                    return []

                # for now let's assume suffix < limit
                msg_part = message[i: min(i+ limit-len(suffix), len(message))]
                parts.append(msg_part + suffix)
                i += limit-len(suffix)

            if len(str(len(parts))) == len_n:
                # it means we have found the answer!
                N = str(len(parts))
                for i, part in enumerate(parts):
                    parts[i] = part.replace(n_placeholder, N)
                return parts

        return []