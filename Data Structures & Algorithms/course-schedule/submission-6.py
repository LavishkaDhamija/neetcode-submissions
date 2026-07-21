class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = []
        adj = {}
        for i in range(numCourses):
            adj[i] = []
            for j in range(len(prerequisites)):
                if prerequisites[j][0] == i:
                    adj[i].append(prerequisites[j][1])
    

        def dfs(course,path):
            if course in path:
                return False
            if adj[course] == []:
                return True
            path.append(course)
            for prereq in adj[course]:
                if not dfs(prereq,path):
                    return False
            path.pop()
            adj[course] = []
            return True
            
            
        for i in range(len(adj)):
            path = []
            if not dfs(i,path):
                return False
        return True