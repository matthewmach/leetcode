"""
- Time Complexity: O(n alpha(n))
    - alpha(n) is the inverse Ackermann function (nearly constant) better than nlogn thing
    
- Space Complexity: O(kn) = O(n)
- can ask how many emails one could have, how many emails total
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parents = list(range(len(accounts)))
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(child, parent):
            parents[find(child)] = find(parent)
        
        ownership = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in ownership:
                    union(i, ownership[email])
                ownership[email] = i
        
        emails = defaultdict(list)
        for email, owner in ownership.items():
            emails[find(owner)].append(email)
        
        out = []
        for i, emails in emails.items():
            account = []
            account.append(accounts[i][0])
            out.append(account + sorted(emails))

        return out