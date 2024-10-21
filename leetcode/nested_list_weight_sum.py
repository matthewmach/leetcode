class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        out = 0

        def helper(nestList, depth):
            out = 0
            for nest in nestList:
                nested = nest.getList()
                if nested:
                    out += helper(nested, depth+1)
                elif nest.isInteger():
                    out += nest.getInteger() * depth
            return out
        
        return helper(nestedList, 1)