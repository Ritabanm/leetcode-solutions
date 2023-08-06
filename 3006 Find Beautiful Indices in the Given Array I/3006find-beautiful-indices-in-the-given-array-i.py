class Solution:
	def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

		result = []

		sl, al, bl = len(s) , len(a) , len(b)

		a_index , b_index = [] , []

		for i in range(sl):

			if s[i] == a[0] and s[i:i + al] == a:
				a_index.append(i)

			if s[i] == b[0] and s[i:i + bl] == b:
				b_index.append(i)

		for i in a_index:
			for j in b_index:

				if abs(i - j) <= k:
					result.append(i)
					break

		return result
		
