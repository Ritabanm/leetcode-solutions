class Solution:
    def minimizeStringValue(self, s: str) -> str:    
        counts = {}
        
        for i in range(97, 123):
            counts[chr(i)] = 0
        
        for char in s:
            if char == "?":
                continue
            
            counts[char] += 1

        replaced_characters = []
        
        for i in range(len(s)): 
            if s[i] != "?":
                continue
                
            min_occuring = float('inf')
            min_char = ''
                
            for key, value in counts.items():
                if value < min_occuring:
                    min_occuring = value
                    min_char = key
                    
            replaced_characters.append(min_char)
            counts[min_char] += 1
        
        replaced_index = 0
        replaced_characters.sort()
        final_string = ''

        for char in s:
            if char == '?':
                final_string += replaced_characters[replaced_index]
                replaced_index += 1
            else:
                final_string += char
        
        return final_string
            

            
                
                    
                
                