class Solution:
    def minSwap(self, A, B) -> int: # A and B are both lists of type int
#         Say we have
#         A = [1, 3, 8]
#         and
#         B = [2, 7, 4]

#         At the beginning, just looking at one column, the cost to end in column (1, 2) is natural = 0, and the cost to end in (2, 1) is swapped = 1. (Cost can be infinity if it's not possible.)

#         Now, when i = 1, if we ended in (1, 2), we could end in (3, 7) for no cost; we could end in (7, 3) for 1 cost [the cost of ending in (1,2), plus swapping the second column]; if we ended in (2, 1), we could end in (3, 7) for no additional cost [total cost 1], or end in (7, 3) for 1 additional cost [total cost 2]. In total, ending in (3, 7) has lowest total cost 0, and ending in (7, 3) has lowest total cost 1.

#         Now, when i = 2, if we ended in (3, 7), we can't end in (8, 4) because the sequences won't be increasing [specifically, B won't be]. We could end in (4, 8) for an additional cost of 1 [total cost 1]. If we ended in (7, 3), we can end in (8, 4) for an additional cost of 0 [total cost 1], and we can't end in (4, 8) because A won't be increasing. In total, ending in (4, 8) has lowest total cost 1, and ending in (8, 4) also has lowest total cost 1.

#         I know these above paragraphs are kind of confusing, but here is a recap:
#         Cost to end the first i columns with the i-th column not flipped: 0, 0, 1
#         Cost to end the first i columns with the i-th column flipped: 1, 1, 1
        prev_natural, prev_swapped = 0, 1
        for i in range(1, len(A)):
            curr_natural, curr_swapped = float("inf"), float("inf")
            if A[i]>A[i-1] and B[i] > B[i-1]:
                curr_natural = min(curr_natural, prev_natural)
                curr_swapped = min(curr_swapped, prev_swapped+1)
            if B[i]>A[i-1] and A[i] > B[i-1]:
                curr_natural = min(curr_natural, prev_swapped)
                curr_swapped = min(curr_swapped, prev_natural+1)
            prev_natural, prev_swapped = curr_natural, curr_swapped
        return min(curr_natural, curr_swapped)