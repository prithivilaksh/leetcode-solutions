# class Solution:
#     def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
#         mp=defaultdict(list)
#         for path in paths:
#             dir,*files=path.split()
#             for file in files:
#                 name,content=file.split("(")
#                 mp[content].append(dir+"/"+name)
#         return [v for v in mp.values() if len(v)>1]

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        mp=defaultdict(list)
        for path in paths:
            dir,*files=path.split()
            for file in files:
                name,content=file.split("(")
                mp[content].append(dir+"/"+name)
        return list(filter(lambda x:len(x)>1,mp.values()))