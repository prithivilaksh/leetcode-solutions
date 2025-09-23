# class RandomizedSet:

#     def __init__(self):
#         self.st=set()
        
#     def insert(self, val: int) -> bool:
#         if val in self.st: return False
#         self.st.add(val)
#         return True

#     def remove(self, val: int) -> bool:
#         if val not in self.st: return False
#         self.st.remove(val)
#         return True

#     def getRandom(self) -> int:
#         return random.choice(list(self.st))


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()

class RandomizedSet:

    def __init__(self):
        self.arr,self.ind=[],{}
        
    def insert(self, val: int) -> bool:
        if val in self.ind: return False
        self.ind[val]=len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ind: return False
        x=self.arr.pop()
        i=self.ind.pop(val)
        if x!=val:
            self.arr[i]=x
            self.ind[x]=i
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()