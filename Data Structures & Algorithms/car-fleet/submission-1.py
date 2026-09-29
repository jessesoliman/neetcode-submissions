class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        fleets = [[position, speed[i]] for i, position in enumerate(position)]
        fleets.sort()
        num_fleets = len(fleets)
        for fleet in fleets:
            fleet.append((target-fleet[0])/fleet[1])
        l = len(fleets) - 2
        r = len(fleets) - 1
        while l > -1:
            while fleets[l][2] <= fleets[r][2] and l >= 0:
                num_fleets -= 1
                l -= 1
                print(num_fleets)
            r = l
            l -= 1

        return num_fleets
