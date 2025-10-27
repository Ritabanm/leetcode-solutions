"""class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        number_of_balloons = min(count['a'],count['n'],count['b'],count['l']//2,count['o']//2)

        return number_of_balloons
        """
class Solution:
    def maxNumberOfBalloons(self, text):
        count = Counter(text)
        num_b = min(count['a'], count['n'], count['b'], count['l']//2, count['o']//2)
        return num_b