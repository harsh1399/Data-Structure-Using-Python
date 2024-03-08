"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
from typing import Optional


class Solution:
    def clone(self, current_node, visited_dict):
        new_node = Node()
        new_node.val = current_node.val
        visited_dict[new_node.val] = new_node
        for adj in current_node.neighbors:
            if adj.val not in visited_dict:
                self.clone(adj, visited_dict)
            if adj.val in visited_dict:
                new_node.neighbors.append(visited_dict[adj.val])
        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        elif len(node.neighbors) == 0:
            new_node = Node()
            new_node.val = node.val
            new_node.neighbors = []
            return new_node
        visited_dict = {}
        return self.clone(node, visited_dict)
