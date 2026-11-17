class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # check has Cycle
        def hasCycle(graph, a, b):
            visited = set()
            def dfs(node, parent):
                if node in visited:
                    return True
    
                visited.add(node)
                for nei in graph[node]:
                    if nei == parent or {nei, node} == {a, b}:
                        continue
                    if dfs(nei, node):
                        return True
                return False

            for i in range(1, n+1):
                if i not in visited and dfs(i, -1):
                    return True
            return False
        
        for a, b in reversed(edges):
            if not hasCycle(graph, a, b):
                return [a,b]
        
        
        
