class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # compute xor of n
        n = len(encoded) + 1
        total_xor = 1
        for i in range(2,n+1):
            total_xor = total_xor ^ i
        
        # compute the first digit
        # step1: get xor of everything but the first digit
        remainder_xor = encoded[1]
        for i in range(3, len(encoded), 2):
            remainder_xor = remainder_xor ^ encoded[i]

        # step2: search for the value that makes the inequality true
        first_element = 1
        while first_element ^ remainder_xor != total_xor:
            first_element += 1

        # use the update equation
        out = [first_element]
        for el in encoded:
            out.append(out[-1]^el)

        return out


