#! /bin/python3
import random


def merge(unsorted_list, start, mid, end):
    left_list = unsorted_list[start:mid + 1]
    right_list = unsorted_list[mid+1:end+1]
    left_list.append(float("inf"))
    right_list.append(float("inf"))
    i = 0
    j = 0
    for k in range(start, end + 1):
        if left_list[i] <= right_list[j]:
            unsorted_list[k] = left_list[i]
            i += 1
        else:
            unsorted_list[k] = right_list[j]
            j += 1
    return unsorted_list


def merge_sort(unsorted_list, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(unsorted_list, start, mid)
        merge_sort(unsorted_list, mid + 1, end)
        merge(unsorted_list, start, mid, end)
    return unsorted_list


def main():
    unsorted_list = [random.randint(0, 1000) for i in range(100)]
    start = 0
    end = len(unsorted_list) - 1
    print(unsorted_list)
    print(merge_sort(unsorted_list, start, end))


if __name__ == "__main__":
    main()
