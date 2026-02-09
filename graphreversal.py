# we will be given a directed graph of n nodes with n-1 edges. 
# we need to find the minimal reversal of edges required such that all the edges are directed away from the root. 
# the root can be any node.
def solve():
    import sys
    sys.setrecursionlimit(200000)
    
    # Example Input: n nodes, edges list of (u, v)
    n = 6
    edges = [(0, 1), (2, 1), (3, 2), (3, 4), (5, 4)]
    
    adj = [[] for _ in range(n)]
    for u, v in edges:
        # (neighbor, cost_to_flip)
        # u -> v is free if we move away from u
        # v -> u costs 1 if we move away from u
        adj[u].append((v, 0))
        adj[v].append((u, 1))

    costs = [0] * n
    
    # First DFS to find cost for root 0
    def dfs1(u, p):
        total = 0
        for v, cost in adj[u]:
            if v != p:
                total += cost + dfs1(v, u)
        return total

    costs[0] = dfs1(0, -1)

    # Second DFS to reroot
    def dfs2(u, p):
        for v, cost in adj[u]:
            if v != p:
                if cost == 0: # Original was u -> v
                    costs[v] = costs[u] + 1
                else:         # Original was v -> u
                    costs[v] = costs[u] - 1
                dfs2(v, u)

    dfs2(0, -1)
    return min(costs)

print(f"Minimal reversals required: {solve()}")