class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
            for j in range(len(prerequisites)):
                if prerequisites[j][0] == i:
                    adj[i].append(prerequisites[j][1])

        ans = []
        visited = set()          # NEW

        def dfs(course, path):
            nonlocal ans

            if course in path:
                return False

            if course in visited:    # NEW
                return True

            path.append(course)

            for c in adj[course]:
                if not dfs(c, path):
                    return False

            path.pop()
            visited.add(course)      # NEW
            ans.append(course)

            return True

        for i in range(numCourses):
            path = []
            if not dfs(i, path):
                return []

        return ans