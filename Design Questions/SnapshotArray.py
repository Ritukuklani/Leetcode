class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0]*(length)
        self.count = 0
        self.snap_dict = {}

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        curr_arr = self.arr.copy()
        self.snap_dict[self.count] = curr_arr
        self.count+=1
        return self.count-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_dict[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)