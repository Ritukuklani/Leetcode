class Solution:
    """
    We only need to care the start point and the end point.

                    s ----- n
    1 --------------------- n
    1 --------------------- n
    1 ----- e

    Explanation
    If start <= end, return the range [start, end].
    If end < start, return the range [1, end] + range [start, n].
    """
    def mostVisited(self, n: int, rounds):  # return type : List[int], rounds is of type: List[int]
        s, e = rounds[0], rounds[-1]
        if s<=e:
            return [i for i in range(s, e+1)] 
        else:
            return [i for i in range(1, e+1)] + [i for i in range(s, n+1)]
            