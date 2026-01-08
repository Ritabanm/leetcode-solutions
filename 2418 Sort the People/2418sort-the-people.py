class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        num_people = len(names)

        height_to_name_map = OrderedDict()

        for height, name in zip(heights, names):
            height_to_name_map[height]=name
        
        height_to_name_map= OrderedDict(
            sorted(height_to_name_map.items(), reverse = True)
        )

        sorted_names = list(height_to_name_map.values())
        return sorted_names