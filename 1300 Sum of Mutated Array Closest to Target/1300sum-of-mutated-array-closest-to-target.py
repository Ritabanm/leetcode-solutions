class Solution:
	def findBestValue(self, arr: List[int], target: int) -> int:
		arr.sort()
		low, high = 0, arr[-1]
		memo = {}
		while low<=high:
			mid = low + (high-low) // 2
			count=0

			for i in range(len(arr)):
				if arr[i]>mid:
					count+= mid * (len(arr)-i)
					break
				else: count+=arr[i]

			if count == target:
				return mid

			if count < target:
				low = mid + 1

			else:
				high = mid - 1 

			memo[mid] = abs(count-target)

		return min(sorted(zip(memo.values(), memo.keys())))[1]