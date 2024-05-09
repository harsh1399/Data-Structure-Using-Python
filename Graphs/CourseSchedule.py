## Leetcode - 207
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
        indegree = [0]*numCourses
        courseTaken = [False]*numCourses
        for adj_nodes in graph:
            for node in adj_nodes:
                indegree[node] += 1
        queue = list()
        for in_index in range(len(indegree)):
            if indegree[in_index] == 0:
                queue.append(in_index)
                courseTaken[in_index] = True
        while len(queue)!=0:
            course = queue.pop(0)
            for adj_nodes in graph[course]:
                indegree[adj_nodes] -= 1
                if indegree[adj_nodes] == 0:
                    queue.append(adj_nodes)
                    courseTaken[adj_nodes] = True
        for isCourseTaken in courseTaken:
            if not isCourseTaken:
                return False
        return True


