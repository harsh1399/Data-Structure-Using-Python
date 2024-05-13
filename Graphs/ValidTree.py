'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
 write a function to check whether these edges make up a valid tree.
'''


from typing import List

class Solution:
    def check_cycle(self,graph,visited,current_node,prev_node):
        visited[current_node] = 1
        for adj_node in graph[current_node]:
            if adj_node!=prev_node and visited[adj_node] == 1:
                return True
            elif visited[adj_node] != 1:
                if self.check_cycle(graph,visited,adj_node,current_node):
                    return True
        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        if len(edges) == 0:
            return True
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        print(graph)
        for vertex in graph:
            if len(vertex) == 0:
                return False
        visited = [0]*n
        if self.check_cycle(graph,visited,0,None):
            return False
        for val in visited:
            if val == 0:
                return False
        return True
