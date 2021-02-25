# Find if number is divisible by number
# Rules from https://www.mathsisfun.com/divisibility-rules.html
def inputValue():
    while True:
        value = input("Please enter a number or quit (q): \n")
        if value.isdigit():
            return value
        elif value == "q" or value == "quit":
            break
        else:
            print("You entered: " + value)
            continue


# see if number is divisible by 1
def divisibleBy1(number):
    print(number + " is divisible by 1")
    return True


# see if number is divisible by 2
# Rule: The last digit is even
def divisibleBy2(number):
    if int(number) % 2 == 0:
        print(number + " is divisible by 2")
        return True
    else:
        print(number + " is not divisible by 2")
        return False


# see if number is divisible by 3
# Rule: The sum of the digits is divisible by 3
def divisibleBy3(number):
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    if sum % 3 == 0:
        print(number + " is divisible by 3")
        return True
    else:
        print(number + " is not divisible by 3")
        return False


# see if number is divisible by 4
# Rule: The last 2 digits are divisible by 4
def divisibleBy4(number):
    lastTwoDigit = int(number) % 100
    if lastTwoDigit % 4 == 0:
        print(number + " is divisible by 4")
        return True
    else:
        print(number + " is not divisible by 4")
        return False


# see if number is divisible by 5
# Rule: The last digit is 0 or 5
def divisibleBy5(number):
    if int(number) % 10 == 0 or int(number) % 10 == 5:
        print(number + " is divisible by 5")
        return True
    else:
        print(number + " is not divisible by 5")
        return False


# see if number is divisible by 6
# Rule: Is even and is divisible by 3
def divisibleBy6(number):
    if int(number) % 2 == 0 and int(number) % 3 == 0:
        print(number + " is divisible by 6")
        return True
    else:
        print(number + " is not divisible by 6")
        return False


# see if number is divisible by 7
# Rule: Double the last digit and subtract it from a number made by the other digits.
# The result must be divisible by 7.
def divisibleBy7(number):
    newnum = 0
    newnum = (2 * int(number) % 100) - int(number) // 10
    if newnum % 7 == 0:
        print(number + " is divisible by 7")
        return True
    else:
        print(number + " is not divisible by 7")
        return False


# see if number is divisible by 8
# The last three digits are divisible by 8
def divisibleBy8(number):
    if (int(number) % 1000) % 8 == 0:
        print(number + " is divisible by 8")
        return True
    else:
        print(number + " is not divisible by 8")
        return False


# see if number is divisible by 9
# Rule: The sum of the digits is divisible by 9
def divisibleBy9(number):
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    if sum % 9 == 0:
        print(number + " is divisible by 9")
        return True
    else:
        print(number + " is not divisible by 9")
        return False


def main():
    choice = ""
    number = ""
    while True:
        number = inputValue()
        if str(number).isnumeric():
            divisibleBy1(number)
            divisibleBy2(number)
            divisibleBy3(number)
            divisibleBy4(number)
            divisibleBy5(number)
            divisibleBy6(number)
            divisibleBy7(number)
            divisibleBy8(number)
            divisibleBy9(number)
        else:
            break

        print("\nWhat would you like to insert another number? (y/n) ")
        if input(choice).upper() == "Y":
            continue
        else:
            break


main()
