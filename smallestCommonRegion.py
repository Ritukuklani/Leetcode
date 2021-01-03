class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str: # regions is of type, List[List[str]]
        parent = {}
        for i in range(len(regions)):
            for j in range(1, len(regions[i])):
                parent[regions[i][j]] = regions[i][0]
        ancestors = set()
        final_parent = regions[0][0]
        while region1!=final_parent:
            ancestors.add(region1)
            region1 = parent[region1]
        ancestors.add(final_parent)
        while region2 not in ancestors:
            region2 = parent[region2]
        return region2
            