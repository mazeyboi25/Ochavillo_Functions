def smallest_factor(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


def optimus_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))


def find_smallest_factor():
    n = int(input("Enter a number to find its smallest factor: "))
    factor = smallest_factor(n)
    print(f"The smallest factor of {n} is: {factor}")


def find_prime_numbers(start, end):
    optimum = [num for num in range(start, end + 1) if optimus_prime(num)]
    return optimum


while True:
    print("Choose something, thank you :D :")
    print("1. Find the smallest factor of a number")
    print("2. Find prime numbers in a range")
    print("3. Bye-bye!")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        find_smallest_factor()
    elif choice == '2':
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start >= end:
            print("Invalid range. Start should be less than end.")
            continue

        optimum = find_prime_numbers(start, end)
        print(f"Prime numbers between {start} and {end} are: {optimum}")
    elif choice == '3':
        print("Program terminated.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
