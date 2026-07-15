class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # idea
        # - order them from left to right
        # - add and subtract passengers along the way
        # - if at any point passengers>capacity then false
    
        events=[(u,n) for n,u,v in trips]+[(v,-n) for n,u,v in trips]
        events.sort()
        passengers=0
        for pos,n in events:
            passengers+=n
            if passengers>capacity: return False
        return True

