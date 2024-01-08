'''Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).'''
#LEETCODE - 797

from typing import List

class Solution:
    def dfs(self,graph,target_node,current_node,paths,current_path):
        if current_node == target_node:
            current_path.append(target_node)
            paths.append(current_path.copy())
            return
        current_path.append(current_node)
        for adj_node in graph[current_node]:
            self.dfs(graph,target_node,adj_node,paths,current_path)
            current_path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        current_path = []
        self.dfs(graph,len(graph)-1,0,paths,current_path)
        return paths