def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i

        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # element swapping
            j = j - 1

        i = i + 1
    return arr


def main():
    arr = [4, 7, 3, 1, 5, 8, 0, 6, 9, 2]
    new_arr = insertion_sort(arr)
    print(new_arr)


if __name__ == "__main__":
    main()
