# Time Complexity:
#   Best Case: O(1)
#   Average Case: O(n)
#   Worst Case: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    sample = [10, 23, 45, 70, 11, 15]
    target = 70
    result = linear_search(sample, target)
    print(result)
