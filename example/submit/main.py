def isPalindrome(num: int) -> bool:
    num = abs(num)
    num_str = str(num)

    return num_str == num_str[::-1]


x = eval(input())

print(isPalindrome(x))
