from typing import List


class Solution:
    """
    Basic idea: 
        1. sort the cars according to their position
        2. If car is faster than the previous one = time of crossing the finish line earlier than the previous car -> fleet -> don't add it to the pile
        3. In the top element of the stack - the current fleet car - time of crossing the finish line
        Stack in ascending order 
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        cars = sorted(zip(position, speed), reverse=True)
        final = []
        for p, s in cars:
            t_car = (target - p) / s
            if not final:
                final.append(t_car)
            if t_car > final[-1]:
                final.append(t_car)
        return len(final)
