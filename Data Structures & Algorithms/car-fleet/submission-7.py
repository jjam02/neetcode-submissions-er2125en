class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Get position and speed map sorted in descending order
        # Because cars cannot overtake
        positionSpeed = [(p, s) for p, s in zip(position, speed)]
        positionSpeed.sort(reverse = True)

        # Use first car of each fleetas the bottleneck
        fleets = 0
        fleetTime = 0
        for p, s in positionSpeed:
            timeTaken = (target - p) / s
            if timeTaken > fleetTime:
                fleets += 1
                fleetTime = timeTaken

        return fleets