class OrderedSet:
    def __init__(self):
        self.set = []
    
    def add(self, val):
        self.set.append(val)
        self.set.sort(reversed=False)
    
    def findByOrder(self, k):
        if k < 0 or k >= len(self.set): return None
        return self.set[k]
    
    def orderOfKey(self, val):
        return sum(1 for x in self.set if x < val)

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        for num in nums: self.prefix.append((self.prefix[-1] if self.prefix else 0) + num)

    def update(self, index: int, val: int) -> None:
        num = self.prefix[index] - (self.prefix[index - 1] if index > 0 else 0)
        val = val - num
        for i in range(index, len(self.prefix)): self.prefix[i] += val

    def sumRange(self, left: int, right: int) -> int:
        l = self.prefix[left - 1] if left > 0 else 0
        r = self.prefix[right]
        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
