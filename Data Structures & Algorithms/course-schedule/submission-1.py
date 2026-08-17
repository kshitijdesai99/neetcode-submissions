class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}
        for course, pre in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for pre in graph.get(course,[]):
                if not dfs(pre):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        # Time complexity - O(V+E)
        # Space complexity - O(V+E)