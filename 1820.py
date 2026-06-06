# class Solution:
#     def maximumInvitations(self, grid: List[List[int]]) -> int:
#         """
#         Solves the maximum bipartite matching problem using Hungarian algorithm.
#         Each boy (row) can be matched with at most one girl (column) based on grid preferences.

#         Args:
#             grid: 2D list where grid[i][j] = 1 means boy i can invite girl j

#         Returns:
#             Maximum number of successful invitations (matches)
#         """

#         def dfs_augmenting_path(boy_idx: int) -> bool:
#             for girl_idx, can_invite in enumerate(grid[boy_idx]):
#                 if can_invite and girl_idx not in visited_girls:
#                     # Mark this girl as visited to avoid cycles
#                     visited_girls.add(girl_idx)

#                     if girl_to_boy_match[girl_idx] == -1 or dfs_augmenting_path(girl_to_boy_match[girl_idx]):
#                         girl_to_boy_match[girl_idx] = boy_idx
#                         return True

#             return False

#         num_boys, num_girls = len(grid), len(grid[0])
#         girl_to_boy_match = [-1] * num_girls
#         total_matches = 0

#         for boy_idx in range(num_boys):
#             visited_girls = set()
#             if dfs_augmenting_path(boy_idx): total_matches += 1

#         return total_matches


from collections import defaultdict
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:


        m,n=len(grid),len(grid[0])
        g2b=defaultdict(lambda:-1)
        
        def dfs(b):
            for g,x in enumerate(grid[b]):
                if x and g not in vis:
                    vis.add(g)
                    if g2b[g]==-1 or dfs(g2b[g]):
                        g2b[g]=b
                        return True
            return False

        
        for i in range(m):
            vis=set()
            if dfs(i): res+=1
        return res


































