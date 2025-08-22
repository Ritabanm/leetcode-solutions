class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        text_values = [ord(char) - 97 for char in text]
        hash_map = {}
        powers_of_26 = [1]
        

        for i in range(1, len(text) + 1):
            powers_of_26.append(powers_of_26[i - 1] * 26)
            

        for substring_length in range(1, len(text_values) // 2 + 1):
            current_hash = 0
            for k in range(0, substring_length):
                current_hash = current_hash * 26 + text_values[k]
            hash_map[(0, substring_length)] = current_hash
            
            for start_index in range(1, len(text_values) - substring_length + 1):

                current_hash -= text_values[start_index - 1] * powers_of_26[substring_length - 1]
                current_hash = current_hash * 26 + text_values[start_index + substring_length - 1]
                hash_map[(start_index, start_index + substring_length)] = current_hash

        distinct_substrings = set()
        

        for pair in hash_map:
            first_pair = pair
            second_pair = (pair[1], pair[1] + (first_pair[1] - first_pair[0]))
            if first_pair in hash_map and second_pair in hash_map and hash_map[first_pair] == hash_map[second_pair]:
                distinct_substrings.add((first_pair[1] - first_pair[0], hash_map[first_pair]))
                    
        return len(distinct_substrings)