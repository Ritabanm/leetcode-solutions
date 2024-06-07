function minimumSubarrayLength(nums, k) {
  let minLength = Infinity
  for (let i = 0; i < nums.length; i++) {
    let sumOr = 0
    for (let j = i; j < nums.length; j++) {
      sumOr |= nums[j]
      if (sumOr >= k) minLength = Math.min(minLength, j + 1 - i)
    }
  }
  return minLength === Infinity ? -1 : minLength
}