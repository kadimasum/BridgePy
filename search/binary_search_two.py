def find_target(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if arr[mid]== target: return True
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return False

print(find_target([3,4,5,6,7], 46))

'''
Time complexity: O(n)
Space complexity: O(1)
'''