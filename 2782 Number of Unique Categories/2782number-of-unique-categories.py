# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        parents = [0]

        for i in range(1, n):
            has_p = False
            for p in parents: 
                if categoryHandler.haveSameCategory(i, p):
                    has_p=True
                    break
            if not has_p:
                parents.append(i)
        
        return len(parents)


