# 19. Print Alternate Prime Numbers till 20

def prime_numbers():
    prime_nums = []
    for num in range(1,21):
        if num == 1:
            pass
        elif num in (2,3,5):
            prime_nums.append(num)
        else:
            if num % 2 == 0:
                pass
            elif num % 3 == 0:
                pass
            elif num % 5 == 0:
                pass
            else:
                prime_nums.append(num)

    print("All prime numbers from 1 to 20:")
    for num in prime_nums:
        print(num, end=' ')

    print("\n\nAlternate prime numbers:")
    for i,num in enumerate(prime_nums):
        if i%2==0:
            print(num, end=' ')

prime_numbers()


