# Time Complexity:
#   Best Case: O(n)
#   Average Case: O(n)
#   Worst Case: O(n)
# Space Complexity: O(n)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    number = 5
    print(factorial(number))
