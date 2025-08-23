class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_numbers = [1,2]
        a, b = 0, 1
        while fib_numbers[-1] <= k:
            fib_numbers.append(a)
            a, b = b, a + b
        
        # Now use a greedy approach to find the minimum number of Fibonacci numbers
        count = 0
        # idx = len(fib_numbers) - 1
        while k > 0:
            while fib_numbers[-1] > k:
                fib_numbers.pop()
            else:
                count +=1
                k-= fib_numbers[-1]
        
        return count

        
        