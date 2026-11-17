class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        courses = defaultdict(list)
        for crs, pre in prerequisites:
            courses[crs].append(pre)

        visited = set()
        added = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crs in added:
                return True
            
            visited.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            del courses[crs]
            res.append(crs)
            added.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res

        #Time: O(V+E), where V=#crs, E=#pre
        #Space: O(V+E)