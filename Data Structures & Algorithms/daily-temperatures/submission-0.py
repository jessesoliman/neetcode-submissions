class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temps = deque([[temperatures[0], 0]])
        print(temps[0])
        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[i-1]:
                while temperatures[i] > temps[len(temps)-1][0]: # pop and add while greater
                    pop = temps.pop()
                    res[pop[1]] = i - pop[1]
                    if len(temps) == 0:
                        break
            temps.append([temperatures[i], i])
        return res
