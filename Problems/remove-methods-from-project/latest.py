class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]
        for a,b in invocations:
            graph[a].append(b)

        visited = [False]*n
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True

            for nxt in graph[node]:
                dfs(nxt)
        
        dfs(k)

        for u,v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))
        ans = []
        for i in range(n):
            if not visited[i]:
                ans.append(i)
        return ans

        