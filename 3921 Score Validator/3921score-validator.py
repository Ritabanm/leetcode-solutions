class Solution:
    def scoreValidator(self, events):
        score = 0
        counter = 0

        for i in events:
            if counter >= 10:
                return [score, counter]

            if i in {"1", "WD", "NB"}:
                score += 1
            elif i in {"2", "3", "4", "5", "6"}:
                score += int(i)
            elif i == "W":
                counter += 1

        return [score, counter]