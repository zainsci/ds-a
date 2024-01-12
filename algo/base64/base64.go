package main

import (
	"fmt"
	"strconv"
)

const BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

func Encode(input string) string {
	// 8-Bit binary string
	eight_bit_str := ""
	for _, char := range input {
		eight_bit_str = fmt.Sprintf("%s%.8b", eight_bit_str, char)
	}

	// List of 6-Bit binary strings
	var six_bits []string
	for i := 0; i < len(eight_bit_str); i = i + 6 {
		if i+6 < len(eight_bit_str) {
			six_bits = append(six_bits, eight_bit_str[i:i+6])
		} else {
			six_bits = append(six_bits, eight_bit_str[i:])
		}
	}

	// 0 Padding
	last_6b_index := len(six_bits) - 1
	padding := 6 - len(six_bits[last_6b_index])

	if len(six_bits[last_6b_index]) < 6 {
		for i := 0; i < padding; i++ {
			six_bits[last_6b_index] += "0"
		}
	}

	// 6-Bits to Decimal
	var decimals []int64
	for _, x := range six_bits {
		d, err := strconv.ParseInt(x, 2, 64)
		if err != nil {
			fmt.Println(err)
			return ""
		}

		decimals = append(decimals, d)
	}

	// Decimals to Base64 Encoded String
	var base64_str string
	for _, decimal := range decimals {
		base64_str += string(BASE64[decimal])
	}

	// Finally Padding of '='
	for i := 0; i < padding/2; i++ {
		base64_str += "="
	}
	return base64_str
}

func main() {
	// Tests
	fmt.Println(Encode("Hello!!"))
	fmt.Println("SGVsbG8hIQ==")

	fmt.Println(Encode("Zain"))
	fmt.Println("WmFpbg==")

	fmt.Println(Encode("We Are Lions!"))
	fmt.Println("V2UgQXJlIExpb25zIQ==")

	return
}
