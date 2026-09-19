class SnapshotArray:

    def __init__(self, l: int):
        self.arr=[[(-1,0)] for _ in range(l)]
        self.id=0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.id,val))

    def snap(self) -> int:
        self.id+=1
        return self.id-1

    def get(self, index: int, snap_id: int) -> int:
        vals=self.arr[index]
        pos=bisect_right(vals,snap_id,key=lambda x:x[0])-1
        return vals[pos][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)