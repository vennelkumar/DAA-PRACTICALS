# Time Complexity:
#   Best Case: O(1)
#   Average Case: O(log n)
#   Worst Case: O(log n)
# Space Complexity: O(1)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    sample = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    result = binary_search(sample, target)
    print(result)
