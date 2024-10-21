class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        out = 0
        i_dic = defaultdict(list)
        i_dic[arr[0]] = [0]
        for j in range(1, len(arr)):
            for k in range(j+1, len(arr)):
                if target-arr[j]-arr[k] in i_dic:
                    out = (out + len(i_dic[target-arr[j]-arr[k]])) % 1000000007
            i_dic[arr[j]].append(j)
        
        return out

# optimal solution sorts the array then deals with same occurances
# sort is n log n so it's fine