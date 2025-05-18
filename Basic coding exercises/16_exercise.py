# 16. Check Palindrome Number

def is_palindrome(num):
    original_number = num
    reverse_number = 0
    while num > 0:
        rem = num % 10
        num //= 10
        reverse_number = reverse_number * 10 + rem

    if original_number == reverse_number:
        return True
    else:
        return False


n = int(input("Enter a number: "))
res= is_palindrome(n)
if res:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")

