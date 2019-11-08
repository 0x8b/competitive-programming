def square_root(n):
    assert n > 1

    left, right = 1, n

    while right - left >= 1e-12:
        mid = left + (right - left) / 2

        if mid ** 2 > n:
            right = mid
        else:
            left = mid

    return left


def iterative_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def recursive_binary_search(arr, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            return recursive_binary_search(arr, left, mid - 1, target)

        return recursive_binary_search(arr, mid + 1, right, target)

    return -1


assert [-1, 0, 1, 2, 3, -1, -1, -1] == [iterative_binary_search([1, 2, 3, 4], i) for i in range(8)]
assert [-1, 0, 1, 2, 3, 4, -1, -1] == [recursive_binary_search([1, 2, 3, 4, 5], 0, 4, i) for i in range(8)]
