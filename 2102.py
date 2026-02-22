# class SORTracker:

#     def __init__(self):
#         self.i=-1
#         self.loc=[]

#     def add(self, name: str, score: int) -> None:
#         insort(self.loc,(-score,name))

#     def get(self) -> str:
#         self.i+=1
#         return self.loc[self.i][1]



# # Your SORTracker object will be instantiated and called as such:
# # obj = SORTracker()
# # obj.add(name,score)
# # param_2 = obj.get()

# class SORTracker:

#     def __init__(self):
#         self.i=-1
#         self.loc=SortedList()

#     def add(self, name: str, score: int) -> None:
#         self.loc.add((-score,name))

#     def get(self) -> str:
#         self.i+=1
#         return self.loc[self.i][1]



# # Your SORTracker object will be instantiated and called as such:
# # obj = SORTracker()
# # obj.add(name,score)
# # param_2 = obj.get()

class Item:
    def __init__(self,score,name):
        self.score,self.name=score,name   
    
    def AsMxItem(self): return MxItem(self.score,self.name)
    def AsMiItem(self): return MiItem(self.score,self.name)
    def Name(self): return self.name

class MxItem(Item):
    def __init__(self,score,name):
        super().__init__(score,name)
    
    def __lt__(self,other):
        if self.score==other.score: return self.name<other.name
        return self.score>other.score

class MiItem(Item):
    def __init__(self,score,name):
        super().__init__(score,name)
    
    def __lt__(self,other):
        if self.score==other.score: return self.name>other.name
        return self.score<other.score



class SORTracker:
    def __init__(self):
        self.i=1
        self.mi,self.mx=[],[]

    def add(self, name: str, score: int) -> None:
        heappush(self.mx,MxItem(score,name))
        item=heappop(self.mx)
        heappush(self.mi,item.AsMiItem())
        if len(self.mi)>self.i:
            item=heappop(self.mi)
            heappush(self.mx,item.AsMxItem())
    

    def get(self) -> str:
        if len(self.mi)<self.i:
            item=heappop(self.mx)
            heappush(self.mi,item.AsMiItem())

        self.i+=1
        return self.mi[0].Name()



# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()