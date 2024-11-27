"""
Brute Force = O(n^2)
Can you make it n?
- how old can someone be
- You can make it n using a list of size 120
    - add the age to the index that would make a friend request to that age
- iterate through the friends again just adding the lengths of each list index
    - age[y] > 0.5 * age[x] +7
    - age[y] <= age[x]
    - O(n)
- another way of O(n)
- space complexity O(1)

another O(n) solution
- prefix sum
- requests = amount_in_ages[age] * (total_amount_until[age] - total_amount_until[age // 2 + 7] 
"""

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        to_friend = [0 for i in range(121)]

        for age in ages:
            y = int(age * 0.5 +7)
            for i in range(y+1, age+1):
                to_friend[i] += 1
        
        out = 0
        for age in ages:
            out += max(to_friend[age] -1, 0)
        
        return out