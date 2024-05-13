from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        queue = list()
        result = list()
        max_number = 10 ** (n)
        low_bound = 10 ** (n-1) - 1
        for i in range(1,10):
            queue.append(i)
        while len(queue)!=0:
            digit = queue.pop(0)
            last_digit = digit%10
            new_digit = 0
            if (last_digit + k)<10:
                new_digit = (digit*10) + (last_digit + k)
                if new_digit != 0 and new_digit < max_number:
                    queue.append(new_digit)
                if new_digit > low_bound and new_digit < max_number:
                    result.append(new_digit)
            if k != 0 and (last_digit - k) >= 0:
                new_digit = (digit*10) + (last_digit-k)
                if new_digit != 0 and new_digit < max_number:
                    queue.append(new_digit)
                if new_digit > low_bound and new_digit < max_number:
                    result.append(new_digit)
        return result

sol = Solution()
sol.numsSameConsecDiff(3,0)