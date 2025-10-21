class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        popularity = Counter()
        for response in responses:
            popularity.update(set(response.split()))
        
        return sorted(features, key=lambda x:popularity[x], reverse=True)