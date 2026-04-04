# from sortedcontainers import SortedList
# class TimeMap:
#     def __init__(self):
#         self.mp=defaultdict(SortedList)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.mp[key].add((timestamp,value))

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.mp: return ""
#         vals=self.mp[key]
#         pos=bisect_right(vals,timestamp,key=lambda x:x[0])-1
#         if pos==-1: return ""
#         return vals[pos][1]


# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)

# class TimeMap:
#     def __init__(self):
#         self.mp=defaultdict(list)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         vals=self.mp[key]
#         pos=bisect_right(vals,timestamp,key=lambda x:x[0])
#         vals[pos:pos]=[(timestamp,value)]

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.mp: return ""
#         vals=self.mp[key]
#         pos=bisect_right(vals,timestamp,key=lambda x:x[0])-1
#         if pos==-1: return ""
#         return vals[pos][1]


# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)


# class TimeMap:
#     def __init__(self):
#         self.mp=defaultdict(list)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         vals=self.mp[key]
#         pos=bisect_right(vals,timestamp,key=lambda x:x[0])
#         vals.insert(pos,(timestamp,value))

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.mp: return ""
#         vals=self.mp[key]
#         pos=bisect_right(vals,timestamp,key=lambda x:x[0])-1
#         if pos==-1: return ""
#         return vals[pos][1]


# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)

class TimeMap:
    def __init__(self):
        self.mp=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        vals=self.mp[key]
        vals.append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp: return ""
        vals=self.mp[key]
        pos=bisect_right(vals,timestamp,key=lambda x:x[0])-1
        if pos==-1: return ""
        return vals[pos][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)