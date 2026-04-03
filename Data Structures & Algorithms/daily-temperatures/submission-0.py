class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        #  pair (temp, index)
        stack = [] 
        
        for i, temp in enumerate(temperatures):
            # we traverse through stack to find hotter temp day
            while stack and temp > stack[-1][0]:
                prevtemp, prevind = stack.pop()
                res[prevind] = i - prevind
            stack.append((temp, i))

        return res