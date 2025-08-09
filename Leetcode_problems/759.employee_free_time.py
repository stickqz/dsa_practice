from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        e_its = []

        # Convert lists to Interval objects for each employee
        for e in schedule:
            its = []
            for i in range(0, len(e), 2):
                it = Interval(e[i], e[i+1])
                its.append(it)
            
            e_its.append(its)
        
        minh = []

        # Push the first interval of each employee into the heap
        for idx, its in enumerate(e_its):
            heappush(minh, (its[0].start, idx, 0))

        free_t = []
        last = None

        while minh:
            st, ei, i = heappop(minh)
            it = e_its[ei][i]

            if last is None:
                last = it.end
            else:
                if it.start > last:
                    free_t.append(Interval(last, it.start))

                last = max(last, it.end)
        
            # Push the next interval from this employee
            if i + 1 < len(e_its[ei]):
                nxt = e_its[ei][i+1]
                heappush(minh, (nxt.start, ei, i+1))

        return free_t
    
# TC: O(N*logK)
# SC: O(K)
# N: number of intervals, K: Number of employees