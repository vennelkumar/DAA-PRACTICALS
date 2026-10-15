# Time Complexity:
#   Best Case: O(n log n)
#   Average Case: O(n log n)
#   Worst Case: O(n^2)
# Space Complexity:
#   Average Case: O(log n)
#   Worst Case: O(n)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print(quick_sort(sample))
