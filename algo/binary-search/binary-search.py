#! /bin/python3

def bin_search(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    if array[mid] < target:
        return bin_search(array, target, mid+1, end)

    if array[mid] > target:
        return bin_search(array, target, start, mid-1)


def main():
    array = [i for i in range(100)]
    target = 10
    start = 0
    end = len(array) - 1
    print(bin_search(array, target, start, end))


if __name__ == "__main__":
    main()
