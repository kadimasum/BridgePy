def sortArr(nums):
    mid = len(nums) // 2
    left = sorted(nums[:mid])
    right = sorted(nums[mid:])
    c = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            c.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            c.append(insert)
        if len(left) > 0:
            for i in left:
                c.append(i)
        if len(right) > 0:
            for i in right:
                c.append(i)
        return c

print(sortArr([-2,5,3,1,-16, 9]))