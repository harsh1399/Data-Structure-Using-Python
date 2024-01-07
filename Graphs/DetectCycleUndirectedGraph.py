'''Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. '''

##using DFS
from typing import List

class Solution:

    def dfs(self, current_node, adj, parent, visited):
        visited[current_node] = 1
        for adj_node in adj[current_node]:
            if parent != adj_node and visited[adj_node] == 1:
                return 1
            elif visited[adj_node] == 0:
                if self.dfs(adj_node, adj, current_node, visited) == 1:
                    return 1
        return 0

        # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V
        for index in range(len(visited)):
            if visited[index] == 0:
                if self.dfs(index, adj, -1, visited) == 1:
                    return 1
        return 0

##using BFS
class BFSSolution:
    # Function to detect cycle in an undirected graph.
    def detectCycle(self, visited, adj, starting_node):
        queue = list()
        queue.append((starting_node, starting_node))
        visited[starting_node] = 1
        while (len(queue) != 0):
            item, starting = queue.pop(0)
            for adjacent in adj[item]:
                if visited[adjacent] == 0:
                    queue.append((adjacent, item))
                    visited[adjacent] = 1
                elif adjacent != starting and visited[adjacent] == 1:
                    return True
        return False

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here
        visited = [0] * V
        for i in range(V):
            if visited[i] != 1:
                if self.detectCycle(visited, adj, i) == True:
                    return True
        return False

# {
# Driver Code Starts

if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends




