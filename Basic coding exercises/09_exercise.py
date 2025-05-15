# 9. Check Palindrome Number

def is_palindrome(num):
    if num < 0:
        return False

    original_num = str(num)
    reversed_num = original_num[::-1]

    if reversed_num == original_num:
        return True
    return False

print(is_palindrome(123))
print(is_palindrome(12321))

print(is_palindrome(-85))
print(is_palindrome(15489))



