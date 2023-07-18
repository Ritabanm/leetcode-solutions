class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        temp = {}

        for index, size in enumerate(groupSizes):
            if size not in temp:
                temp[size] = []
            temp[size].append(index)
            
            if len(temp[size]) == size:
                answer.append(temp[size])
                temp[size] = []

        return answer


