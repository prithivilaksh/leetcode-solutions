# Disk Storage
# A disk stores hierarchical data in an undirected tree with tree_nodes nodes numbered from 0 to tree_nodes - 1, rooted at node 0. Each node has a character value represented by an array named arr, where arr[i] is the character on the i-th node.
# You are given an array queries of length m. For each query queries[i], determine how many nodes v (including queries[i]) exist on the path from queries[i] to the root, such that the letters on the nodes from queries[i] to v can be arranged to form a palindrome.
# Return an integer array of size m with the answer to each query.
# Note: A palindrome is a string that reads the same backward as forward. Examples of palindromes include "z", "aaa", "aba", and "abccba".

# Example

# tree_nodes = 4
# arr = ['z', 'a', 'a', 'a']
# tree_from = [0, 0, 1]
# tree_to = [1, 2, 3]
# m = 1
# queries = [3]

# Tree structure:
#     0(z)
#    /    \
#  2(a)   1(a)
#          |
#         3(a)
# Answer: [4]
# For query node 3, the path to root is: 3(a) → 1(a) → 0(z).

# {a} → palindrome ✓
# {a, a} → "aa" ✓
# {a, a, a} → "aaa" ✓
# {a, a, a, z} → "aazaa" ✓

# All 4 nodes on the path qualify, so the answer is 4.


from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

def palindromePaths(n, tree_from, tree_to, arr, queries):
    g = defaultdict(list)
    for u, v in zip(tree_from, tree_to):
        g[v].append(u)
        g[u].append(v)
    
    res = [0] * n
    
    # Count how many times each bitmask has appeared on path from root to current node
    mask_count = defaultdict(int)
    mask_count[0] = 1  # empty path has mask 0
    
    def dfs(u, p, mask):
        c = ord(arr[u]) - ord('a')
        mask ^= (1 << c)  # toggle bit for current character
        

        # like prefix sum to find target
        # When two nodes have the same mask, XOR = 000 → all characters appeared even times → palindrome ✓
        # When two nodes differ by 1 bit, XOR = 000...1...000 → exactly one character is odd → palindrome ✓ (middle character)
        # Palindrome possible if at most 1 bit set in XOR of path masks
        # Check mask with 0 bits set (even all chars)
        res[u] += mask_count[mask]
        # Check mask with exactly 1 bit set (one odd char allowed)
        for i in range(26):
            res[u] += mask_count[mask ^ (1 << i)]
        
        mask_count[mask] += 1
        
        for v in g[u]:
            if v != p:
                dfs(v, u, mask)
        
        mask_count[mask] -= 1  # backtrack
    
    dfs(0, -1, 0)
    
    return [res[q] for q in queries]


if __name__ == '__main__':
    arr = ['z', 'a', 'a', 'a']
    tree_from = [0, 0, 1]
    tree_to = [1, 2, 3]
    queries = [3]
    
    print(palindromePaths(4, tree_from, tree_to, arr, queries))
    # Expected: [4]