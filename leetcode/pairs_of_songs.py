class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(time)):
            dic[time[i] % 60].append(i) 
        
        out = 0
        for key in dic:
            if key < 30:
                if key == 0:
                    if len(dic[key]) > 1:
                        out += int(len(dic[key]) * (len(dic[key])-1) /2)
                elif 60-key in dic:
                    out += len(dic[key]) * len(dic[60-key])
            elif key == 30:
                if len(dic[key]) > 1:
                    out += int(len(dic[key]) * (len(dic[key])-1) /2)
            print (out)
        return out