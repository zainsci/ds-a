"""
A Simple Base64 Implementation
"""

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class Base64:
    def __init__(self) -> None:
        self.encoded_str = ""

        return None

    def encode(self, input_str):
        # Convert String chars to ASCII
        str_to_ascii = [ord(x) for x in input_str]

        # Convert ASCII to 8-Bit binary
        ascii_to_8bit = [format(x, "08b") for x in str_to_ascii]
        # Join 8-Bit binary into a single string
        ascii_to_8bit_str = "".join(ascii_to_8bit)

        # Converting 8-bit string to 6-bit binary
        to_6bit = []
        for i in range(0, len(ascii_to_8bit_str), 6):
            to_6bit.append(ascii_to_8bit_str[i:i+6])

        # Padding to add on the last 6-bit string
        padding = 6 - len(to_6bit[-1])
        to_6bit[-1] = to_6bit[-1] + (padding * "0")

        # Converting 6-bit binary to decimal numbers
        six_bit_to_decimal = [int(x, 2) for x in to_6bit]

        # Converting decimal to Base64 using BASE64 chart
        decimal_to_base64 = [BASE64[x] for x in six_bit_to_decimal]
        # Joining Base64 string
        base64_str = "".join(decimal_to_base64) + (int(padding/2) * "=")

        self.encoded_str = base64_str
        return base64_str

    def decode(self, encoded_str=""):
        if encoded_str == "" or encoded_str == None:
            encoded_str = self.encoded_str

        return encoded_str


def main():
    base64 = Base64()

    # Tests
    print(base64.encode("Hello!!"))
    print("SGVsbG8hIQ==")

    print(base64.encode("Zain"))
    print("WmFpbg==")

    print(base64.encode("We Are Lions!"))
    print("V2UgQXJlIExpb25zIQ==")


if __name__ == "__main__":
    main()
