from typing import List


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list: List[NestedInteger], depth: int) -> int:
            res = 0
            for ele in nested_list:
                if ele.isInteger(): res += ele.getInteger() * depth
                else: res += dfs(ele.getList(), depth + 1)
            return res

        return dfs(nestedList, 1)