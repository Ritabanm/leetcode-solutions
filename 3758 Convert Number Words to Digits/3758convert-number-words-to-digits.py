class Solution:
    def convertNumber(self, s):
        n = len(s)

        dict1 = {}
        dict1["zero"] = '0'
        dict1["one"] = '1'
        dict1["two"] = '2'
        dict1["three"] = '3' 
        dict1["four"] = '4'
        dict1["five"] = '5'
        dict1["six"] = '6'
        dict1["seven"] = '7'
        dict1["eight"] = '8'
        dict1["nine"] = '9'

        i, t = 0, ""

        while i < len(s):
            found_key = False

            for key in dict1.keys():
                if s[i:i+len(key)] == key:
                    t += dict1[s[i:i+len(key)]]
                    found_key = True 
                    i += len(key)
                    break

            if not found_key:
                i += 1 

        return t 