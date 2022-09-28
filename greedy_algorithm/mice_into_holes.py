'''
Return minimum time required to place mice in holes using the greedy algorithm approach. We can put each mouse to its nearest hole to minimize the time. This can be done by sorting the positions of mice and holes.
'''

def assignHole(mice, holes):

    # Base -  number of mice and holes should be the same
    if len(mice) != len(holes):
        return "Number of mice and holes not the same"

    # Sort first
    mice.sort()
    holes.sort()

    # Finding the difference between ith mice and hole
    max_diff = 0

    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])

    return max_diff

mice = [4,-4,2]
holes = [4,0,5]

min_time = assignHole(mice, holes)

print(min_time)