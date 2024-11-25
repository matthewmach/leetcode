class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(A: str, B: str):
            if len(A) != len(B):
                return False
            if A == B:
                return True
            diff = []
            setA = set()
            dupe = False
            for i in range(len(A)):
                if A[i] in setA:
                    dupe = True
                setA.add(A[i])
                if A[i] != B[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            if len(diff) == 1:
                return False
            elif len(diff) == 2:
                return A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]
            else:
                return dupe
        
        sim_dict = defaultdict(list)

        for i in range(len(strs)):
            for j in range(i, len(strs)):
                if similar(strs[i], strs[j]):
                    sim_dict[i].append(j)
                    sim_dict[j].append(i)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in sim_dict[node]:
                dfs(neigh)
        
        out = 0
        for i in range(len(strs)):
            print (visited, i)
            if i in visited:
                continue
            dfs(i)
            out +=1
        
        return out