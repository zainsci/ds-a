package main

import "fmt"

func bubble_sort(arr []int) []int {
	flag := true

	for flag {
		flag = false

		for i := 1; i < len(arr); i++ {
			if arr[i] < arr[i-1] {
				flag = true
				arr[i-1], arr[i] = arr[i], arr[i-1]
			}
		}
	}

	return arr
}

func main() {
	arr := []int{2, 4, 6, 1, 2, 0}
	fmt.Println(bubble_sort(arr))
}
