class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        courses = defaultdict(list)
        for crs, pre in prerequisites:
            courses[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if crs not in courses:
                return True
            
            visited.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            del courses[crs]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        #Time: O(V+E)
        # Space: O(V+E), V = number of courses, E = # prereqs

        


                