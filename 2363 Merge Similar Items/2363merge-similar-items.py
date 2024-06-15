class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        my_dict = dict(items1)
        for k, v in items2:
            if k in my_dict:
                my_dict[k] += v
            else:
                my_dict[k] = v
        return sorted(my_dict.items())