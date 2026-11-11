class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_and_speed = []
        timeStack = []
        for i in range(len(position)):
            position_and_speed.append([position[i], speed[i]])

        position_and_speed.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(position_and_speed)):
            time = (target - position_and_speed[i][0]) / position_and_speed[i][1]
            if timeStack and timeStack[-1] >= time:
                continue
            else:
                timeStack.append(time)

        return len(timeStack)
        